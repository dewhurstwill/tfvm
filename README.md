# tfvm [ Terraform Version Manager ] 🔧

Terraform Version Manager

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=dewhurstwill_tfvm&metric=ncloc)](https://sonarcloud.io/dashboard?id=dewhurstwill_tfvm)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=dewhurstwill_tfvm&metric=bugs)](https://sonarcloud.io/dashboard?id=dewhurstwill_tfvm)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=dewhurstwill_tfvm&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=dewhurstwill_tfvm)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=dewhurstwill_tfvm&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=dewhurstwill_tfvm)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=dewhurstwill_tfvm&metric=security_rating)](https://sonarcloud.io/dashboard?id=dewhurstwill_tfvm)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=dewhurstwill_tfvm&metric=sqale_index)](https://sonarcloud.io/dashboard?id=dewhurstwill_tfvm)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=dewhurstwill_tfvm&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=dewhurstwill_tfvm)

![GitHub repo size](https://img.shields.io/github/repo-size/dewhurstwill/tfvm?style=flat-square)

## Install 📦 & Run 💻

| Steps 📝 | Commands 💻 |
|-|-|
| Step 1 | Install [Python 3.x](https://www.python.org/downloads/) <=|
| Step 2 | Install [Pip 3.x](https://pip.pypa.io/en/stable/installing/) <= |
| Step 3 | ``` /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/dewhurstwill/tfvm/main/setup.sh)" ``` |
| Step 4 | ``` tfvm help ``` |


## Uninstall 📦

```bash 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/dewhurstwill/tfvm/main/uninstall.sh)" 
```


## Required python packages:

Handled by [setup.sh](https://github.com/dewhurstwill/tfvm/blob/main/setup.sh)

* [blessed](https://pypi.org/project/blessed/) 
  * ![PyPI - Downloads](https://img.shields.io/pypi/dm/blessed?style=flat-square)
  * ![PyPI - License](https://img.shields.io/pypi/l/blessed?style=flat-square)
  * inquirer dependency
  * Blessed is an easy, practical library for making terminal apps, by providing an elegant, well-documented interface to Colors, Keyboard input, and screen position and Location capabilities.
* [readchar](https://pypi.org/project/readchar/) 
  * ![PyPI - Downloads](https://img.shields.io/pypi/dm/readchar?style=flat-square)
  * ![PyPI - License](https://img.shields.io/pypi/l/readchar?style=flat-square)
  * inquirer dependency
  * Born as a python-inquirer requirement.
  * The idea is to have a portable way to read single characters and key-strokes.
* [python-editor](https://pypi.org/project/python-editor/) 
  * ![PyPI - Downloads](https://img.shields.io/pypi/dm/python-editor?style=flat-square)
  * ![PyPI - License](https://img.shields.io/pypi/l/python-editor?style=flat-square)
  * inquirer dependency
  * python-editor is a library that provides the editor module for programmatically interfacing with your system’s $EDITOR.
* [inquirer](https://pypi.org/project/inquirer/)
  * ![PyPI - Downloads](https://img.shields.io/pypi/dm/inquirer?style=flat-square)
  * ![PyPI - License](https://img.shields.io/pypi/l/inquirer?style=flat-square)
  * Collection of common interactive command line user interfaces, based on Inquirer.js.
