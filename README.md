# tfvm [ Terraform Version Manager ] 🔧

Terraform Version Manager

## Install 📦 & Run 💻

| Steps 📝 | Commands 💻 |
|-|-|
| Step 1 | ``` /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/dewhurstwill/tfvm/main/setup.sh)" ``` |
| Step 2 | ``` tfvm help ``` |


## Uninstall 📦

```bash 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/dewhurstwill/tfvm/main/uninstall.sh)" 
```


Required python packages:

* [blessed](https://pypi.org/project/blessed/)
  * inquirer dependency
  * Blessed is an easy, practical library for making terminal apps, by providing an elegant, well-documented interface to Colors, Keyboard input, and screen position and Location capabilities.
* [readchar](https://pypi.org/project/readchar/)
  * inquirer dependency
  * Born as a python-inquirer requirement.
  * The idea is to have a portable way to read single characters and key-strokes.
* [python-editor](https://pypi.org/project/python-editor/)
  * inquirer dependency
  * python-editor is a library that provides the editor module for programmatically interfacing with your system’s $EDITOR.
* [inquirer](https://pypi.org/project/inquirer/)
  * Collection of common interactive command line user interfaces, based on Inquirer.js.
