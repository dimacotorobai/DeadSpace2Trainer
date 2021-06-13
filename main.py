from win32 import win32api
from win32 import win32gui
from win32 import win32process
import win32.lib.win32con as win32con
from ctypes import *
from ctypes import wintypes
import psutil


#Global Variables
DEADSPACE2 = 'Dead Space™ 2'
DEADSPACE  = 'Dead Space'

#Define a main entry point(Optional)
if __name__ == '__main__':
    #Find the window
    hWnd = win32gui.FindWindow(None, DEADSPACE)
    if(hWnd == 0):
        print(r'Error - Could Not Find Window "' + DEADSPACE + r'"')
        exit()

    #List Window Attributs
    thread_id, process_id = win32process.GetWindowThreadProcessId(hWnd)

    print('Window Name : ' + win32gui.GetWindowText(hWnd))
    print('Process Name: ' + psutil.Process(process_id).name())
    print('Process ID  : ' + str(process_id))
    print('Thread ID   : ' + str(thread_id))

    #Get a Handle to the process
    hProcess = win32api.OpenProcess(
        win32con.PROCESS_VM_READ|win32con.PROCESS_VM_WRITE|win32con.PROCESS_VM_OPERATION,
        False,
        process_id
    )

    if(hProcess == 0):
        print(r'Error - Could Not Get A Handle to "' + 
            psutil.Process(process_id).name() + 
            r'"')
        win32api.CloseHandle(hProcess)
        exit()

    #Load ReadProcessMemory and WriteProcessMemory
    kernel32 = windll.LoadLibrary('kernel32.dll')
    ReadProcessMemory = kernel32.ReadProcessMemory
    WriteProcessMemory = kernel32.WriteProcessMemory

    #Read Memory
    nodes_address = 0x07945154
    nodes_buffer = c_int32(0)

    ReadProcessMemory(
        int(hProcess),
        nodes_address,
        byref(nodes_buffer),
        4,
        0)

    print("Nodes: " + str(nodes_buffer.value))

    


    #Close Handle
    win32api.CloseHandle(hProcess)