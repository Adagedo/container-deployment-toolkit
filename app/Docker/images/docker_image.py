import docker 
from docker.errors import APIError, BuildError
from typing import Optional

# set up a client 

clients = docker.DockerClient.from_env()

class DockerImageManagementService():
    
    
    def build(self, path:str) -> tuple:
        if path is None:
            return TypeError(f"file path is not specifies")
        try:
            image = clients.images.build(path=path)
            return image
        except BuildError as ee:
            return BuildError
        except APIError as ee:
            return ee
        
    def build_with_queit_tag(quiet:dict):
        
        if quiet is None:
            return TypeError(f"file path is not specifies")
        try:
            image = clients.images.build(quiet=quiet)
            return image
        except BuildError as ee:
            return BuildError
        except APIError as ee:
            return ee
        
        
    
    
    