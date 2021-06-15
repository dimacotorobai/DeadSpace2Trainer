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

        if win32api.GetAsyncKeyState(win32con.VK_F3):
            print("Pressed [F3]")
            base_address = pDeadspace.GetBaseAddress()
            bStasisOn = not(bStasisOn)
            if bStasisOn:
                pDeadspace.PatchMemory(DeadSpace2.stasis_on, base_address + DeadSpace2.stasis_offset, DeadSpace2.stasis_size)
            else:
                pDeadspace.PatchMemory(DeadSpace2.stasis_off, base_address + DeadSpace2.stasis_offset, DeadSpace2.stasis_size)

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
