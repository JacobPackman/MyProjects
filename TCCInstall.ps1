$user= Read-Host "Please enter User: "
$OldPC = Read-Host "Please enter reference PC: "
$secure = Read-Host "Enter VDIAdmin Password: " -AsSecureString
$install = "C:\Install"
$pri="Operations","Accounting","Executive Office","Warehouse","ProjectMgmt"
$testpath = "C:\Users\JacobPackman\OneDrive - VDI Communications, Inc\Desktop\Install Script"
$path= Get-ChildItem $testpath -Recurse
$department = "ACTD","SRPM","EXC","OPR","EST"


Invoke-Command -ComputerName $old -Scriptblock { New-SmbShare -Name Robocopy -Path "C:\Users\$($user)" -FullAccess $user } 
mkdir $install
Invoke-WebRequest https://download.parallels.com/ras/v17/17.1.1.21792/RASClient-x64-17.1.21792.msi -OutFile $in\rdp.msi
Invoke-WebRequest http://sudwld.itsupport247.net/AgentSetupdwld/setups/AgentSetupsOD/TCC713_118953_DPMA_SILENT_549.msi -outfile $in\rmm.msi
Copy-Item -path \\10.100.162.25\setup\tcc\2XSettings.2xc -dest $in\2XSettings.2xc -credential jacob.packman@vdi-inc.com

Set-Location $in
$path.fullname | ForEach-Object {(Get-Content $_ -Raw).Replace("bartsimpson","$($user -replace '[.]')")| Set-Content $_}
msiexec /i rdp.msi DEFSETTINGS="2XSettings.2xc" /qn
msiexec /i rmm.msi /qn

Add-Printer -ConnectionName \\tcc-fs01\$($pri[1])
New-LocalUser -Name vdiadmin -password $secure -PasswordNeverExpires 
Add-LocalGroupMember -Group Administrators -Member vdiadmin 
Rename-Computer -NewName "TCC-$($department[0])05"

robocopy "\\$($oldpc)\$($user)" "$home" /e /copy:datsou /r:0 /tee