#################################
#                               #
#        Uninstall Script       #
#                               #
#################################

echo Cleaning Up
# Removing Source Directory
sudo rm /usr/local/bin/tfvm
# Removing terraform symbolic link
sudo unlink /usr/local/bin/terraform
echo Done
