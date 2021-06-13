from ctypes import *
from ctypes import wintypes
from process import Process


#Global Variables
DEADSPACE2 = 'Dead Space™ 2'
DEADSPACE  = 'Dead Space'

NODE_OFFSET = (0x00B4578C, 0x8, 0x38, 0xD0, 0x594)

#Define a main entry point(Optional)
if __name__ == '__main__':
    pDeadspace = Process(DEADSPACE)
    pDeadspace.PrintProcessInfo()

    node_address = pDeadspace.FindDynamicAddress(NODE_OFFSET)
    print('Node Address: ' + hex(node_address))

    pDeadspace.WriteMemory(node_address, 100)
    node_value = pDeadspace.ReadMemory(node_address)
    print('Node New Value: ' + str(node_value))