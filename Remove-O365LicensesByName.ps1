foreach ($name in $names) {
    $user = (Get-MsolUser | ? {$_.DisplayName -like $name})
    $ID = $user.ObjectID
    $licenses = (Get-MsolUser -ObjectID $ID).Licenses.AccountSkuID
    Set-MsolUserLicense -ObjectId $ID -RemoveLicenses $licenses
}