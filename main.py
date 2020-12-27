# Packages
import inquirer

#Helper Modules
from cli_handler import cli_args
from terraform_handler import get_versions, switch_version
from message_handler import display_message


# If not CLI flags have been passed
if not cli_args():
  # Get a list of all available terraform versions
  available_versions = get_versions('all')
  # Display a CLI UI to the user to pick a version
  questions = [inquirer.List('version', message='Select a version', choices=available_versions)]
  # Get the users choice
  answers = inquirer.prompt(questions)
  display_message(['Switchng to ' + str(answers['version'])])
  # Swtich to the requested version
  switch_version(answers['version'])
  display_message(['Switch Successful: ' + str(answers['version'])])
