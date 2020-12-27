# Packages
from sys import argv

# Helper Modules
from message_handler import help_message, version_message, display_message
from env_handler import is_tf_in_path, handle_path
from terraform_handler import switch_version, get_versions
from file_handler import purge, initialise


# Handles flags passed to the script
def cli_args():
  # Help flags
  if ('-h' in argv) or ('--h' in argv) or ('-help' in argv) or ('--help' in argv) or ('help' in argv):
    # Display help message
    help_message()
    # Return true so the user is not prompted to select a version
    return True
  # Version flags
  elif ('-v' in argv) or ('--v' in argv) or ('-version' in argv) or ('--version' in argv) or ('version' in argv):
    # Display the version message
    version_message()
    # Return true so the user is not prompted to select a version
    return True
  # Reset/Purge flags
  elif (('reset' in argv) and (argv[1] == 'reset')) or (('purge' in argv) and (argv[1] == 'purge')):
    # Check to see if terraform is in $PATH
    if is_tf_in_path(handle_path()):
      display_message(['Purging'])
      # Call a number of helper modules
      purge()
      initialise('install')
      initialise('temp')
      display_message(['Purged'])
    # Return true so the user is not prompted to select a version
    return True
  # Select flags
  elif ('select' in argv) and (argv[1] == 'select'):
    if len(argv) > 2:
      # The select flag must be followed by a version
      # Select will always be in position 1 so then we can safely assume the version
      # will be in position 2
      version = argv[2]
      # Check to ensure the version is not null
      if version != '':
        display_message(['Switchng to ' + str(version)])
        # Get a list of available terraform versions
        available_versions = get_versions('all')
        # Check to see if the user inputted version is in the list of available versions
        if version in available_versions:
          # If true, call the switch version helper
          switch_version(version)
          display_message(['Switch Successful: ' + str(version)])
        else:
          display_message(['', str(version) + ' is an invalid version'])
      else:
        display_message(['', 'Version requires a valid value'])
    else:
        display_message(['', 'Version requires a valid value'])
    # Return true so the user is not prompted to select a version
    return True
  else:
    # Return false so the user is prompted for a version
    return False
