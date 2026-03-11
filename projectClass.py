import json

class Project():
    def __init__(self, projectName):
        self._projectName = projectName
        try:
            _check = open(f"project/{projectName}.json", "r")
            _check.close()
        except:
            _data = {
                "Structure": {
                    "Floor": [],
                    "Room": {},
                    "Connector": {},
                    "Checkpoint": {}
                },
                "Floor Connect": [],
                "Room Connect": {},
                "Checkpoint Connect": {}
            }
            with open(f"project/{projectName}.json", "w") as _file:
                json.dump(_data, _file, indent = 4)
    
    def updateProject(self, data):
        with open(f"project/{self._projectName}.json", "w") as _file:
            json.dump(data, _file, indent = 4)
    
    def getStructure(self):
        with open(f"project/{self._projectName}.json", "r") as _file:
            _data = json.load(_file)
        return [_data["Structure"]["Floor"], _data["Structure"]["Room"], _data["Structure"]["Connector"], _data["Structure"]["Checkpoint"]]
    
    def getFloorConnect(self):
        with open(f"project/{self._projectName}.json", "r") as _file:
            _data = json.load(_file)
        return _data["Floor Connect"]
    
    def getRoomConnect(self):
        with open(f"project/{self._projectName}.json", "r") as _file:
            _data = json.load(_file)
        return _data["Room Connect"]

    def getCheckpointConnect(self):
        with open(f"project/{self._projectName}.json", "r") as _file:
            _data = json.load(_file)
        return _data["Checkpoint Connect"]
