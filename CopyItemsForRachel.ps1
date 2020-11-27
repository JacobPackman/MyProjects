$folders = gci -recurse | where {$_.Name -match "\w+jpg|\w+gif|\w+tif|\w+jpeg|\w+tiff|\w+bmp|\w+png|\w+raw"}

foreach ($fol in $folders) { 
    $FolderName = ($fol).Directory.Name
<<<<<<< HEAD
    $Backup = "$HOME\Backup\"
    $BackupFolderName = $backup + $FolderName
=======
    $BackupFolderName = "C:\Users\Jacob\Desktop\RachelBackup\" + $FolderName
>>>>>>> 3b400bc... Added powershell scrip to get all images from directory, load into var and recursively copy to a backup folder while preserving direct file structure
    if ( (Test-Path $BackupFolderName) -eq $true)
        {Copy-Item ($fol).FullName -Destination $BackupFolderName}
    else 
        { mkdir $BackupFOlderName; 
          cp ($fol).FullName -Destination $BackupFolderName }
}