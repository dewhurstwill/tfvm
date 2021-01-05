#################################
#                               #
#        Install Script         #
#            (BETA)             #
#################################

# Constants
$version = "0.1.0-beta"
$url = 'https://codeload.github.com/dewhurstwill/tfvm/zip/v' + $version
$output_zip = "C:\$env:HOMEPATH\" + $zip_name
$output_dir = "C:\$env:HOMEPATH\.tfvm"

if (!(Test-Path -Path C:\$env:HOMEPATH\.tfvm))
{
    New-Item "C:\$env:HOMEPATH\.tfvm" -itemtype directory
}

$oldpath = (Get-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH).path
if (!($oldpath -like "*.terraform.versions*"))
{
    $newpath = "$oldpath;" + "C:\$env:HOMEPATH\.terraform.versions"
    Set-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH -Value $newpath
    Write-Host "Your computer will need to be restarted before you can use tfvm"
}

$download_start_time = Get-Date
(New-Object System.Net.WebClient).DownloadFile($url, $output_zip)
Write-Output "Time taken: $((Get-Date).Subtract($download_start_time).Seconds) second(s)"

if (Test-Path -Path $output)
{
    $expandedDir = $output_dir + '\tfvm-' + $version
    if (Test-Path -Path $expandedDir){
        Remove-Item -Path $expandedDir -Recurse
    }

    Expand-Archive -LiteralPath $output -DestinationPath $output_dir
    
    if (Test-Path $expandedDir)
    {
	Move-Item -Path $expandedDir + '\dist\tfvm.exe' -Destination $output_dir + 'tfvm.exe'
	Remove--Item -Path $expandedDir -Recurse        
    }
}
