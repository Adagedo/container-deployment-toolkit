import docker 
from docker import DockerClient
from docker.errors import (
    APIError, 
    DockerException, 
    NotFound
    )
from typing import Optional, Any



class DockerPlugins():
    
    def __init__(self):
        
        self.client = DockerClient.from_env()
    
    def get_plugin(self, name:str):
        
        try:
            plugin = self.client.plugins.get(name=name)
            return plugin
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
    def install_plugins(self,remote_name:str, local_name:str):
        
        try:
            plugins = self.client.plugins.install(
                remote_name=remote_name, local_name=local_name
            )
            return plugins
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
    
    def list_plugins(self)-> list[str]:
        try:
            plugins:list[str] = self.client.plugins.list()
            return plugins
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
        
    def create_plugin(self, name:Optional[Any], plugin_data_dir:Optional[Any], gzip:Optional[bool]=False):
        
        try:
            new_plugin = self.client.plugins.create(
                name=name, plugin_data_dir=plugin_data_dir, gzip=gzip
            )
            return new_plugin
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
   
        
        
                