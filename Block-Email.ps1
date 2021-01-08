write-host "### CONNECT TO EXCHANGE FIRST! ###"
$email = read-host "Enter email given by end user" 
Set-HostedContentFilterPolicy -Identity Default -BlockedSenders @{add="$email"}
Get-HostedContentFilterPolicy -Identity Default | Select -Expand BlockedSenders