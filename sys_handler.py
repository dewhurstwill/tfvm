# Packages
import platform

# Use platform package to work out which architecture the script is running on
# This is used to download the correct version of terraform
def get_architecture():
  arch = platform.processor()
  if is_os_64bit():
    if 'arm' in arch:
      return 'arm64'
    else:
      return 'amd64'
  else:
    if 'arm' in arch:
      return 'arm'
    else:
      return '386'

# Use the platform package to work out of the system is 64 or 32 bit
# This is also used to download the correct version of terraform
def is_os_64bit():
  return platform.machine().endswith('64')
