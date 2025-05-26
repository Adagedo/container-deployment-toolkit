import docker 
from docker import DockerClient
from docker.errors import (
    DockerException, NotFound, APIError
)

from typing import( 
    Optional
    )




class DockerVolume():
    
    def __init__(self):
        
        self.client = DockerClient.from_env()
    
    
    def create_volume(self, name:str, driver:Optional[str]=None, driver_opts:Optional[dict]=None, labels:Optional[dict]=None):
        try:
            volumes = self.client.volumes.create(name=name, driver=driver, driver_opts=driver_opts, labels=labels)
            return volumes
        
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
        
    def get_volumes(self, volume_id:str):
        
        try:
            volume = self.client.volumes.get(volume_id=volume_id)
            return volume
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
    
    def list_volumes(self, filters:Optional[dict]=None):
        
        try:
            
            volumes = self.client.volumes.list(filters=filters)
            return volumes
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
        
    def delete_unused_volumes(self, filters:Optional[dict]=None):
        try:
            response = self.client.volumes.prune(filters=filters)
            return response 
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
            