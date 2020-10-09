#In order to run this script, save it as a .ps1 file on the server and create a task in task scheduler to run once at your desired time
#the action shoudl be start a program, the program/script should be powershell.exe and add arguements
#   -Command "& C:\users\administrator\desktop\script.ps1 -user 'test.user' -password 'Gone#321'" 
#change the C:\...script.ps1 to the location of your script, the 'test.user' to the user of your choice, and the password to whatever password you want to set. 
#Be careful! Apostrophes are dangerous. 
#Once created on the server, you can just keep the task floating in there and modify to run for whoever at your leisure. 

param ( 
	$user = "test",
	$password = "Gone#321"
)
$secure = ConvertTo-SecureSTring -string $password -AsPlainText -Force;
Set-ADUser -identity $user -enabled $FALSE -CannotChangePassword $TRUE -PasswordNeverExpires $TRUE -EmployeeID $NULL -EmployeeNumber $NULL;
Set-ADAccountPassword -Identity $user -Reset -NewPassword $Secure;
Start-AdSyncSyncCycle -PolicyType Delta;