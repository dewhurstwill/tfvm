@ECHO OFF
@REM WORK IN PROGRESS
iexplore https://www.python.org/downloads/
echo Please ensure you have python 3.8 or greater installed
timeout 240
echo Ensure your have pip installed
py -m ensurepip --default-pip
echo Creating a binaries directory for the terraform symlink 
mkdir C:\bin
echo Creating a sym link for the active terraform binary
mklink C:\bin\terraform C:\Users\%USERNAME%\.terraform.versions\terraform
echo Adding the new bin folder to the PATH environment variable
setx /M path "%path%;C:\bin\"
echo Installing dependencies
pip3 install -r requirements.txt