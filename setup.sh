
#################################
#                               #
#        Install Script         #
#                               #
#################################

# Constants
version='0.1.0'
zip_url="https://codeload.github.com/dewhurstwill/tfvm/zip/v${version}"
zip_download_location="${HOME}/Downloads/tfvm-v${version}.zip"
bin_download_location="${HOME}/Downloads/tfvm-${version}/dist/tfvm"

# Downloading
echo Downloading
curl -s --output $zip_download_location $zip_url

# Unpacking
echo Unpacking
unzip -q -d "${HOME}/Downloads" $zip_download_location

# Making binary executable
chmod +x $bin_download_location

# Installing
echo Installing
sudo mv $bin_download_location /usr/local/bin/tfvm
sudo ln -s ~/.terraform.versions/terraform /usr/local/bin/terraform

# Cleanup
echo Cleaning up
rm $zip_download_location
rm -r "${HOME}/Downloads/tfvm-${version}"

# Done
echo Done
