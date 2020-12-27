# Packages
from sys import argv
import inquirer

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
  # Latest flags
  elif ('latest' in argv) and (argv[1] == 'latest'):
    available_versions = get_versions('all')
    version = available_versions[0]
    display_message(['The latest available version of terraform is ' + str(version),''])
    if ('show' in argv) and (argv[2] == 'show'):
      return True
    # Display a CLI UI to the user to pick yes or no
    questions = [inquirer.List('latest', message='Would you like to switch to '+ version + '?', choices=['Yes','No'])]
    # Get the users choice
    answers = inquirer.prompt(questions)
    if answers['latest'] == 'Yes':
      display_message(['Switchng to ' + str(version)])
      switch_version(version)
      display_message(['Switch Successful: ' + str(version)])
      return True
    else:
      questions = [inquirer.List('version', message='Would you like to switch to another version?', choices=['Yes','No'])]
      # Get the users choice
      answers = inquirer.prompt(questions)
      if answers['version'] == 'Yes':
        return False
      else:
        display_message(['Exiting'])
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
        # Get a list of available terraform versions
        display_message(['Switchng to ' + str(version)])
        available_versions = get_versions('all')
        if version.lower() == 'latest':
          version = available_versions[0]
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
