import psutil
import win32.lib.win32con as win32con
from win32 import win32api, win32gui, win32process
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

    #Get Base Address of Module
    def GetBaseAddress(self) -> int:
        return int(self.__hModule)

    #Print Process Information    
    def GetProcessInfo(self) -> tuple:
        return (win32gui.GetWindowText(self.__hWnd), psutil.Process(self.__process_id).name(), str(self.__process_id), str(self.__thread_id))

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
    
    #Patch Memory Externaly
    def PatchMemory(self, src: tuple, dst: int, size: int):
        oldProtect = c_uint32(0)
        arr = (c_ubyte *len(src))(*src)
        VirtualProtectEx(int(self.__hProcess), dst, size, win32con.PAGE_EXECUTE_READWRITE, byref(oldProtect))
        WriteProcessMemory(int(self.__hProcess), dst, arr, size, 0)
        VirtualProtectEx(int(self.__hProcess), dst, size, oldProtect, byref(oldProtect))

    #Allocate Memory within Process
    def AllocMemory(self, address: int, size: int) -> int:
        addr = VirtualAllocEx(int(self.__hProcess), address, size, win32con.MEM_COMMIT, win32con.PAGE_EXECUTE_READWRITE)
        #print('VirtualAllocEx: ' + hex(addr))
        return addr

    #Free Allocated Memory
    def FreeMemory(self, address:int, size: int) -> int:
        bResult = VirtualFreeEx(int(self.__hProcess), address, size, win32con.MEM_DECOMMIT)
        return bResult
