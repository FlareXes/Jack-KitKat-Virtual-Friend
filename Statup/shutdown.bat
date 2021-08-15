@echo off
shutdown /s /f /t 60 /c " "
cls

set /p pass=Enter Your Password :
if %pass%==time_pass goto yes
if not %pass%==time_pass goto no

:no
cls
color 0a
echo Your Password Was Incorrect
echo -- One More Try --
if %pass%==time_pass goto yes
if not %pass%==time_pass goto bye
exit

:bye
cls
shutdown /p

:yes
shutdown /a
exit