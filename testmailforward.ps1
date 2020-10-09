    $user = "jacobvdi"
    $fqdn = '@texascontract.net'
    $groupname = $user + "forward"
    $dist = "$user" + "forward" + "$fqdn"
    $forward = 'vdiadmin@texascontract.net',"joshvdi@texascontract.net"
    $cred = get-credential -credential "jacobvdi@texascontract.net"
    Connect-ExchangeOnline -credential $cred;
    New-DistributionGroup -name $groupname -primarysmtpaddress $dist -ManagedBy 'vdiadmin@texascontract.net' -members $forward;
    set-mailbox -Identity $user -ForwardingAddress $dist -DeliverToMailboxAndFOrward $TRUE
    Disconnect-ExchangeOnline -confirm