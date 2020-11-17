write-host "### CONNECT TO EXCHANGE FIRST! ###"
$email = read-host "Enter email given by kelly" 
Set-Mailbox Apartments -EmailAddresses @{add="$email"}
(Get-mailbox Apartments | Select -Expand EmailAddresses | Sort).Replace("smtp:","")