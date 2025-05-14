import docker 
from docker import DockerClient
from docker.errors import APIError
from typing import Optional

client = DockerClient.from_env()

class Node():
    pass 




class DockerNodeManagementSystem():
    
    def get_node_by_id_or_name(self, name:Optional[str]=None, id:Optional[str]=None):
        
        try:
            node = client.nodes.get(node_id=name|id)
            return node 
        except APIError as ee:
            return ee
        
    def list_node(self, filter:Optional[dict[str]])-> list[Node]:
        try:
            list_of_nodes = client.nodes.list(filters=filter)
            return list_of_nodes
        except APIError as ee:
            return ee
        

        