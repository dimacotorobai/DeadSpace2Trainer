from process import Process             #Process info
from win32 import win32api              #Get Keys presses
import win32.lib.win32con as win32con   #Win macros
import time                             #Import for sleep thread
from offsets import DeadSpace, DeadSpace2

#Global Variables
bGodmodeOn  = False
bAmmoOn     = False
bStasisOn   = False
bAirOn      = False

#Memory Alloc On
bMemAlloc   = False

#Godmode hex
godmode_array = (0x50, 0x53, 0xB8, 0x00,
                 0x00, 0x40, 0x00, 0x05,
                 0x54, 0xD5, 0xC4, 0x01,
                 0x8B, 0x00, 0x83, 0xC0,
                 0x18, 0x8B, 0x00, 0x83,
                 0xC0, 0x2C, 0x8B, 0x00,
                 0x83, 0xC0, 0x0C, 0x8B,
                 0x00, 0x05, 0xE8, 0x00,
                 0x00, 0x00, 0x89, 0xFB,
                 0x81, 0xC3, 0xE8, 0x00,
                 0x00, 0x00, 0x39, 0xD8,
                 0x74, 0x0A, 0xF3, 0x0F,
                 0x11, 0x87, 0xE8, 0x00,
                 0x00, 0x00, 0xEB, 0x00,
                 0x5B, 0x58, 0x68, 0x64,
                 0x4D, 0xF8, 0x00, 0xC3)

#Define a main entry point(Optional)
if __name__ == '__main__':

    #Fine Process and Print Info
    pDeadspace = Process(DeadSpace2.windowName)
    pDeadspace.PrintProcessInfo()

    #Print Menu
    print('\nDead Space 2 Trainer\n')
    print('[F1] for Godmode')
    print('[F2] for Infinite Ammo')
    print('[F3] for Infinite Stasis')
    print('[F4] for Infinite Air')
    print('[F5] for 500 Credits')
    print('[F6] for 1 Node')
    print('[F7] to exit trainer')
    print('[F8] for Godmode Testing')

    while True:
        #Godmode
        if win32api.GetAsyncKeyState(win32con.VK_F1):
            print("Pressed [F1]")
            base_address = pDeadspace.GetBaseAddress()
            bGodmodeOn = not(bGodmodeOn)
            if bGodmodeOn:
                pDeadspace.PatchMemory(DeadSpace2.godmode_on, base_address + DeadSpace2.godmode_offset, DeadSpace2.godmode_size)
            else:
                pDeadspace.PatchMemory(DeadSpace2.godmode_off, base_address + DeadSpace2.godmode_offset, DeadSpace2.godmode_size)

        #Ammo On
        if win32api.GetAsyncKeyState(win32con.VK_F2):
            print("Pressed [F2]")
            base_address = pDeadspace.GetBaseAddress()
            bAmmoOn = not(bAmmoOn)
            if bAmmoOn:
                pDeadspace.PatchMemory(DeadSpace2.ammo_on, base_address + DeadSpace2.ammo_offset, DeadSpace2.ammo_size)
            else:
                pDeadspace.PatchMemory(DeadSpace2.ammo_off, base_address + DeadSpace2.ammo_offset, DeadSpace2.ammo_size)

        #Stasis On
        if win32api.GetAsyncKeyState(win32con.VK_F3):
            print("Pressed [F3]")
            base_address = pDeadspace.GetBaseAddress()
            bStasisOn = not(bStasisOn)
            if bStasisOn:
                pDeadspace.PatchMemory(DeadSpace2.stasis_on, base_address + DeadSpace2.stasis_offset, DeadSpace2.stasis_size)
            else:
                pDeadspace.PatchMemory(DeadSpace2.stasis_off, base_address + DeadSpace2.stasis_offset, DeadSpace2.stasis_size)

        #Air On
        if win32api.GetAsyncKeyState(win32con.VK_F4):
            print("Pressed [F4]")
            base_address = pDeadspace.GetBaseAddress()
            bAirOn = not(bAirOn)
            if bAirOn:
                pDeadspace.PatchMemory(DeadSpace2.air_on, base_address + DeadSpace2.air_offset, DeadSpace2.air_size)
            else:
                pDeadspace.PatchMemory(DeadSpace2.air_off, base_address + DeadSpace2.air_offset, DeadSpace2.air_size)

        #Give Credits
        if win32api.GetAsyncKeyState(win32con.VK_F5):
            print("Pressed [F5]")
            credit_addr = pDeadspace.FindDynamicAddress(DeadSpace2.credit_offsets)
            credit_value = pDeadspace.ReadMemory(credit_addr)
            pDeadspace.WriteMemory(credit_addr, credit_value + 500)

        #Give Nodes
        if win32api.GetAsyncKeyState(win32con.VK_F6):
            print("Pressed [F6]")
            node_addr = pDeadspace.FindDynamicAddress(DeadSpace2.node_offsets)
            node_value = pDeadspace.ReadMemory(node_addr)
            pDeadspace.WriteMemory(node_addr, node_value + 1)

        #Close Trainer
        if win32api.GetAsyncKeyState(win32con.VK_F7):
            print("Pressed [F7]")
            break

        if win32api.GetAsyncKeyState(win32con.VK_F8):
            print("Pressed F8")
            base_address = pDeadspace.GetBaseAddress()
            if bMemAlloc == False:
                address = pDeadspace.AllocMemory(0, len(godmode_array))
                pDeadspace.PatchMemory(godmode_array, address, len(godmode_array))

                offset = address - (base_address + DeadSpace2.godmode_offset + 5)

                bytes = offset.to_bytes(4, byteorder='little')
                bytes = b'\xE9' + bytes
                bytes = tuple(bytes)

                pDeadspace.PatchMemory(DeadSpace2.godmode_on, base_address + DeadSpace2.godmode_offset, DeadSpace2.godmode_size)
                pDeadspace.PatchMemory(bytes, base_address+DeadSpace2.godmode_offset, len(bytes))

                print(bytes)

                bMemAlloc = True
        
        #Put Thread to Sleep
        time.sleep(0.25)

    #Close Process Handle    
    pDeadspace.CloseProcess()
