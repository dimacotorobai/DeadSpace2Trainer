from win32 import win32api, win32gui, win32process
import win32.lib.win32con as win32con
import psutil
from ctypes import *
from kernel32 import *

class Process:
    #Constructor Definition
    def __init__(self, window_name: str):
        #Find the window
        self.__hWnd = win32gui.FindWindow(None, window_name)

        #Check if window handle is valid
        if(self.__hWnd == 0):
            print(r'Error - Could Not Find Window "' + window_name + r'"')
            exit()

        #Get threadID and processID
        self.__thread_id, self.__process_id = win32process.GetWindowThreadProcessId(self.__hWnd)

        #Get process handle
        self.__hProcess = win32api.OpenProcess(
            win32con.PROCESS_VM_READ|win32con.PROCESS_VM_WRITE|win32con.PROCESS_VM_OPERATION,
            False,
            self.__process_id
        )

        #Check if process handle is valid
        if(self.__hProcess == 0):
            print(r'Error - Could Not Get A Handle to "' + 
                psutil.Process(self.__process_id).name() + 
                r'"')
            win32api.CloseHandle(self.__hProcess)
            exit()

        #Get module handle/base address
        self.__hModule = win32process.EnumProcessModules(self.__hProcess)[0]
    
    #Destructor Definition
    def CloseProcess(self):
        win32api.CloseHandle(self.__hProcess)

    #Print Process Information    
    def PrintProcessInfo(self) -> None:
        print('Window Name : ' + win32gui.GetWindowText(self.__hWnd))
        print('Process Name: ' + psutil.Process(self.__process_id).name())
        print('Process ID  : ' + str(self.__process_id))

    #Find Dynamic Address
    def FindDynamicAddress(self, offsets: tuple) -> int:
        
        address = c_int32(self.__hModule + offsets[0])
        for offset in offsets[1:]:
            ReadProcessMemory(int(self.__hProcess), address, byref(address), 4, 0)
            address.value += offset

        return address.value

    #Read Memory
    def ReadMemory(self, address: int) -> int:
        value_buffer = c_int32(0)
        ReadProcessMemory(int(self.__hProcess), address, byref(value_buffer), 4, 0)
        return value_buffer.value

    #Write Memory
    def WriteMemory(self, address: int, value: int) -> None:
        value_buffer = c_int32(value)
        WriteProcessMemory(int(self.__hProcess), address, byref(value_buffer), 4, 0)
        return None



