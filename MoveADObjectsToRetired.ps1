foreach ($hostname in $computerlist) {
    $identity = Get-adcomputer ($hostname).replace(".ALTUSACE.COM","") | Select -Expand DistinguishedName
    $target = Get-ADOrganizationalUnit -filter * | ? {$_.DistinguishedName -match ".*Retired.*"} | Select -expand DistinguishedName
    Move-ADObject –Identity $identity -TargetPath $target 

}
