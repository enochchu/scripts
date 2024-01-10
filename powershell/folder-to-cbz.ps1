$folderlist = Get-ChildItem "."

foreach ($File in $folderlist) {
    Compress-Archive -path $File.Name -destinationPath "$($File.Name).zip"
    Rename-Item -Path "$($File.Name).zip" "$($File.Name).cbz"
}