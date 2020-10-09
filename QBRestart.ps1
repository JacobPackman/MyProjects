$Trigger = New-JobTrigger -Weekly -DaysOfWeek Tuesday, Thursday, Sunday -At "02:30"
$option = New-ScheduledJobOption -RunElevated -WakeToRun

Register-ScheduledJob -Name "QB Restart" -Trigger $trigger -Option $option -ScriptBlock {
    Start-Process "C:\Program Files (x86)\Intuit\Quickbooks 2019\QBW32.EXE" ; 
    Stop-Process -Name "QBW32" -force
}
