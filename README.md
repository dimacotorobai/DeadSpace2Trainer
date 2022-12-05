## DeadSpace2 Trainer
This is a trainer for the game Dead Space 2. This trainer was created in Python with the help of the PyWin32 library. This trainer contains Godmode, Infinite Ammo, Infinite Stasis, and Infinite Air, as well as Get and Set Nodes and Credits. This is an external hack that uses code injection, code caves, and memory reading/writing.

<p align="center">
  <img src="https://github.com/dimacotorobai/DeadSpace2Trainer/assets/52585921/5f3d981e-4633-4915-9476-64028cb42097.png?raw=true" alt="DeadSpace2 Trainer Image"/>
</p>

## Instructions
To use this application the user must either run the executable provided in the releases section or run the Python interpreter on the DeadSpace2Trainer.py file. Below I have provided step-by-step instructions on how to install and run the DeadSpace2 trainer using the Python interpreter.

### Step By Step
  * Download Python from *https://www.python.org/downloads/*. This project was created using Python 3.10 but will work on all Python 3.6+ versions.
  * Add both the Python and PIP executables to your PATH
      * Navigate to Control Panel > System > Edit the system environment variables > Environment Variables > Path > Edit
      * Add the Python executable path(i.e. C:\Users\Dima\AppData\Local\Programs\Python\Python310\)
      * Add the PIP executable path(i.e. C:\Users\Dima\AppData\Local\Programs\Python\Python310\Scripts\)
      * Press OK
  * Install both *pywin32* and *psutil*. These packages can be downloaded from the PyPI repository.
      * Open up the command prompt
      * Run *pip install pywin32* to install pywin32
      * Run *pip install psutil* to install psutil
  * Install the DeadSpace2Trainer
      * Download the project and unzip it to the desired location
      * Or use git to clone the project(*git clone https://github.com/dimacotorobai/DeadSpace2Trainer.git*)
  * Open up a command prompt in the project directory and run "*python DeadSpace2Trainer.py*"
  * Enjoy playing the game with the trainer :)
  

## Project Goal
My goal for this project was to create an application using Python while building on my pre-existing knowledge of operating systems and game hacking. I am also a fan of the Dead Space games(including DS3) and so creating a trainer for Dead Space 2 seemed like a normal idea.
 
## Help
This project could not have been built without the excellent tutorials provided by GuidedHacking. The process of finding offsets, reverse engineering, and writing the code required for memory reading/writing was learned from GuidedHacking.
