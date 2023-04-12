#create a script that automatically saves output as a .sh makes it executable and then runs the same script
#write the same script except use chatgpt code as input
##Here's the code that will create a python script, save it as a .sh file, make it executable and then execute it:


import os

# Create the output script and add some basic commands to it
with open('output.sh', 'w') as f:
    f.write('#!/bin/bash')
    f.write('echo "Hello World"')
    f.write('echo "This is a test"')

# Make the script executable
os.chmod('output.sh', 0o755)

# Execute the script
os.system('./output.sh')


#This code creates a file called "output.sh" and writes some basic commands to the file. Then, it changes the permissions of the file to make it executable. Finally, it executes the script using the `os.system()` command.