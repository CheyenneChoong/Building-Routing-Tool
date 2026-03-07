import time
import textwrap
from projectClass import Project

def manageFloors(project):
    while True:
        print("\033c")
        _structure = project.getStructure()
        _floors = _structure[0]
        print(textwrap.dedent(f"""\
        {"-" * 25}
        | BUILDING ROUTING TOOL |
        {"-" * 25}
        Manage Floors

        {", ".join(_floors)}

        1. Add floor.
        2. Remove floor.
        3. Exit.
        """))
        _action = input("Selection: ")

        try:
            _action = int(_action)
            if _action == 1:
                _floorName = input("Floor Name: ")
                if _floorName not in _floors and _floorName.strip():
                    _floors.append(_floorName.strip())
                else:
                    print("Floor name already exists or invalid floor name.")
                    time.sleep(2)
                    pass
            elif _action == 2:
                _floorName = input("Floor Name to Remove: ")
                if _floorName.strip() in _floors:
                    _floors.remove(_floorName.strip())
                else:
                    print("Invalid floor name.")
                    time.sleep(2)
                    pass
            elif _action == 3:
                break
            _data = {
                "Structure": {
                    "Floor": _floors,
                    "Room": _structure[1],
                    "Connector": _structure[2]
                },
                "Floor Connect": project.getFloorConnect(),
                "Room Connect": project.getRoomConnect()
            }
            project.updateProject(_data)
        except:
            pass

def manageRooms(project):
    while True:
        print("\033c")
        _structure = project.getStructure()
        _rooms = _structure[1]
        print(textwrap.dedent(f"""\
        {"-" * 25}
        | BUILDING ROUTING TOOL |
        {"-" * 25}
        Manage Rooms

        {", ".join(_rooms)}

        1. Add room.
        2. Remove room.
        3. Exit.
        """))
        _action = input("Selection: ")

        try:
            _action = int(_action)
            if _action == 1:
                _roomName = input("Room Name: ")
                if _roomName not in _rooms and _roomName.strip():
                    _rooms.append(_roomName.strip())
                else:
                    print("Room name already exists or invalid floor name.")
                    time.sleep(2)
                    pass
            elif _action == 2:
                _roomName = input("Room Name to Remove: ")
                if _roomName.strip() in _rooms:
                    _rooms.remove(_roomName.strip())
                else:
                    print("Invalid room name.")
                    time.sleep(2)
                    pass
            elif _action == 3:
                break
            _data = {
                "Structure": {
                    "Floor": _structure[0],
                    "Room": _rooms,
                    "Connector": _structure[2]
                },
                "Floor Connect": project.getFloorConnect(),
                "Room Connect": project.getRoomConnect()
            }
            project.updateProject(_data)
        except:
            pass

def manageConnectors(project):
    while True:
        print("\033c")
        _structure = project.getStructure()
        _connectors = _structure[2]
        print(textwrap.dedent(f"""\
        {"-" * 25}
        | BUILDING ROUTING TOOL |
        {"-" * 25}
        Manage Connectors

        {", ".join(_connectors)}

        1. Add connector.
        2. Remove connector.
        3. Exit.
        """))
        _action = input("Selection: ")

        try:
            _action = int(_action)
            if _action == 1:
                _connectorName = input("Connector Name: ")
                if _connectorName not in _connectors and _connectorName.strip():
                    _connectors.append(_connectorName.strip())
                else:
                    print("Connector name already exists or invalid connector name.")
                    time.sleep(2)
                    pass
            elif _action == 2:
                _connectorName = input("Connector Name to Remove: ")
                if _connectorName.strip() in _connectors:
                    _connectors.remove(_connectorName.strip())
                else:
                    print("Invalid connector name.")
                    time.sleep(2)
                    pass
            elif _action == 3:
                break
            _data = {
                "Structure": {
                    "Floor": _structure[0],
                    "Room": _structure[1],
                    "Connector": _connectors
                },
                "Floor Connect": project.getFloorConnect(),
                "Room Connect": project.getRoomConnect()
            }
            project.updateProject(_data)
        except:
            pass

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
        Rooms: {len(_structure[1])}
        Connector: {len(_structure[2])}
        *Note: Connectors refer to whatever that links two separate floors. (e.g. stairs)

        1. Manage floors.
        2. Manage rooms.
        3. Manage connectors.
        4. Mapping.
        5. Set up route.
        6. Test routing.
        7. Exit.
        """))
        _redirect = input("Selection: ")
    
        try:
            _redirect = int(_redirect)
            if _redirect == 1:
                manageFloors(_project)
            elif _redirect == 2:
                manageRooms(_project)
            elif _redirect == 3:
                manageConnectors(_project)
            elif _redirect == 4:
                print("Mapping")
            elif _redirect == 5:
                print("Set Up Route")
            elif _redirect == 6:
                print("Test Routing")
            elif _redirect == 7:
                break
        except:
            pass