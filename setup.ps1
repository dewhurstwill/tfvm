#################################
#                               #
#        Install Script         #
#            (BETA)             #
#################################

# Constants
$version = "0.0.9"
$url = 'https://codeload.github.com/dewhurstwill/tfvm/zip/v' + $version
$output_zip = "C:\$env:HOMEPATH\" + $zip_name
$output_dir = "C:\$env:HOMEPATH\.tfvm"

python -V
pip -V

if (!(Test-Path -Path C:\$env:HOMEPATH\.tfvm))
{
    New-Item "C:\$env:HOMEPATH\.tfvm" -itemtype directory
    if (!(Test-Path -Path C:\$env:HOMEPATH\.tfvm\logs))
    {
        New-Item "C:\$env:HOMEPATH\.tfvm\logs" -itemtype directory
    }
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
        if (Test-Path -Path "$output_dir\app")
        {
            Remove-Item -Path "$output_dir\app" -Recurse
        }
        Rename-Item $expandedDir "$output_dir\app"
        if (Test-Path -Path "$output_dir\app")
        {
            pip install -r "C:\$ENV:HOMEPATH\.tfvm\app\requirements.txt"

            $aliasValue = 'python.exe "C:' + $ENV:HOMEPATH + '\.tfvm\app\main.py"'
            Set-Alias -Name "tfvm" -Value "$aliasValue"
        }
    }
}
