from process import Process     # Process Management class
from offsets import DeadSpace2  # DeadSpace2 Offsets class
from window import Window       # Window Gui class


def main() -> None:
    # Create Process Manager
    pDeadspace = Process(DeadSpace2.windowName)

    #Create Window
    window = Window(pDeadspace)
    window.DrawUI()
    window.MainLoop()

    #Release Process
    pDeadspace.CloseProcess()

if __name__ == '__main__':
    main()
