from multiprocessing.spawn import old_main_modules
import os


# Part 1: write a short program that prints out the names of all of the contents 
# of the examples/more_examples directory.

print(os.listdir("/Users/maxleitgeb/Desktop/i211/I211_labs/lab3/lab_03_starter/examples/more_examples"))




#Part 2: Change the current working directory to the resources/code/ directory.
# Print out the names of all of the files (not directories!) and their sizes
os.chdir(os.path.join(os.getcwd(), "resources/code/"))
print(os.listdir(os.getcwd()))


#Part 3: Rename the functions.py file to database_functions.py.
#os.rename('functions.py', 'database_functions.py')

