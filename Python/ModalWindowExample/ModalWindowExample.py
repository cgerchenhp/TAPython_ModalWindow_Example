import unreal
from Utilities.Utils import Singleton

class ModalWindowExample(metaclass=Singleton):
    def __init__(self, json_path:str):
        self.json_path = json_path
        self.data:unreal.ChameleonData = unreal.PythonBPLib.get_chameleon_data(self.json_path)
