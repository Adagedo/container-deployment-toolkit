import docker 
from docker import DockerClient
from typing import Optional
from docker.errors import APIError, NotFound

class Network():
    pass 


class DockerNetWorkManagementSystem():
    
    def __init__(self):
        self.client = DockerClient.from_env()

    
    def create_network(
        self,
        name:str, 
        driver:str,
        chech_duplicate:Optional[bool]=None,
        internal:Optional[bool]=None,
        labels:Optional[dict]=None,
        enabel_ipv6:Optional[bool]=False,
        attachable:Optional[bool]=None,
        scope:Optional[str] = "local"|"global"|"swarm",
        ingress:Optional[bool]=None
    )-> Network:
        try:
            
            network_response = self.client.networks.create(
                name=name, driver=driver, check_duplicate=chech_duplicate,
                internal=internal, labels=labels, enable_ipv6=enabel_ipv6, 
                attachable=attachable,
                scope=scope,ingress=ingress
            )
            
            return network_response
        except APIError as ee:
            return ee
    
    
    def get_network(
        self,
        network_id:str, verbose:Optional[bool]=None,
        scope:Optional[str] = "local"|"global"|"swarm", 
    )-> Network:
        try:
            response = self.client.networks.get(
                network_id=network_id, 
               verbose=verbose, 
               scope=scope                           
            )
            return response
            
        except NotFound as ee:
            return ee
        except APIError as ee:
            return ee
        
    def list_network(
        self,
        names:Optional[list[str]]=None, 
        ids:Optional[list[str]]=None,
        filters:Optional[dict[str]]=None,
        greedy:Optional[bool]=None
    )-> list[Network]:
        try:
            networks = self.client.networks.list(
                names=names, 
                ids=ids,
                filters=filters,
                greedy=greedy
            )
            return networks
        except APIError as ee:
            return ee
        
    def delete_unused_network(self, filters:Optional[dict]=None)-> dict[str,any|any, str]:
        try:
            response = self.client.networks.prune(filters=filters)
            return response 
        except APIError as ee:
            return ee
        
            
        