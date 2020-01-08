@ECHO OFF

: Legal workaround?
copy /Y "C:\Program Files (x86)\Vector CANape 14\CANapeAPI\CANapAPI.h" %~dp0
clang-format -style=file CANapAPI.h > CANapAPI2.h
