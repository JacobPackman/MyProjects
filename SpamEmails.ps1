$policy = "Default"
$sender = "saptarshi.paul@cognizant.com"
$user = "jkvalsten@yarishmd.com"
Connect-ExchangeOnline
Get-InboxRule -Mailbox $user
Set-HostedContentFilterPolicy -Identity "$policy" -BlockedSenders @{add="$sender"}
Get-HostedContentFilterPolicy -Identity "$policy" | Select -ExpandProperty BlockedSenders