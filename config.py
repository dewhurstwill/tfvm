# Packages
import platform
from os.path import expanduser

# tfvm version
version = '0.0.5'

# Support for Windows/*nix file systems
path_style = '/'
if platform.system() == 'Windows':
  path_style = '\\'

# Various terraform variables
terraform_base_url = 'https://releases.hashicorp.com/terraform/'
terraform_base_location = expanduser('~') + path_style
terraform_install_location = terraform_base_location + '.terraform.versions'
terraform_temp_location = terraform_base_location + '.terraform.temp'

# Binary paths
win_bin_path = 'C:\\bin\\terraform'
nix_bin_path = '/usr/local/bin/terraform'