from docker import DockerClient
from docker.errors import DockerException, APIError


def docker_client_authentication(username:str, password:str, registry:str="https://index.docker.io/v1/") -> DockerClient:
    try:
        client = DockerClient.from_env()
        response = client.login(username=username, password=password, registry=registry)
        print(f"login successfull:{response.get('Username')}")
        return client 
    except APIError as ee:
        print(f"docker login failed:{ee.explanation}")
    except DockerException as ee:
        print(f"docker error:{ee}")
    except Exception as e:
        print(f"unexpected error during login:{e}")
    

