from docker import DockerClient
from docker.errors import DockerException, APIError
from typing import Optional
from config.docker.docker_config import update_config

def docker_client_authentication(username:str, password:str, registry:str="https://index.docker.io/v1/") -> Optional[DockerClient]:
    try:
        client = DockerClient.from_env()
        response = client.login(username=username, password=password, registry=registry)
        print(f"login successfull:{response.get('Username')}")
        update_config(config_data=response)
        return client if response else None 
    except APIError as ee:
        print(f"docker login failed:{ee.explanation}")
    except DockerException as ee:
        print(f"docker error:{ee}")
    except Exception as e:
        print(f"unexpected error during login:{e}")

def isAuthenticated()->bool:
    pass
    
    
