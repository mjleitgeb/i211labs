from multiprocessing.spawn import old_main_modules
import os


# Part 1: write a short program that prints out the names of all of the contents 
# of the examples/more_examples directory.

print(os.listdir("/Users/maxleitgeb/Desktop/i211/I211_labs/lab3/lab_03_starter/examples/more_examples"))




#Part 2: Change the current working directory to the resources/code/ directory.
# Print out the names of all of the files (not directories!) and their sizes
os.chdir(os.path.join(os.getcwd(), "resources/code/"))
resources = os.listdir(os.getcwd())
for item in resources:
    if os.path.isfile(item) == True:
        print(item)
        print(os.path.getsize(item))
# print(os.path.getsize(".DS_Store"))
# print(os.path.getsize("code1.py"))
# print(os.path.getsize("code2.py"))
# print(os.path.getsize("database_functions.py"))

#Part 3: Rename the functions.py file to database_functions.py.
#os.rename('functions.py', 'database_functions.py')

