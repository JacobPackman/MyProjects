$folders = gci -directory
foreach ($fol in $folders) { 
   
    $acl = Get-Acl $fol
    $acl.SetAccessRuleProtection($true,$true)
    Set-Acl -path $fol -AclObject $acl
    
    $acl = Get-Acl $fol
    $rule = $acl.Access | ? {$_.IdentityReference -match ".*txcosc\\[^(s|d)]" -or $_.IdentityReference -Match ".*Domain Users.*"}
    $acl.RemoveAccessRule($rule)
    Set-Acl -path $fol -AclObject $acl

    $name = ($fol.Name)
    $NewAccessRule = New-Object system.security.AccessControl.FileSystemAccessRule("txcosc\$name","Read",,,"Allow")
    $acl.AddAccessRule($NewAccessRule)
    Set-Acl -path $fol -AclObject $acl
}