import docker 
from docker import DockerClient
from docker.errors import (
    DockerException, 
    NotFound, 
    APIError
)

from typing import Optional, Any, Literal

client = DockerClient.from_env()


class DockerServices():
    
    def create_service():
        pass
    