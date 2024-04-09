# automate the following project setup procedure

# DONE >> mkdir new_project					    # creates new project folder
# N/A  >> cd new_project					    # changes into new project folder
# DONE >> touch new_project.py				    # creates new python file
# DONE >> touch README.md					    # creates Markdown Readme file	
# DONE >> touch TODO.txt					    # creates TODO file
# >> python -m venv venv --prompt new-venv		# creates virtual environment called venv with a display name of new-venv
# >> source venv/Scripts/activate				# activates virtual environment
# DONE >> touch .gitignore					    # creates .gitignore file: files and directories specified in here will be ignored by git
# DONE >> echo __pycache__ >> .gitignore		# adds __pycache__ to .gitignore
# DONE >> echo venv/ >> .gitignore				# adds venv/ to .gitignore
# DONE >> echo TODO.txt >> .gitignore			# adds TODO.txt to .gitignore
# >> git init						            # initializes git for the project
# >> git add --all					            # adds .gitignore to the staging area
# >> git commit -m "setup project"			    # commits the changes

# --> create same project on github and follow instructions to push existing repo from command line


# import os module for interaction with the computer's operating system

import os, sys

p_name = sys.argv[1] # TODO: add try except block
p_path = "./" + p_name

# Create project directory

try:
    os.mkdir(p_path)
    print(f"\nCreating folder {p_name} ... Path: {p_path}\n")
except FileExistsError:
    print(f"\nFolder already exists: {p_path} --> Execution aborted.\nRe-run script with a different project name.\n")
except OSError:
    print(f"\nInvalid file name: {p_name} --> Execution aborted.\nRe-run script with a different project name not including any of the characters ---'\\/:*?<>|' or a space character")

# create files

files_tbc = [
    {"name": "TODO.txt", "content": ""},
    {"name": "README.md", "content": ""},
    {"name": p_name + ".py", "content": ""},
    {"name": ".gitignore", "content": "__pycache__\nTODO.txt\n/venv\n"}
]

print(files_tbc)

for file in files_tbc:
    f_path = p_path + "/" + file["name"]
    fd = os.open(f_path, os.O_RDWR|os.O_CREAT)  # creates and opens file
    fo = os.fdopen(fd, "w+")  # gets a file object for the file
    fo.write(file["content"])  # writes something on open file
    fo.close() # closes file

# create subfolders

# venv_path = p_path + "/venv"
# os.mkdir(venv_path)

# Testing

