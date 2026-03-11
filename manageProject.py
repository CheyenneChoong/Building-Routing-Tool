import time
import textwrap
from projectClass import Project

def manageFloors(project):
    while True:
        print("\033c")
        _structure = project.getStructure()
        _floorConnect = project.getFloorConnect()
        _roomConnect = project.getRoomConnect()
        _checkpointConnect = project.getCheckpointConnect()
        _floors = _structure[0]
        _rooms = _structure[1]
        _connectors = _structure[2]
        _checkpoints = _structure[3]

        print(textwrap.dedent(f"""\
        {"-" * 25}
        | BUILDING ROUTING TOOL |
        {"-" * 25}
        Manage Floors

        {", ".join(_floors)}

        1. Add floor.
        2. Remove floor.
        3. Clear floor.
        4. Exit.
        """))
        _action = input("Selection: ")

        try:
            _action = int(_action)
            if _action == 1:
                _floorName = input("Floor Name: ")
                if _floorName not in _floors and _floorName.strip():
                    _floors.append(_floorName.strip())
                    _rooms[_floorName] = []
                    _connectors[_floorName] = []
                    _checkpoints[_floorName] = []
                    _roomConnect[_floorName] = []
                    _checkpointConnect[_floorName] = []
                else:
                    print("Floor name already exists or invalid floor name.")
                    time.sleep(2)
                    pass
            elif _action == 2:
                _floorName = input("Floor Name to Remove: ")
                if _floorName.strip() in _floors:
                    _floors.remove(_floorName.strip())
                    _rooms.pop(_floorName)
                    _connectors.pop(_floorName)
                    _checkpoints.pop(_floorName)
                    _roomConnect.pop(_floorName)
                    _checkpointConnect.pop(_floorName)
                    _floorConnect = []
                else:
                    print("Invalid floor name.")
                    time.sleep(2)
                    pass
            elif _action == 3:
                _floors = []
            elif _action == 4:
                break
            _data = {
                "Structure": {
                    "Floor": _floors,
                    "Room": _rooms,
                    "Connector": _connectors,
                    "Checkpoint": _checkpoints
                },
                "Floor Connect": _floorConnect,
                "Room Connect": _roomConnect,
                "Checkpoint Connect": _checkpointConnect
            }
            project.updateProject(_data)
        except:
            pass

def redirectFloor(project):
    _structure = project.getStructure()
    _floors = _structure[0]
    print("")
    for _floor in _floors:
        print(_floor)
    _floorSelection = input("Select Floor: ")
    _floorSelection = _floorSelection.strip()
    if _floorSelection in _floors:
        return _floorSelection
    else:
        return False

def manageRoomConnector(project, floor):
    while True:
        _structure = project.getStructure()
        _floorConnect = project.getFloorConnect()
        _roomConnect = project.getRoomConnect()
        _checkpointConnect = project.getCheckpointConnect()
        print("\033c")
        print(textwrap.dedent(f"""\
        {"-" * 25}
        | BUILDING ROUTING TOOL |
        {"-" * 25}
        Manage Rooms and Connectors on floor {floor}

        Rooms:
        {", ".join(_structure[1][floor])}

        Connectors:
        {", ".join(_structure[2][floor])}

        1. Add room.
        2. Add connector.
        3. Add checkpoint.
        4. Remove room / connector / checkpoint.
        5. Clear room.
        6. Clear connector.
        7. Clear checkpoint.
        8. Exit.
        """))
        _action = input("Selection: ")
        try:
            _action = int(_action)
        except:
            pass

        if _action == 8:
            break
        elif _action == 5:
            _structure[1][floor] = []
        elif _action == 6:
            _structure[2][floor] = []
        elif _action == 7:
            _structure[3][floor] = []

        _name = input("Name: ")
        _name = _name.strip()

        if _name and _action == 1 and _name not in _structure[1][floor] and _name not in _structure[2][floor]:
            _structure[1][floor].append(_name)
        elif _name and _action == 2 and _name not in _structure[1][floor] and _name not in _structure[2][floor]:
            _structure[2][floor].append(_name)
            _structure[3][floor].append(_name)
        elif _name and _action == 3 and (_name in _structure[1][floor] or _name in _structure[2][floor]) and _name not in _structure[3][floor]:
            _structure[3][floor].append(_name)
        if _name and _action == 4 and _name in _structure[1][floor]:
            _structure[1][floor].remove(_name)
            _roomConnect[floor] = []
        if _name and _action == 4 and _name in _structure[2][floor]:
            _structure[2][floor].remove(_name)
            _floorConnect[floor] = []
        if _name and _action == 4 and _name in _structure[3][floor]:
            _structure[3][floor].remove(_name)
            _checkpointConnect[floor] = []
        else:
            print("Invalid input or room / connector exists.")
        
        _data = {
            "Structure": {
                "Floor": _structure[0],
                "Room": _structure[1],
                "Connector": _structure[2],
                "Checkpoint": _structure[3]
            },
            "Floor Connect": _floorConnect,
            "Room Connect": _roomConnect,
            "Checkpoint Connect": _checkpointConnect
        }
        project.updateProject(_data)

def work(projectName):
    _project = Project(projectName)
    while True:
        print("\033c")
        _structure = _project.getStructure()
        print(textwrap.dedent(f"""\
        {"-" * 25}
        | BUILDING ROUTING TOOL |
        {"-" * 25}
        {projectName}

        Floors: {len(_structure[0])}
        {", ".join(_structure[0])}

        1. Manage floors.
        2. Manage rooms, connectors and checkpoints.
        3. Set up map.
        4. Test routing.
        5. Exit.
        """))
        _redirect = input("Selection: ")
    
        try:
            _redirect = int(_redirect)
            if _redirect == 1:
                manageFloors(_project)
            elif _redirect == 2:
                _floor = redirectFloor(_project)
                if _floor:
                    manageRoomConnector(_project, _floor)
                else:
                    print("Invalid floor.")
                    time.sleep(2)
            elif _redirect == 3:
                print("Mapping")
            elif _redirect == 4:
                print("Test Route")
            elif _redirect == 5:
                break
        except:
            pass