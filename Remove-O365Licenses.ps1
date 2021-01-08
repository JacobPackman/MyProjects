foreach ($user in $users) {
    $ID = (Get-MsolUser $user).ObjectID
    $licenses = (Get-MsolUser -ObjectID $ID).Licenses.AccountSkuID
    Set-MsolUserLicense -ObjectId $ID -RemoveLicenses $licenses
}