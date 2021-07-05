from tkinter import *
from process import Process
from offsets import *
from shellcode import *

class Window:
    def __init__(self, pDeadSpace: Process):
        #Create Window
        self.window = Tk()
        self.window.title('Dead Space™ 2 Hack v1.0')
        self.window.geometry('400x500')
        self.window.configure(bg='#d3d3d3')
        self.window.minsize(400, 500)
        self.window.maxsize(400, 500)
        self.window.grid_propagate(0)
        self.window.protocol('WM_DELETE_WINDOW', self.__quit__)

        #Create Variables
        self.var_godmode = IntVar()
        self.var_ammo = IntVar()
        self.var_stasis = IntVar()
        self.var_air = IntVar()

        self.var_credits = IntVar()
        self.var_nodes = IntVar()

        self.text_credits = StringVar()
        self.text_nodes = StringVar()

        #Game Variables
        self.pDeadSpace = pDeadSpace
        self.godmode_alloc = 0

    #Define A Exit Custom Window Function
    def __quit__(self):
        self.var_godmode.set(0)
        self.var_ammo.set(0)
        self.var_stasis.set(0)
        self.var_air.set(0)
        self.var_nodes.set(0)
        self.var_credits.set(0)

        self.Godmode_Check()
        self.Ammo_Check()
        self.Stasis_Check()
        self.Air_Check()
        self.Nodes_Check()
        self.Credits_Check()

        self.window.destroy()
        pass


    def DrawUI(self):
        #Info Frame
        self.proc_info_frame = LabelFrame(self.window, text='Process Information', width = 380, height = 150, padx=10, pady = 10)
        self.proc_info_frame.configure(bg='#d3d3d3', font = ("TkDefaultFont", 10))
        self.proc_info_frame.grid(columnspan=2, padx=10, pady = 10)
        self.proc_info_frame.grid_propagate(0)

        Label(self.proc_info_frame, text='                                      ', bg = '#d3d3d3', height=0).grid(row = 4, column = 0)
        Label(self.proc_info_frame, text='                                      ', bg = '#d3d3d3', height=0).grid(row = 4, column = 1)
        Label(self.proc_info_frame, text='                                      ', bg = '#d3d3d3', height=0).grid(row = 4, column = 2)

        proc_info = self.pDeadSpace.PrintProcessInfo() #Process Info

        self.window_name = Label(self.proc_info_frame, text='Window Name: ' + proc_info[0], bg='#d3d3d3')
        self.window_name.grid(row = 0, column = 0, sticky = "W")

        self.process_name = Label(self.proc_info_frame, text='Process Name: '+ proc_info[1], bg='#d3d3d3')
        self.process_name.grid(row = 1, column = 0, sticky = "W")

        self.process_id = Label(self.proc_info_frame, text='Process ID: '+ proc_info[2], bg='#d3d3d3')
        self.process_id.grid(row = 2, column = 0, sticky = "W")

        self.thread_id = Label(self.proc_info_frame, text='Thread ID: '+ proc_info[3], bg='#d3d3d3')
        self.thread_id.grid(row = 3, column = 0, sticky = "W")


        #Cheat Frame
        self.cheat_frame = LabelFrame(self.window, text='Cheat', padx=-10, pady=1, width = 190, height = 300)
        self.cheat_frame.configure(bg='#d3d3d3', font = ("TkDefaultFont", 10))
        self.cheat_frame.grid(row = 2, column = 0)
        self.cheat_frame.grid_propagate(0)

        Label(self.cheat_frame, text='             ', bg = '#d3d3d3').grid(row = 0, column = 0)
        Label(self.cheat_frame, text='                ', bg = '#d3d3d3').grid(row = 0, column = 1)
        Label(self.cheat_frame, text='          ', bg = '#d3d3d3').grid(row = 0, column = 2)

        self.godmode_cb = Checkbutton(self.cheat_frame, text='Godmode      ', bg='#d3d3d3', height = 2, variable = self.var_godmode, command = self.Godmode_Check, onvalue = 1, offvalue = 0)
        self.godmode_cb.grid(row = 1, column = 1, sticky = "W")

        self.infammo_cb = Checkbutton(self.cheat_frame, text='Infinite Ammo', bg='#d3d3d3', height = 2, variable = self.var_ammo, command = self.Ammo_Check, onvalue = 1, offvalue = 0)
        self.infammo_cb.grid(row = 2, column = 1, sticky = "W")

        self.infstasis_cb = Checkbutton(self.cheat_frame, text='Infinite Stasis', bg='#d3d3d3', height = 2, variable = self.var_stasis, command = self.Stasis_Check, onvalue = 1, offvalue = 0)
        self.infstasis_cb.grid(row = 3, column = 1, sticky = "W")

        self.infair_cb = Checkbutton(self.cheat_frame, text='Infinite Air', bg='#d3d3d3', height = 2, variable = self.var_air, command = self.Air_Check, onvalue = 1, offvalue = 0)
        self.infair_cb.grid(row = 4, column = 1, sticky = "W")


        #Misc Frame
        self.misc_frame = LabelFrame(self.window, text='Misc', padx=1, pady=1,width = 190, height = 300)
        self.misc_frame.configure(bg='#d3d3d3', font = ("TkDefaultFont", 10))
        self.misc_frame.grid(row = 2, column = 1)
        self.misc_frame.grid_propagate(0)

        Label(self.misc_frame, text='             ', bg = '#d3d3d3').grid(row = 0, column = 0)
        Label(self.misc_frame, text='             ', bg = '#d3d3d3').grid(row = 0, column = 1)
        Label(self.misc_frame, text='        ', bg = '#d3d3d3').grid(row = 0, column = 2)

        Label(self.misc_frame, text='Nodes ', bg = '#d3d3d3').grid(row = 1, column = 0)
        self.tb_nodes = Entry(self.misc_frame, width = 17, textvariable = self.text_nodes, justify = 'right')
        self.tb_nodes.grid(row = 1, column = 1)
        self.cb_nodes = Checkbutton(self.misc_frame, text='', bg='#d3d3d3', variable = self.var_nodes, command = self.Nodes_Check, onvalue = 1, offvalue = 0)
        self.cb_nodes.grid(row = 1, column = 2)

        self.b_nodes_get = Button(self.misc_frame, text='GET', bg='#d3d3d3', width=13, command = self.GetNodes)
        self.b_nodes_get.grid(row = 2, column= 1, sticky='W', columnspan = 3)
        self.b_nodes_set = Button(self.misc_frame, text='SET', bg = '#d3d3d3', command = self.SetNodes)
        self.b_nodes_set.grid(row = 2, column = 2, columnspan = 3, sticky='W')

        Label(self.misc_frame, text='', bg='#d3d3d3').grid(row = 3, column = 0)

        Label(self.misc_frame, text='Credits ', bg = '#d3d3d3').grid(row = 4, column = 0)
        self.tb_credits = Entry(self.misc_frame, width = 17, textvariable = self.text_credits, justify = 'right')
        self.tb_credits.grid(row = 4, column = 1)
        self.cb_credits = Checkbutton(self.misc_frame, text='', bg='#d3d3d3', variable = self.var_credits, command = self.Credits_Check, onvalue = 1, offvalue = 0)
        self.cb_credits.grid(row = 4, column = 2)

        self.b_credits_get = Button(self.misc_frame, text='GET', bg='#d3d3d3', width = 13, command = self.GetCredits)
        self.b_credits_get.grid(row = 5, column= 1, sticky='W')
        self.b_credits_set = Button(self.misc_frame, text='SET', bg = '#d3d3d3', command = self.SetCredits)
        self.b_credits_set.grid(row = 5, column = 2, sticky='W')
    
    #Wrapper for main loop method
    def MainLoop(self):
        self.window.mainloop()

    #Button Command Functions
    def Godmode_Check(self):
        base_address = self.pDeadSpace.GetBaseAddress()
        godmode_array[3:7] = list(base_address.to_bytes(4, 'little'))
        godmode_array[50:54] = list((base_address + DeadSpace2.godmode_offset + DeadSpace2.godmode_size).to_bytes(4, 'little'))

        if(self.var_godmode.get() == 1):
            #Allocate Memory
            self.godmode_alloc = self.pDeadSpace.AllocMemory(0, len(godmode_array))
            self.pDeadSpace.PatchMemory(godmode_array, self.godmode_alloc, len(godmode_array))

            #Calculate Relative
            relative_address = self.godmode_alloc - (base_address + DeadSpace2.godmode_offset + 5)
            jmp_shellcode = tuple(b'\xE9' + relative_address.to_bytes(4, 'little'))

            #Patch Current Mem
            self.pDeadSpace.PatchMemory(DeadSpace2.godmode_on, base_address + DeadSpace2.godmode_offset, DeadSpace2.godmode_size)
            self.pDeadSpace.PatchMemory(jmp_shellcode, base_address + DeadSpace2.godmode_offset, len(jmp_shellcode))
        else:
            #Unpatch jmp instruction
            self.pDeadSpace.PatchMemory(DeadSpace2.godmode_off, base_address + DeadSpace2.godmode_offset, DeadSpace2.godmode_size)

            #Deallocate Memory
            self.pDeadSpace.FreeMemory(self.godmode_alloc, len(godmode_array))


    def Ammo_Check(self):
        base_address = self.pDeadSpace.GetBaseAddress()
        if(self.var_ammo.get() == 1):
            self.pDeadSpace.PatchMemory(DeadSpace2.ammo_on, base_address + DeadSpace2.ammo_offset, DeadSpace2.ammo_size)
        else:
            self.pDeadSpace.PatchMemory(DeadSpace2.ammo_off, base_address + DeadSpace2.ammo_offset, DeadSpace2.ammo_size)

    def Stasis_Check(self):
        base_address = self.pDeadSpace.GetBaseAddress()
        if(self.var_stasis.get() == 1):
            self.pDeadSpace.PatchMemory(DeadSpace2.stasis_on, base_address + DeadSpace2.stasis_offset, DeadSpace2.stasis_size)
        else:
            self.pDeadSpace.PatchMemory(DeadSpace2.stasis_off, base_address + DeadSpace2.stasis_offset, DeadSpace2.stasis_size)

    def Air_Check(self):
        base_address = self.pDeadSpace.GetBaseAddress()
        if(self.var_air.get() == 1):
            self.pDeadSpace.PatchMemory(DeadSpace2.air_on, base_address + DeadSpace2.air_offset, DeadSpace2.air_size)
        else:
            self.pDeadSpace.PatchMemory(DeadSpace2.air_off, base_address + DeadSpace2.air_offset, DeadSpace2.air_size)

    #Constant Write to Nodes and Credits
    def Nodes_Check(self):
        if(self.var_nodes.get() == 1):
            self.window.title('Nodes Checked')

            nodes_addr = self.pDeadSpace.FindDynamicAddress(DeadSpace2.node_offsets)
            nodes_value = int(self.tb_nodes.get())
            self.pDeadSpace.WriteMemory(nodes_addr, nodes_value)

            self.window.after(1000, self.Nodes_Check)
        else:
            self.window.title('Nodes Unchecked')


    def Credits_Check(self):
        if(self.var_credits.get() == 1):
            self.window.title('Credits Checked')

            credit_addr = self.pDeadSpace.FindDynamicAddress(DeadSpace2.credit_offsets)
            credit_value = int(self.tb_credits.get())
            self.pDeadSpace.WriteMemory(credit_addr, credit_value)

            self.window.after(1000, self.Credits_Check)
        else:
            self.window.title('Credits Unchecked')

    #Get/Set Nodes and Credits
    def GetNodes(self):
        nodes_addr = self.pDeadSpace.FindDynamicAddress(DeadSpace2.node_offsets)
        nodes_value = self.pDeadSpace.ReadMemory(nodes_addr)
        self.text_nodes.set(str(nodes_value))

    def SetNodes(self):
        nodes_addr = self.pDeadSpace.FindDynamicAddress(DeadSpace2.node_offsets)
        nodes_value = int(self.tb_nodes.get())
        self.pDeadSpace.WriteMemory(nodes_addr, nodes_value)

    def GetCredits(self):
        credit_addr = self.pDeadSpace.FindDynamicAddress(DeadSpace2.credit_offsets)
        credit_value = self.pDeadSpace.ReadMemory(credit_addr)
        self.text_credits.set(str(credit_value))

    def SetCredits(self):
        credit_addr = self.pDeadSpace.FindDynamicAddress(DeadSpace2.credit_offsets)
        credit_value = int(self.tb_credits.get())
        self.pDeadSpace.WriteMemory(credit_addr, credit_value)

        