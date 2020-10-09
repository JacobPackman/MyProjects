param (
    $user = "lparra"
)
$secure = Read-Host "Please enter PW" -AsSecureString
Set-ADAccountPassword -Identity $user -NewPassword $secure -Reset
Set-AdUser -Identity $user -ChangePasswordAtLogon $TRUE
Start-AdSyncSyncCycle -PolicyType Delta