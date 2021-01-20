$extensions = (gci -file | Sort Extension | Select -Expand Extension )  | Get-Unique
foreach ($ext in $extensions) { 
    $FolderName = ($ext).Replace(".","")
    $Files = (gci *$($ext))
    if ( (test-Path $FolderName) -eq $True) {
        Move-Item -Destination $FolderName
    }
    else {
        mkdir $FolderName; $files | Move-Item -Destination 
    }
}