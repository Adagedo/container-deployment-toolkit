# import the google sdk for the api integration with python
from google.auth import exceptions
import google as gg

class GoogleServiceMangement():
    
    def __init__(self):
        pass
    
    def create_registry(self, registry_name:str, registry_id:str, auth:any)->None:
        try:
            if auth:
                """create the registry if use is authenticatde"""
                pass
            raise exceptions.GoogleAuthError()
        except Exception as ee:
            raise exceptions.DefaultCredentialsError() if not auth else print(ee)
           
            
             