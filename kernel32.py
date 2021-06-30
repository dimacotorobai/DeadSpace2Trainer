from ctypes import windll
from ctypes import wintypes

#Import DLL
kernel32 = windll.LoadLibrary('kernel32.dll')

#Read/Write Function Imports
ReadProcessMemory  = kernel32.ReadProcessMemory
WriteProcessMemory = kernel32.WriteProcessMemory

#Virtual Protect, Alloc
VirtualProtectEx = kernel32.VirtualProtectEx
VirtualAllocEx   = kernel32.VirtualAllocEx
VirtualFreeEx    = kernel32.VirtualFreeEx