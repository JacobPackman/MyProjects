
$folders = gci -recurse | where {$_.Name -match "\w+jpg|\w+gif|\w+tif|\w+jpeg|\w+tiff|\w+bmp|\w+png|\w+raw"}

foreach ($fol in $folders) { 
    $FolderName = ($fol).Directory.Name
    $Backup = "$HOME\Backup"
    $BackupFolderName = "$Backup" + $FolderName
    if ( (Test-Path $BackupFolderName) -eq $true)
        {Copy-Item ($fol).FullName -Destination $BackupFolderName}
    else 
        { mkdir $BackupFOlderName; 
          cp ($fol).FullName -Destination $BackupFolderName }
} 