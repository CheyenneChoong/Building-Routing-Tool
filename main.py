"""
main.py serves as the starting point.
Only this file should be run.
"""
from manageFile import createProject, openProject, duplicateProject
import textwrap

welcome = textwrap.dedent(f"""\
    {"-" * 25}
    | BUILDING ROUTING TOOL |
    {"-" * 25}
    Welcome, what are we doing today?

    1. New project
    2. Open project
    3. Duplicate project
    4. Exit

    Selection: """)

while True:
    print("\033c")
    redirect = input(welcome)
    try:
        redirect = int(redirect)
        if redirect == 1:
            createProject()
        elif redirect == 2:
            openProject()
        elif redirect == 3:
            duplicateProject()
        elif redirect == 4:
            break
    except:
        pass