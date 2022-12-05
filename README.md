## DeadSpace2 Trainer
This is a trainer for the game Dead Space 2. This trainer was created in python with the help of the pywin32 library. This trainer contains Godmode, Infinite Ammo, Infinite Stasis, and Infinite Air, as well as Get and Set Nodes and Credits. This is an external hack that uses code injection, code caves, and memory reading/writing.

<p align="center">
  <img src="https://user-images.githubusercontent.com/52585921/124494449-d9892f00-dd84-11eb-9d80-7e6f28f55b3c.jpg?raw=true" alt="DeadSpace2 Trainer Image"/>
</p>


## Instructions
To use this application the user must have Python installed and the required libraries. The user can either use the regular GUI trainer(DeadSpace2Trainer.py) or the console version of the trainer(DS2ConsoleTrainer.py). Below I have provided step-by-step instructions on how to install and run the DeadSpace2 trainer.

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
  * Open up a command prompt in the project directory and run "*python DeadSpace2Trainer.py*" or "*python DS2ConsoleTrainer.py*"
  * Enjoy playing the game with the trainer :)
  

## Project Goal
My goal for this project was to create an application using Python while building on my pre-existing knowledge of operating systems and game hacking. I am also a fan of the Dead Space games(including DS3) and so creating a trainer for Dead Space 2 seemed like a normal idea.
 
## Help
This project could not have been built without the excellent tutorials provided by GuidedHacking. The process of finding offsets, reverse engineering, and writing the code required for memory reading/writing was learned from GuidedHacking.
