write-host "### CONNECT TO EXCHANGE FIRST! ###"
$email = read-host "Enter email given by end user" 
$id = (Get-HostedContentFilterPolicy | ? {$_.IsDefault -eq $TRUE}).Id
Set-HostedContentFilterPolicy -Identity $id -BlockedSenders @{add="$email"}
Get-HostedContentFilterPolicy -Identity $id | Select -Expand BlockedSenders