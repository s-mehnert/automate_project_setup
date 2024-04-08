# automate the following project setup procedure

# >> mkdir new_project					# creates new project folder
# >> cd new_project					# changes into new project folder
# >> touch new_project.py					# creates new python file
# >> touch README.md					# creates Markdown Readme file	
# >> touch TODO.txt					# creates TODO file
# >> python -m venv venv --prompt new-venv		# creates virtual environment called venv with a display name of new-venv
# >> source venv/Scripts/activate				# activates virtual environment
# >> touch .gitignore					# creates .gitignore file: files and directories specified in here will be ignored by git
# >> echo __pycache__ >> .gitignore			# adds __pycache__ to .gitignore
# >> echo venv/ >> .gitignore				# adds venv/ to .gitignore
# >> echo TODO.txt >> .gitignore				# adds TODO.txt to .gitignore
# >> git init						# initializes git for the project
# >> git add --all					# adds .gitignore to the staging area
# >> git commit -m "setup project"			# commits the changes

# --> create same project on github and follow instructions to push existing repo from command line
