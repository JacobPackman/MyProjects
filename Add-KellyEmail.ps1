write-host "### CONNECT TO EXCHANGE FIRST! ###"
$email = read-host "Enter email given by kelly"
$email = $email.ToLower().Replace("mailto:","")
Set-Mailbox Apartments -EmailAddresses @{add="$email"}
(Get-mailbox Apartments | Select -Expand EmailAddresses | Sort).Replace("smtp:","")