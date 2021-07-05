from process import Process             #Process info
from win32 import win32api              #Get Keys presses
import win32.lib.win32con as win32con   #Win macros
import time                             #Import for sleep thread
from offsets import DeadSpace, DeadSpace2
from window import Window

#Global Variables
bGodmodeOn  = False
bAmmoOn     = False
bStasisOn   = False
bAirOn      = False

#Memory Alloc On
dwGodmodeAddr = 0

#Godmode hex
godmode_array = [0x50, 0x53, 0xB8, 0x99, 0x99, 0x99, 0x99,
                 0x8B, 0x80, 0x54, 0xD5, 0xC4, 0x01, 0x8B,
                 0x40, 0x18, 0x8B, 0x40, 0x2C, 0x8B, 0x40,
                 0x0C, 0x05, 0xE8, 0x00, 0x00, 0x00, 0x89,
                 0xFB, 0x81, 0xC3, 0xE8, 0x00, 0x00, 0x00,
                 0x39, 0xD8, 0x74, 0x08, 0xF3, 0x0F, 0x11,
                 0x87, 0xE8, 0x00, 0x00, 0x00, 0x5B, 0x58,
                 0x68, 0x99, 0x99, 0x99, 0x99, 0xC3]

#Define a main entry point(Optional)
if __name__ == '__main__':

    #Fine Process and Print Info
    pDeadspace = Process(DeadSpace2.windowName)
    pDeadspace.PrintProcessInfo()

    #Create Window
    window = Window(pDeadspace)
    window.DrawUI()
    window.MainLoop()

    #Release Process
    pDeadspace.CloseProcess()

    exit(code=0)

    #Dont Below is the code for the Console Version of the Hack 

    #Print Menu
    print('\nDead Space 2 Trainer\n')
    print('[F1] for Godmode')
    print('[F2] for Infinite Ammo')
    print('[F3] for Infinite Stasis')
    print('[F4] for Infinite Air')
    print('[F5] for 500 Credits')
    print('[F6] for 1 Node')
    print('[F7] to exit trainer')

    while True:
        #Godmode
        if win32api.GetAsyncKeyState(win32con.VK_F1):
            print("Pressed [F1]")
            base_address = pDeadspace.GetBaseAddress()
            godmode_array[3:7] = list(base_address.to_bytes(4, 'little'))
            godmode_array[50:54] = list((base_address + DeadSpace2.godmode_offset + DeadSpace2.godmode_size).to_bytes(4, 'little'))
            bGodmodeOn = not(bGodmodeOn)
            if bGodmodeOn:
                #Allocate Memory
                dwGodmodeAddr = pDeadspace.AllocMemory(0, len(godmode_array))
                pDeadspace.PatchMemory(godmode_array, dwGodmodeAddr, len(godmode_array))

                #Calculate Relative
                relative_address = dwGodmodeAddr - (base_address + DeadSpace2.godmode_offset + 5)
                jmp_shellcode = tuple(b'\xE9' + relative_address.to_bytes(4, 'little'))

                #Patch Current Mem
                pDeadspace.PatchMemory(DeadSpace2.godmode_on, base_address + DeadSpace2.godmode_offset, DeadSpace2.godmode_size)
                pDeadspace.PatchMemory(jmp_shellcode, base_address + DeadSpace2.godmode_offset, len(jmp_shellcode))
            else:
                #Unpatch jmp instruction
                pDeadspace.PatchMemory(DeadSpace2.godmode_off, base_address + DeadSpace2.godmode_offset, DeadSpace2.godmode_size)

                #Deallocate Memory
                pDeadspace.FreeMemory(dwGodmodeAddr, len(godmode_array))

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
        
        #Put Thread to Sleep
        time.sleep(0.25)

    #Close Process Handle    
    pDeadspace.CloseProcess()
