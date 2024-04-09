import os, sys, subprocess

# --- HELPER FUNCTIONS ---


def create_project_dir(name: str, path: str):
    """Create project directory."""
    try:
        os.mkdir(path)
        print(f"\nCreating folder {name} ... Path: {path}\n")
    except FileExistsError:
        print(f"\nFolder already exists: {path} --> Execution aborted.\nRe-run script with a different project name.\n")
    except OSError:
        print(f"\nInvalid file name: {name} --> Execution aborted.\nRe-run script with a different project name not including any of the characters ---'\\/:*?<>|' or a space character")


def create_files(files: list, path: str):
    """Create project's files from file list."""
    for file in files:
        f_path = path + "/" + file["name"]
        fd = os.open(f_path, os.O_RDWR | os.O_CREAT)  # creates and opens file
        fo = os.fdopen(fd, "w+")  # gets a file object for the file
        fo.write(file["content"])  # writes something in open file
        fo.close()  # closes file


def load_template(filename):
    """Load sample file and return its text"""
    with open(filename) as template:
        return template.read()


def git_init_first_commit():
    """Set up git repository, stage files and make first commit."""
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "--all"])
    subprocess.run(["git", "commit", "-m", '"set up project files and folders"'])


def create_venv_name(p_name: str) -> str:
    """Shorten project name for venv prompt."""
    v_name = ""
    splitter = ""
    if "_" in p_name:
        splitter = "_"
    elif "-" in p_name:
        splitter = "-"
    if splitter:
        p_name_list = p_name.split(splitter)
        for word in p_name_list:
            v_name += word[0].upper()
    else:
        v_name = p_name[:5]
    approved = input(f"\nPrompt name of venv is set to {v_name}. To change it enter new name --> ")
    if approved:
        v_name = approved
    return v_name


def create_venv(v_name: str):
    """Create virtual environment."""
    subprocess.run(["python", "-m", "venv", "venv", "--prompt", v_name])


def main():
    """
    Use command line arguments or prompt user to create Python project folder
    and files, a git repository and a virtual environment.
    """
    try:
        p_name = sys.argv[1]
    except:
        p_name = input("\nEnter project name --> ")
    p_path = "./" + p_name
    files_tbc = [
        {"name": "TODO.txt", "content": load_template("./templates/sample_TODO.txt")},
        {"name": "README.md", "content": load_template("./templates/sample_readme.txt")},
        {"name": p_name + ".py", "content": ""},
        {"name": ".gitignore", "content": "__pycache__\nTODO.txt\n/venv\n"}
]
    create_project_dir(p_name, p_path)
    create_files(files_tbc, p_path)
    os.chdir(p_name)  # changes the directory

    try:
        git = sys.argv[2]
    except:
        git = input("\nInitialize git repository? (y) --> ")

    if git in ["git", "y", "yes"]:
        git_init_first_commit()
        print("\n--- To make repo available remotely create same project on GitHub and follow instructions to push existing repo from command line ---")

    try:
        venv = sys.argv[3]
    except:
        venv = input("\nCreate virtual environment? (y) --> ")

    if venv in ["venv", "y", "yes"]:
        print("\nSetting up the virtual environment will take a moment. Please wait ...")
        v_name = create_venv_name(p_name)
        create_venv(v_name)


if __name__ == "__main__":
    main()