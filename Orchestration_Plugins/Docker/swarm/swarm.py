import docker 
from docker import DockerClient
from docker.errors import (
    DockerException, NotFound, APIError
)

from typing import Optional, Any, Iterable




class DockerSwarm():

    def __init__(self):
        self.client = DockerClient.from_env()
    
    def initialise_swarm(
            self, 
            advertise_addr:Optional[str]=None, listen_addr:Optional[str]="0.0.0.0:2377",
            force_new_cluster:Optional[bool]=False, default_addr_pool:Iterable[str]=None, 
            subnet_size:Optional[int]=None, data_path_port:Optional[str]=None, data_path_addr:Optional[str]=None,
    )-> str:
        
        try:
            response = self.client.swarm.init(
                advertise_addr=advertise_addr,listen_addr=listen_addr, 
                force_new_cluster=force_new_cluster, default_addr_pool=default_addr_pool, 
                subnet_size=subnet_size, data_path_addr=data_path_addr, data_path_port=data_path_port
                )
            return response
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
    
    def join_swarm(
        self,
        remote_addr:Iterable[str]=None, join_token:Optional[str]=None, 
        listen_addr:Optional[str]="0.0.0.0:2377", advertise_addr:Optional[str]=None, 
        data_path_addr:Optional[str]=None
    )-> bool:
        
        try:
            response = self.client.swarm.join(
                remote_addr=remote_addr, join_token=join_token, listen_addr=listen_addr, 
                advertise_addr=advertise_addr, data_path_addr=data_path_addr
            )
            return response
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
        
    def leave_swarm(self, force:Optional[bool]=False)-> bool:
        
        try:
            response = self.client.swarm.leave(force=force)
            return response
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
    def unlock_swarm(self, key:Optional[str])-> bool:
        
        try:
            response = self.client.swarm.unlock(key=key)
            return response
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
    def get_unlock_key(self)-> dict:
        
        try:
            key = self.client.swarm.get_unlock_key()
            return key
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
    
    def update_swarm(
            self,
            rotate_worker_token:Optional[bool]=False, rotate_manager_token:Optional[bool]=False, 
            rotate_manager_unlock_key:Optional[bool]=False
        ):
        
        try:
            response = self.client.swarm.update(rotate_manager_token=rotate_manager_token, 
                rotate_manager_unlock_key=rotate_manager_unlock_key, rotate_worker_token=rotate_worker_token
                )
            return response
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        
    def reload_swarm(self):
        
        try:
            if self.client.swarm.version:
                response = self.client.swarm.reload()
                return response
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee