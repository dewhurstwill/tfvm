# Packages
import platform, sys
from os.path import expanduser, isdir, islink, exists
from os import environ, rmdir, mkdir, remove, symlink

# Config
from config import terraform_install_location, nix_bin_path, win_bin_path


# Helper Module for checking if terraform is in the system PATH environment variable
def is_tf_in_path(path_list: list):
  # Loop over the path list and return any paths that include terraform
  # If greater than 0
  if len([index for index, current_string in enumerate(path_list) if 'terraform' in current_string]) > 0:
    return isdir(win_bin_path)
  else:
    return islink(nix_bin_path)


# Helper Module for retreiving and parsing the PATH environment variable
def handle_path():
  path = environ['PATH']
  path_delimeter = ':' # Default *nix delimiter

  # If windows
  if platform.system() == 'Windows': 
    # Swap to use ; instead
    path_delimiter = ';'

  # Split and return the string
  path_list = path.split(path_delimiter)
  return path_list
