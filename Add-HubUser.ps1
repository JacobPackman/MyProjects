write-host "Good job forgetting this one again moron."
write-host "### CONNECT TO EXCHANGE FIRST! ###"
$user = read-host "Enter User Principal Name/email" 
Add-MailboxPermission -AccessRights FullAccess -Identity "tcchub@texascontract.net" -User $user