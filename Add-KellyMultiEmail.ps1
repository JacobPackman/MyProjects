Write-Host '#### Please write emails to $emails variable'
$emails | % {Set-Mailbox Apartments -EmailAddresses @{add="$_"}}