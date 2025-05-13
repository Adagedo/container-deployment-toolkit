import docker
from docker import DockerClient
from docker.errors import DockerException, ContainerError, ImageNotFound, APIError

client = DockerClient.from_env()

class DockerContainerManagementService():
    
    def run_container(self, image:str, command:str):
        try:
            container = client.containers.run(image=image,command=command)
            return container
        except DockerException as ee:
            return ee
        except ContainerError as ee:
            return ee
        except ImageNotFound as ee:
            return ee
        except APIError as ee:
            return ee
        
        
    
    def run_container_detach(self, image:str, command:str, detach:bool):
        try:
            container = client.containers.run(image=image, command=command, detach=detach)
            return container.logs()
        except Exception as ee:
            return ee
        except DockerException as ee:
            return ee
        except ContainerError as ee:
            return ee 
        except ImageNotFound as ee:
            return ee
        except APIError as ee:
            return ee
        
        
        
    def create_container(self, image:str, command:str) -> dict[str] | str:
        try:
            container = client.containers.create(image=image, command=command)
            return container
        except Exception as ee:
            return ee 
        except DockerException as ee:
            return ee
        except APIError as ee:
            return ee
        except ImageNotFound as ee:
            return ee
        
    def get_container_by_id(self, id:str)-> dict[str]:
        try:
            container = client.containers.get(container_id=id)
            return container
        except Exception as ee:
            return ee
        except DockerException as ee:
            return ee
        except ContainerError as ee:
            return ee 
        except ImageNotFound as ee:
            return ee
        except APIError as ee:
            return ee
        
    def list_running_containers(self):
        try:
            containers = client.containers.list(all=True)
            return containers
        except Exception as ee:
            return ee
        except DockerException as ee:
            return ee
        except ContainerError as ee:
            return ee 
        except ImageNotFound as ee:
            return ee
        except APIError as ee:
            return ee
        
    
    def list_container_before(self, since:str):
        try:
            containers = client.containers.list(all=True, since=since)
            return containers
        except Exception as ee:
            return ee
        except DockerException as ee:
            return ee
        except ContainerError as ee:
            return ee 
        except ImageNotFound as ee:
            return ee
        except APIError as ee:
            return ee
        
    def list_last_created_containers(limit:int):
        try:
            containers = client.containers.list(limit=limit)
            return containers
        except Exception as ee:
            return ee
        except DockerException as ee:
            return ee
        except ContainerError as ee:
            return ee 
        except ImageNotFound as ee:
            return ee
        except APIError as ee:
            return ee

    def delete_stopped_container(self)-> dict[int|str]:
        try:
            containers = client.containers.prune()
            return containers
        except Exception as ee:
            return ee
        except DockerException as ee:
            return ee
        except ContainerError as ee:
            return ee 
        except ImageNotFound as ee:
            return ee
        except APIError as ee:
            return ee
