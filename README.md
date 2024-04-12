# Python Project Creator

Python Script that automatically sets up files and folders for a new Python project and optionally initializes a local git repository as well as a virtual environment.


## Installation

To run the script Python and Git need to be installed. The script must be run from a Bash shell.


## Usage

Note that the script is tailored to my personal needs.
I am running it on a Windows machine using GitBash as a terminal, therefore the script uses Bash commands. The script has not been tested in other environments. 
Feel free to adapt it to your personal needs.

To run the program in Bash:
```bash
python set_up_project.py project-name git venv
```

The first command line argument provides the project's name which will be used for folder and venv creation, the second argument indicates whether or not a git repo should be initialized (valid inputs: "git", "y", "yes"), the third argument does the same for creating a virtual environment (valid inputs: "venv", "y", "yes").

```bash
python set_up_project.py
```

If no, or incomplete command line arguments are being provided, the user will be prompted to enter the missing data during script execution.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License

[MIT](https://choosealicense.com/licenses/mit/)