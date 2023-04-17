# FreezeTag-Recursive
### A simple python script that loops through a directory and runs the freezetag command on every directory and subdirectory allowing for the folder and file names and all metadata to be recovered if needed with the unfreeze command.

Freezetag is a CLI tool that is meant to be run with a command from in the terminal and this script just loops through a directory and runs it for every folder it encounters. This script is very basic and has only been tested on windows 7 and 10. In Windows freezetag does not create a .ftag file if certain special characters with non normative encodings are in the directory name and this script doesn't either. Some characters it gracefully skips and other characters it crashes. Look through the output of the script in the terminal or check the directories to make sure it created a freezetag file for all of them.  You can use the CLI to enter any directory that it didn't work on run the freezetag freeze command directly there and it should work.

This script is meant to work in conjunction with other scripts in order to manage a large music library when the source of the music has good metadata you want to use to organize it.  You can find an overview of the scripts and workflow at [Origin-Music-Management](https://github.com/spinfast319/Origin-Music-Management). 

## Dependencies
This project has a dependency on the freezetag project created by x1ppy. Freezetag is a tool that saves, strips, and restores file paths and music metadata. This metadata is written to a freezetag file (usually just a few kB) that can transform downloaded music files between different filename/tag states. The freezetag application is here: https://github.com/x1ppy/freezetag

## Install and set up
1) Clone this script where you want to run it.

2) Install [freezetag](https://github.com/x1ppy/freezetag) following the instructions on that github page 


3) Edit the script where it says _Set your directory here_ to set up or specify the directory you will be using. Write them as absolute paths for:

    A. The directory where the albums you want to run freezetag on are stored  

4) Use your terminal to navigate to the directory the script is in and run the script from the command line.  When it finishes it will output how many times it ran freesetag.

```
FreezeTag-Recursive.py
```

_note: on linux and mac you will likely need to type "python3 FreezeTag-Recursive.py"_  
_note 2: you can run the script from anywhere if you provide the full path to it_
