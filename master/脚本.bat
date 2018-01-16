@echo off

set dir_s=%cd%

cd /d D:\
md SecurityDaily_Internet

cd /d %dir_s%
xcopy /E /-Y %dir_s%\* D:\SecurityDaily_Internet\
pause