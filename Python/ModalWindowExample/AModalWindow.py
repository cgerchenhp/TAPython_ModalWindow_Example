import unreal
from Utilities.Utils import Singleton


class AModalWindow(metaclass=Singleton):
    def __init__(self, json_path: str):
        self.json_path = json_path
        self.data: unreal.ChameleonData = unreal.PythonBPLib.get_chameleon_data(self.json_path)
        self.ui_buttons_room = "SomePlaceForButtons"
        self.button_count = 0

    def add_button(self):
        print("add_button call.")
        button_json_content = """
            {
                "SButton": { 
                    "Text": "PlaceHolder Button"
                    , "ContentPadding": [-8, 0]
                    , "VAlign": "Center"
                    , "HAlign": "Center" 
                }
            }
            """

        self.data.append_slot_from_json(self.ui_buttons_room, button_json_content)
        self.button_count += 1

    def remove_button(self):
        print("remove_button call.")
        self.data.remove_widget_at(self.ui_buttons_room, 0)
        self.button_count -= 1
