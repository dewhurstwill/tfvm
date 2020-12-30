#################################
#                               #
#        Install Script         #
#                               #
#################################

# Constants
version='0.0.9'
new_dir='/usr/local/bin/tfvm'
repo_url='https://codeload.github.com/dewhurstwill/tfvm/zip'

# Check if python3 is installed
python3 -V

# Check if pip3 is installed
pip3 -V


# Setting some dynamic variables
current_dir=$(pwd)
pkg_dir="${new_dir}/tfvm-${version}"
zip_path="${new_dir}/tfvm-v${version}.zip"


# Creating Log Location
echo Creating log location
mkdir ~/.tfvm
mkdir ~/.tfvm/logs
touch ~/.tfvm/logs/install.log


# Creating Install Location
echo Creating install location
sudo mkdir $new_dir
cd $new_dir


# Downloading
echo Downloading
sudo curl --output $zip_path --slient "${repo_url}/v${version}"


# Unpacking
echo Unpacking
sudo unzip -q $zip_path


# Installing
echo Installing 
sudo cp -r ${pkg_dir}/* . 2>&1 >> ~/.tfvm/logs/install.log
pip3 install -r requirements.txt 2>&1 >> ~/.tfvm/logs/install.log
sudo ln -s ~/.terraform.versions/terraform /usr/local/bin/terraform 2>&1 >> ~/.tfvm/logs/install.log


# Cleaning Up
echo Cleaning Up
sudo rm $zip_path
sudo rm -r $pkg_dir


# Adding Alias 
string_to_check='alias tfvm'
if grep -q "$string_to_check" ~/.bashrc ; then
  echo "Already in .bashrc, Skipping..." 2>&1 >> ~/.tfvm/logs/install.log ;
else
  echo "Adding alias to bashrc" 2>&1 >> ~/.tfvm/logs/install.log ;
  echo "alias tfvm='python3 ${new_dir}/main.py'" >> ~/.bashrc ; 
fi

if grep -q "$string_to_check" ~/.bash_profile ; then
  echo "Already in .bash_profile, Skipping..." 2>&1 >> ~/.tfvm/logs/install.log ; 
else
  echo "Adding alias to bash_profile" 2>&1 >> ~/.tfvm/logs/install.log ;
  echo "alias tfvm='python3 ${new_dir}/main.py'" >> ~/.bash_profile ;
fi 


# Done
echo Done
cd $current_dir
