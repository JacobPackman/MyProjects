$user = read-host "Enter username" 
Set-ADAccountPassword -Identity $user -Reset -NewPassword (ConvertTo-SecureString -AsPlainText "#ChangeMe" -Force); Set-ADUser -Identity $user -ChangePasswordAtLogon $true