import docker 
from docker import DockerClient
from docker.errors import (
    DockerException, NotFound, APIError
)

from typing import( 
    Optional
    )

client = DockerClient.from_env()


class DockerVolume():
    
    
    def create_volume(self, name:str, driver:Optional[str]=None, driver_opts:Optional[dict]=None, labels:Optional[dict]=None):
        try:
            volumes = client.volumes.create(name=name, driver=driver, driver_opts=driver_opts, labels=labels)
            return volumes
        
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
        
    def get_volumes(volume_id:str):
        
        try:
            volume = client.volumes.get(volume_id=volume_id)
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
            
            volumes = client.volumes.list(filters=filters)
            return volumes
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
        
    def delete_unused_volumes(filters:Optional[dict]=None):
        try:
            response = client.volumes.prune(filters=filters)
            return response 
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
            