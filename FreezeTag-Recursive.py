# FreezeTag-Recursive
# author: hypermodified
# A simple python script that loops through a directory and runs the freezetag command on every directory and subdirectory allowing for the folder and file names and all metadata to be recovered if needed with the unfreeze command.

# Import dependencies
import os  # Imports functionality that let's you interact with your operating system
import subprocess  # Imports functionality that let's you run command line commands in a script
import freezetag  # Imports freezetag

COUNT = 0

#  Set your directory here
directory_to_check = "M:\POST-PROCESS\FREEZE" # Which directory do you want to start with?

#  A function that gets the directory and then runs the freezetag freeze command plus the directory
def my_function(directory):
      global COUNT
      print("Listing: " + directory)
      print("\t-" + "\n\t-".join(os.listdir("."))) # List current working directory
      subprocess.run ("freezetag freeze \"" + directory + "\"") # Executes the freesetag freeze command on the directory you are in
      COUNT += 1  # variable will increment every loop iteration

# Get all the subdirectories of directory_to_check recursively and store them in a list:
directories = [os.path.abspath(x[0]) for x in os.walk(directory_to_check)]
directories.remove(os.path.abspath(directory_to_check)) # If you don't want your main directory included

#  Run a loop that goes into each directory identified in the list and runs the function that runs freezetag
for i in directories:
      os.chdir(i)         # Change working Directory
      my_function(i)      # Run your function
      
print(f"Freeze tag ran {COUNT} times.")      
      
"""      
In windows 7 freezetag does not create a .ftag file if certain special characters with non normative encodings are in the directory name and this script doesn't either. Some characters it gracefully skips and other characters it crashes. 
"""