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
![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/dewhurstwill/tfvm?include_prereleases&sort=semver&style=flat-square)


## Install 📦 & Run 💻

```bash
curl -fsSL https://raw.githubusercontent.com/dewhurstwill/tfvm/main/setup.sh | bash
tfvm help
```


## Uninstall 📦

```bash 
curl -fsSL https://raw.githubusercontent.com/dewhurstwill/tfvm/main/uninstall.sh | bash
```

## Required python packages

Handled by [build.sh](https://github.com/dewhurstwill/tfvm/blob/main/build.sh)


* [requests](https://pypi.org/project/requests/) 
  * ![PyPI - Downloads](https://img.shields.io/pypi/dm/requests?style=flat-square)
  * ![PyPI - License](https://img.shields.io/pypi/l/requests?style=flat-square)
  * Requests is a simple, yet elegant HTTP library.
* [inquirer](https://pypi.org/project/inquirer/)
  * ![PyPI - Downloads](https://img.shields.io/pypi/dm/inquirer?style=flat-square)
  * ![PyPI - License](https://img.shields.io/pypi/l/inquirer?style=flat-square)
  * Collection of common interactive command line user interfaces, based on Inquirer.js.
  

More can be found in [requirements.txt](https://github.com/dewhurstwill/tfvm/blob/main/requirements.txt)


## Want to build your own binary

| Step | Action |
|-|-|
| Step 1 | Clone the repo |
| Step 2 | Navigate to the repo |
| Step 3 | Run build.sh |
| Step 4 | Consume the binary from the dist folder |
  
  
## Screenshots
  
| Command | Screenshot |
|-|-|
| ```tfvm ``` | ![tfvm screenshot](https://imgur.com/BZUVEGW.png "tfvm") |
| ```tfvm help``` | ![tfvm help screenshot](https://imgur.com/4brR0oe.png "tfvm help") |
| ```tfvm version``` | ![tfvm version](https://imgur.com/fqee855.png "tfvm version") |
| ```tfvm select <version>``` | ![tfvm select](https://imgur.com/QZo7OdW.png "tfvm select") |
| ```tfvm latest``` | ![tfvm latest](https://imgur.com/rKvTjhI.png "tfvm latest") |

## Platforms

| Platform | Tested On | Working On |
|-|-|-|
| Mac OSX 11.0.1 | ✅ | ✅ |
| Ubuntu 20.10 | ✅ | ✅ |
| Windows 10 | ✅ | ❌ |

* This should now work on windows however it has not been tested
