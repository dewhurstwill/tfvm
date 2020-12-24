def display_message(message: list):
  for l in message:
    print(str(l))

def help_message():
  display_message([
    'Usage: tfvm [-h, --h, -help, --help] [-v, --v, -version, --version] <command> [args]',
    '',
    'The available commands for execution are listed below.',
    '',
    'Commands:',
    '  version            - Display the current version of terraform version manager',
    '  select [<Version>] - Specify a valid semantic version to switch to',
    '  reset              - Resets terraform version manager',
    '  purge              - Alias for reset'
  ])

def version_message():
  display_message(['Version: ' + version])
