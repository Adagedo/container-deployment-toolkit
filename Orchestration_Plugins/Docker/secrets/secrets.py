import docker 
from docker import DockerClient
from docker.errors import (
    DockerException, 
    NotFound, 
    APIError
    )
from typing import Optional

client = DockerClient.from_env()

class DockerSecretes():
    
    def create_secrets(name:str, data:bytes,label:dict, driver):
        
        try:
            secrets_id = client.secrets.create(name=name, data=data, label=label, driver=driver)
            return secrets_id
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
    def get_secrete(secrets_id:str):
        
        try:
            secrets = client.secrets.get(secret_id=secrets_id)
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
    
    def list_secretes(filters:Optional[dict]=None)-> list:
        
        try:
            DockerSecretes = client.secrets.list()
            return DockerSecretes
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
    