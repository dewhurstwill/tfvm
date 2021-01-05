
#################################
#                               #
#        Install Script         #
#                               #
#################################

# Constants
version='0.0.9'
zip_url="https://codeload.github.com/dewhurstwill/tfvm/zip"
zip_download_location="${HOME}/Downloads/tfvm-v${version}.zip"
bin_download_location="${HOME}/Downloads/tfvm-${version}/dist/tfvm"

# Downloading
echo Downloading
curl -s --output $zip_download_location $zip_url

# Unpacking
unzip $zip_download_location -q -d "${HOME}/Downloads"

# Making binary executable
chmod +x $bin_download_location

# Installing
echo Installing
sudo mv $bin_download_location /usr/local/bin/tfvm
sudo ln -s ~/.terraform.versions/terraform /usr/local/bin/terraform

# Cleanup
echo Cleaning up
rm $zip_download_location
rm -r "${HOME}/Downloads/tfvm-v${version}"

# Done
echo Done
