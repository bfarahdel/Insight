import symbl
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class symbl_api:
    def __init__(self):
        self.app_id = os.getenv("app_id")
        self.app_secret = os.getenv("app_secret")
    
    def audio_text(self, path):
    # Process audio file
        conversation_object = symbl.Audio.process_file(
        credentials={"app_id": self.app_id, "app_secret": self.app_secret},
        file_path=path)

        msg = []
        for response in conversation_object.get_messages().messages:
            msg.append(response.text)

        return msg