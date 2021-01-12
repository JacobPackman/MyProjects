$names = @"
Ex1
Ex2
Ex3
"@ -split '\n'

$emails = @(); 
foreach ( $name in $names) { 
    $emails += (get-mailbox | ? {$_.DisplayName -like "*$($name)*"}).PrimarySmtpAddress 
}

foreach ($email in $emails) { 
    Add-DistributionGroupMember example@contoso.com -Member $email 
    }