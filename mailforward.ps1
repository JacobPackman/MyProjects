param (
    $site = '@texascontract.net', 
    $user = "cristobal",
    $forward = @("mirna.aguilar$site","brandi.stout$site","heather$site"),
    $ManageRights = "michael.sherman$site"
)

$groupname = $user + "forward"
$dist = "$user" + "forward" + "$site"
$cred = get-credential -credential "jacobvdi$site"

Connect-ExchangeOnline -credential $cred;
New-DistributionGroup -name $groupname -primarysmtpaddress $dist -ManagedBy "vdiadmin$site" -members $forward;
set-mailbox -identity $user -ForwardingAddress $dist -DeliverToMailboxAndForward $true;
add-mailboxpermission -identity $user -user $ManageRights -AccessRights FullAccess;
Disconnect-ExchangeOnline -confirm
