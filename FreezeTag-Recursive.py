#!/usr/bin/env python3

# FreezeTag-Recursive
# author: hypermodified
# A simple python script that loops through a directory and runs the freezetag command on every directory and subdirectory allowing for the folder, filenames and metadata to be recovered if changed.
# It then checks each directory to make sure a .ftag file is there and logs those that are missing.
# It can handle albums with artwork folders or multiple disc folders in them.
# It can also handle specials characters and skips and logs any characters that makes windows fail.
# It has been tested and works in both Ubuntu Linux and Windows 10.

# Import dependencies
import os  # Imports functionality that let's you interact with your operating system
from freezetag import commands # Imports freezetag
import datetime  # Imports functionality that lets you make timestamps

#  Set your directories here
album_directory = "M:\PROCESS"  # Which directory do you want to start with?
log_directory = "M:\PROCESS-LOGS\Logs"  # Which directory do you want the log in?

# Establishes the counters for completed albums and missing origin files
count = 0
ftag_create_count = 0
ftag_missing = 0
error_message = 0

# Sets up the list of folders missing ftags
missing_ftag_list = []

# A function to log events
def log_outcomes(directory, log_name, message):
    global log_directory

    script_name = "Freeze Tag Recursive Script"
    today = datetime.datetime.now()
    log_name = f"{log_name}.txt"
    album_name = directory.split(os.sep)
    album_name = album_name[-1]
    log_path = os.path.join(log_directory, log_name)
    with open(log_path, "a", encoding="utf-8") as log_name:
        log_name.write(f"--{today:%b, %d %Y} at {today:%H:%M:%S} from the {script_name}.\n")
        log_name.write(f"The album folder {album_name} {message}.\n")
        log_name.write(f"Album location: {directory}\n")
        log_name.write(" \n")
        log_name.close()


# A function that determines if there is an error
def error_exists(error_type):
    global error_message

    if error_type >= 1:
        error_message += 1  # variable will increment if statement is true
        return "Warning"
    else:
        return "Info"


# A function that writes a summary of what the script did at the end of the process
def summary_text():
    global count
    global ftag_create_count
    global ftag_missing
    global error_message

    print("")
    print(f"This script created {ftag_create_count} freezetag files for {count} folders examined.")
    print("")
    print("This script looks for potential missing files or errors. The following messages outline whether any were found.")

    error_status = error_exists(ftag_missing)
    print(f"--{error_status}: There were {ftag_missing} missing freezetag files for {count} folders examined..")

    if error_message >= 1:
        print("Check the logs to see which folders had errors and what they were.")
    else:
        print("There were no errors.")


#  A function that gets the directory and then runs the freezetag freeze command plus the directory
def freeze_folder(directory):
    global ftag_create_count
    
    print("")
    print(f"Listing: {directory}")
    print("\t-" + "\n\t-".join(os.listdir(".")))  # List current working directory
    commands.freeze(directory, False, directory) # Executes the freezetag freeze command on the directory you are in
    ftag_create_count += 1  # variable will increment every loop iteration


# The main function that controls the flow of the script
def main():
    global count
    
    try:
        # intro text
        print("")
        print("In this universe, there's only one absolute. ")
        print("")
        print("Part 1: Freezing")
        
        # Get all the subdirectories of album_directory recursively and store them in a list:
        directories = [os.path.abspath(x[0]) for x in os.walk(album_directory)]
        directories.remove(os.path.abspath(album_directory))  # If you don't want your main directory included

        #  Run a loop that goes into each directory identified in the list and runs the function that runs freezetag
        for i in directories:
            os.chdir(i)  # Change working Directory
            freeze_folder(i)  # Run your function
            count += 1  # variable will increment every loop iteration
            
            
        #print("Part 2: Checking for missing freeze files")    
    
    finally:
        # Summary text
        print("")
        print("Everything freezes.")
        # run summary text function to provide error messages
        summary_text()
        print("")

if __name__ == "__main__":
    main()

"""      
In windows freezetag does not create a .ftag file if certain special characters with non normative encodings are in the directory name and this script doesn't either. Some characters it gracefully skips and other characters it crashes. 
"""
