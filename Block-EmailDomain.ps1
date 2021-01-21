write-host "### CONNECT TO EXCHANGE FIRST! ###"
$email = read-host "Enter email domain" 
$id = (Get-HostedContentFilterPolicy | ? {$_.IsDefault -eq $TRUE}).Id
Set-HostedContentFilterPolicy -Identity $id -BlockedSenderDomains @{add="$email"}
Get-HostedContentFilterPolicy -Identity $id | Select -Expand BlockedSenderDomains