# Packages
import requests, platform
from shutil import copyfile
from os.path import exists, expanduser

# Helper Modules
from sys_handler import get_architecture
from file_handler import check_if_version_exists, download_terraform, make_executable, initialise
from env_handler import is_tf_in_path, handle_path

# Config
from config import terraform_install_location, nix_bin_path, win_bin_path, path_style

# Scrapes the terraform website for a list of available versions
def get_versions(versions_to_return: str = 'all'):
  all_tf_versions = []
  standard_tf_versions = []
  alpha_tf_versions = []
  beta_tf_versions = []
  rc_tf_versions = []

  tf_versions_url = 'https://releases.hashicorp.com/terraform/'
  tf_versions_html = requests.get(tf_versions_url)

  # Check if the request was successful
  if tf_versions_html.ok:
    tf_versions_list = tf_versions_html.text.split('\n')
    for row in tf_versions_list:
      # If line includes html a tag with a link which starts with /terraform/
      if '<a href="/terraform/' in row:
        # Split link to get version (/terraform/<VERSION HERE>/)
        version = (row.split('/'))[2]
        # Create a list of all versions
        if versions_to_return == '' or versions_to_return == 'all':
          all_tf_versions.append(version)
        else:
          if 'alpha' in version and versions_to_return == 'alpha':
            # Create a list of versions which include alpha
            alpha_tf_versions.append(version)
          elif 'beta' in version and versions_to_return == 'beta':
            # Create a list of versions which include beta
            beta_tf_versions.append(version)
          elif 'rc' in version and versions_to_return == 'rc':
            # Create a list of versions which includes rc (release candidate)
            rc_tf_versions.append(version)
          elif versions_to_return == 'standard' and ('alpha' not in version) and ('beta' not in version) and ('-rc' not in version):
            # Create a list of versions which does not include alpha or beta
            standard_tf_versions.append(version)

    if versions_to_return == 'standard':
      return standard_tf_versions
    elif versions_to_return == 'alpha':
      return alpha_tf_versions
    elif versions_to_return == 'beta':
      return beta_tf_versions
    else:
     return all_tf_versions
  else:
    # If request was unsuccessful throw an error message
    print('Unable to query for available terraform versions')

# Sets the active version of terraform
def set_active_version(version: str):
  destination_file = terraform_install_location + path_style + 'terraform'
  selected_version_file = destination_file + '_' + version

  if platform.system() == 'Windows':
    selected_version_file += '.exe'
    destination_file += '.exe'
  
  copyfile(selected_version_file, destination_file)
  
  if platform.system() != 'Windows':
    make_executable(destination_file)

# Switch version helper, checks if a cached version is available to switch to, if not it will download it
def switch_version(version: str = ''):
  if not exists(terraform_install_location):
    initialise('install')
    
  if not check_if_version_exists(version):
    download_terraform(version)
  
  set_active_version(version)
