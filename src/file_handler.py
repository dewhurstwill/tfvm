# Packages
import platform, requests, sys, stat
from zipfile import ZipFile as zipfile
from os import mkdir, rmdir, rename, walk, chmod
from os import stat as os_stat
from os import remove as deletefile
from os.path import exists, expanduser, isfile, isdir

# Helper Modules
from sys_handler import get_architecture, is_os_64bit

#Config
from config import terraform_install_location, terraform_temp_location, nix_bin_path, win_bin_path, terraform_base_url, path_style


# Initialise helper, used to create various terraform directories if they don't exist
def initialise(target: str):
  if target == 'install' and not exists(terraform_install_location):
    mkdir(terraform_install_location)
  elif target == 'temp' and not exists(terraform_temp_location):
    mkdir(terraform_temp_location)


# Purge helper, used to remove dangling terraform binaries
def purge():
  for location in [terraform_install_location, terraform_temp_location]:
    directories = []
    files = []
    if(exists(location)):
      for (dirpath, dirnames, filenames) in walk(location):
        files.extend(filenames)
        directories.extend(dirnames)
        break
      
      if len(directories) > 0:
        print('Please manually remove all subdirectories under ' + location + ' then try again')
      else:
        for file in files:
          if file != 'terraform':
            deletefile(terraform_install_location + path_style + file)
        if 'temp' in location:
          rmdir(location)


# Runs chmod to make terraform binary executable after downloading
def make_executable(file: str):
  st = os_stat(file)
  chmod(file, st.st_mode | stat.S_IEXEC)


# Downloads, Unpacks and gets terraform ready for use
def download_terraform(version: str):
  url = terraform_base_url + version
  system = str(platform.system()).lower()
  arch = get_architecture()

  file = 'terraform_' + version + '_' + system + '_' + arch + '.zip'

  initialise('temp')
  with open(terraform_temp_location + path_style + file, 'wb') as f:
    print('Downloading %s' % file)
    res = requests.get(url + '/' + file, stream=True)
    total_length = res.headers.get('Content-length')
    if total_length is None:
      f.write(res.content)
    else:
      dl = 0
      total_length = int(total_length)
      for data in res.iter_content(chunk_size=4096):
        dl += len(data)
        f.write(data)
        done = int(50 * dl / total_length)
        sys.stdout.write("\r[%s%s]" % ('#' * done, ' ' * (50-done)) )
        sys.stdout.flush()

  print('')
  with zipfile(terraform_temp_location + path_style + file, 'r') as zip_ref:
    print('Extracting %s' % file)
    zip_ref.extractall(terraform_temp_location)
  print('Extracted')
  print('Renaming extracted file')
  base_file = path_style + 'terraform'
  extracted_file = terraform_temp_location + base_file
  renamed_file = terraform_install_location + base_file + '_' + version

  if platform.system() == 'Windows':
    extracted_file += '.exe'
    renamed_file += '.exe'

  rename(extracted_file, renamed_file)

  if platform.system() != 'Windows':
    make_executable(renamed_file)

  print('Cleaning Up')
  deletefile(terraform_temp_location + path_style + file)


# Checks if a specified version of terraform is already cached
def check_if_version_exists(version: str):
  if (exists(terraform_install_location) and isdir(terraform_install_location)):
    terraform_file = terraform_install_location + path_style + 'terraform_' + version
    return (exists(terraform_file) and isfile(terraform_file))
  else:
    return False
    