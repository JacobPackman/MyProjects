$Sacl = Get-Acl ssandys
$Srule = $Sacl.Access | ? {$_.IdentityReference -like "*ssandys*"} | Select -Expand IdentityReference
foreach ($fol in $folders) { 
    $acl = Get-Acl $fol
    $rules = $acl.Access
    foreach ($rule in $rules) {
        $owner = $rule | Select -Expand IdentityReference
        if ($owner -eq $Srule) {
            ($fol).Name
        }
    }
}





