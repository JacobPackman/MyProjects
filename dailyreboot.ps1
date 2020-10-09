$Trigger = New-JobTrigger -Daily -At (Get-Date).AddSeconds(15)
Register-ScheduledJob -Name "LogMeIn Reboot" -Trigger $trigger -Scriptblock { 
    Restart-Computer
}