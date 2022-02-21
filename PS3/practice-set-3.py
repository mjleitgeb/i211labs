# Practice Set 3
# ! Use this file as your starter file
# ! Do not move this file outside of the provided directory and files
# ! Reference the slides for Practice Set 3 for details on using the os module
# os module documentation:
# https://docs.python.org/3/library/os.html?highlight=os#module-os
import os



dir_list = []
resources = os.listdir(os.getcwd())                 # creating a list with the directories 
for item in resources:
    if os.path.isdir(item) == True:
        dir_list.append(item)
print(dir_list)

def directory_choice(choice):                                       # function for the user to select the directory
    while choice != '':
        if choice in dir_list:
            print('Selected directory:', choice)
            break
        else:
            print('That is not a valid directory, try again.')
            choice = input('Choose a directory')

def print_files(dir_choice):                                        # function that will print the files of the users directory
    if dir_choice == 'other_files':
        os.chdir(os.path.join(os.getcwd(), "other_files"))
    if dir_choice == 'more_files':
        os.chdir(os.path.join(os.getcwd(), "more_files"))  
 
    contents = os.listdir(os.getcwd())
    for item in contents:
        if os.path.isfile(item) == True:
            print(item) 

# PS 3.1
# Write a function directory_choice() that prints the names of all the 
# directories in the current working directory (but not the files), 
# then ask the user to choose one of the directories. 
user_choice = input('Choose a directory')
directory_choice(user_choice)                       # calling direcotry choice function

# new_file4 = open('file_4.txt', 'x')                           # creation of the three extra files (commented out because it would cause errors if ran again)
# new_file5 = open('file_5.txt', 'x')
# new_file6 = open('file_6.txt', 'x')

print_files(user_choice)                            # calling print file function

# If the user gives you something that isn’t valid (isn’t a directory name), 
# ask again until it’s a valid directory name.

# Example output:
# Current Directories:
# ['more_files', 'other_files'] 
# Please select a directory: files
# That is not a valid directory, try again
# Please select a directory: more_files
# Selected directory: more_files




# PS 3.2
# Using the os module and your file skills,
# create three new files in our current directory:
# file-4.txt, file-5.txt and file-6.txt



# PS 3.3
# Expand your code from PS 3.1 by writing a new function print_files()
# In your main, once you have selected a valid directory (PS 3.1):
# add functionality to move into the selected directory, 
# and then print out all valid file names
# (each file name should print on its own line, do not print any directories)

# Example output:
# Current Directories:
# ['more_files', 'other_files'] 
# Please select a directory: files
# That is not a valid directory, try again
# Please select a directory: more_files
# Selected directory: more_files
# Available files:
# more-1.txt
# more-2.txt




