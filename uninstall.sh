#################################
#                               #
#        Uninstall Script       #
#                               #
#################################


echo Cleaning Up
# Removing Source Directory
sudo rm -r /usr/local/bin/tfvm
# Removing terraform symbolic link
sudo unlink /usr/local/bin/terraform
# Cleaning up previous .tfvm.removed
sudo rm -r ~/.tfvm.removed
# Moving current install to .tfvm.removed
mv ~/.tfvm ~/.tfvm.removed
echo Done