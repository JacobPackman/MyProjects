$User = Read-Host "Enter UPN of user"
$DLs = Get-DistributionGroup

foreach ($dl in $dls) { 
        if ($NULL -ne (Get-DistributionGroupMember -Identity ($dl).SamAccountName | ? {$_.PrimarySmtpAddress -like "*$user*"}))
        {
            write-output $dl
        }
}
