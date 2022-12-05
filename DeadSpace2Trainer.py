from src.process import Process     # Process Management class
from src.offsets import DeadSpace2  # DeadSpace2 Offsets class
from src.window import Window       # Window Gui class


if __name__ == '__main__':
    # Create Process Manager
    pDeadspace = Process(DeadSpace2.windowName)

    #Create Window
    window = Window(pDeadspace)
    window.DrawUI()
    window.MainLoop()

    #Release Process
    pDeadspace.CloseProcess()