# -*- coding:utf-8 -*-
from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        pass
    def load(self, path_to_exe):
        creation_flags = DEBUG_PROCESS
        startupInfo = STARTUPINFO()
        process_Information = PROCESS_INFORMATIUON()
        startupInfo.dwFlags = 0x1
        startupInfo.wShowWindow = 0x0
        startupInfo.cb = sizeof(startupInfo)
        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(startupInfo),
                                   byref(process_Information)):
            print "[*] We have successfully launched the process!"
            print "[*] PID:%d"%process_Information.dwProcessID
        else:
            print "[*] Error:0x%08x."%kernel32.GetLastError()