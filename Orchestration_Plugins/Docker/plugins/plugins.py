import docker 
from docker import DockerClient
from docker.errors import (
    APIError, 
    DockerException, 
    NotFound
    )
from typing import Optional, Any

client = DockerClient.from_env()

class DockerPlugins():
    
    
    def get_plugin(self, name:str):
        
        try:
            plugin = client.plugins.get(name=name)
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
            plugins = client.plugins.install(
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
            plugins:list[str] = client.plugins.list()
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
            new_plugin = client.plugins.create(
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
   
        
        
                