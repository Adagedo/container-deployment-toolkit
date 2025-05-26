import docker 
from docker import DockerClient
from docker.errors import (
    DockerException, 
    NotFound, 
    APIError
    )
from typing import Optional

class DockerSecretes():
    
    def __init__(self):
        
        self.client = DockerClient.from_env()
    
    def create_secrets(self, name:str, data:bytes,label:dict, driver):
        
        try:
            secrets_id = self.client.secrets.create(name=name, data=data, label=label, driver=driver)
            return secrets_id
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
    def get_secrete(self, secrets_id:str):
        
        try:
            secrets = self.client.secrets.get(secret_id=secrets_id)
            return secrets
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
    
    def list_secretes(self, filters:Optional[dict]=None)-> list:
        
        try:
            DockerSecretes = self.client.secrets.list()
            return DockerSecretes
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
    