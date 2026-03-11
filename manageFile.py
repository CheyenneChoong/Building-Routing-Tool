import time
import os
import textwrap
import json
from projectClass import Project
from manageProject import work

os.makedirs("project", exist_ok=True)
try:
    _check = open("project/project.txt", "r")
    _check.close()
except:
    _check = open("project/project.txt", "w")
    _check.close()

def openProject():
    _header = textwrap.dedent(f"""\
    {"=" * 25}
    | BUILDING ROUTING TOOL |
    {"=" * 25}
    Open Project
    """)
    while True:
        print("\033c")
        print(_header)
        with open("project/project.txt", "r") as _file:
            for _line in _file:
                print(_line.strip("\n"))
        print("")
        _projectName = input("Open Project: ")
        _projectName = _projectName.strip()
        if os.path.exists(f"project/{_projectName}.json"):
           work(_projectName)
        else:
            print("Project doesn't exists or there is a typo.")
            time.sleep(2)

def duplicateProject():
    _header = textwrap.dedent(f"""\
    {"-" * 25}
    | BUILDING ROUTING TOOL |
    {"-" * 25}
    Duplicate Project
    """)
    while True:
        print("\033c")
        print(_header)
        with open("project/project.txt", "r") as _file:
            for _line in _file:
                print(_line.strip("\n"))
        print("")
        _duplicate = input("Duplicate Project: ")
        _duplicate = _duplicate.strip()
        if not os.path.exists(f"project/{_duplicate}.json"):
            print("Project doesn't exists or there is a typo.")
            time.sleep(2)
            pass
        _projectName = input("Project Name: ")
        _projectName = _projectName.strip()
        if " " not in _projectName and not os.path.exists(f"project/{_projectName}.json") and len(_projectName) > 0:
            Project(_projectName)
            with open("project/project.txt", "a") as _file:
                _file.write(_projectName + "\n")
            with open(f"project/{_duplicate}.json", "r") as _file:
                _data = json.load(_file)
            with open(f"project/{_projectName}.json", "w") as _file:
                json.dump(_data, _file, indent=4)
            print(f"Project duplicated successfully.")
            time.sleep(2)
            break
        else:
            print(f"Project name already taken or contains space.")
            time.sleep(2)
        
def createProject():
    _header = textwrap.dedent(f"""\
    {"=" * 25}
    | BUILDING ROUTING TOOL |
    {"=" * 25}
    Create New Project

    Note: Project name can't have any spaces.
    Project Name: """)
    while True:
        print("\033c")
        _projectName = input(_header)
        _projectName = _projectName.strip()
        if " " not in _projectName and not os.path.exists(f"project/{_projectName}.json") and len(_projectName) > 0:
            Project(_projectName)
            with open("project/project.txt", "a") as _file:
                _file.write(_projectName + "\n")
            print(f"Project: {_projectName} created successfully.")
            time.sleep(2)
            break
        else:
            print(f"Project name already taken or contains space.")
            time.sleep(2)