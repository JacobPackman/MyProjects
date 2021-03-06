$folders = gci -directory
foreach ($fol in $folders) { 
   
    $acl = Get-Acl $fol
    $acl.SetAccessRuleProtection($true,$true)
    Set-Acl -path $fol -AclObject $acl
    
    $rules = $acl.Access | ? {$_.IdentityReference -match ".*txcosc\\[^(s|d)]" -or $_.IdentityReference -Match ".*users.*"}
    foreach ($rule in $rules) { 
        $acl.RemoveAccessRule($rule);
	}

    $name = ($fol.Name)
    $NewAccessRule = New-Object system.security.AccessControl.FileSystemAccessRule("txcosc\$name","Modify","ObjectIherit, ContainerInherit","None","Allow")
    $acl.AddAccessRule($NewAccessRule)
    Set-Acl -path $fol -AclObject $acl
}
}
