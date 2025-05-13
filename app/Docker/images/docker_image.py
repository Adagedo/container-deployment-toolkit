import docker 
from docker.errors import APIError, BuildError
from typing import Optional, Any

# set up a client 

client = docker.DockerClient.from_env()

class DockerImageManagementService():
    
    
    def build(
        self, 
        path:str,
        fileobj:Optional[dict]=None,
        tag:Optional[str]=None, quiet:Optional[bool]=None,
        nocache:Optional[bool]=None, rm:Optional[bool]=None,
        timeout:Optional[int]=None,custom_context:Optional[bool]=None,
        pull:Optional[bool]=None, 
        forcerm:Optional[bool]=None, encoding:Optional[str]=None,
        dockerfile:Optional[str]=None, buildargs:Optional[dict]=None, 
        container_limits:Optional[dict]=None,
        shmsize:Optional[int]=None, 
        labels:Optional[dict]=None, cache_from:Optional[list]=None,
        target:Optional[str]=None, squash:Optional[bool]=None, 
        network_mode:Optional[str]=None, extra_host:Optional[dict]=None,
        platforms:Optional[str]=None, isolation:Optional[str]=None,
        use_config_proxy:Optional[bool]=None
    ) -> tuple:
        if path is None:
            return TypeError(f"file path is not specifies")
        try:
            image = client.images.build(
                path=path,fileobj=fileobj, tag=tag, 
                nocache=nocache, timeout=timeout, pull=pull, quiet=quiet,
                rm=rm, custom_context=custom_context, forcerm=forcerm, encoding=encoding,
                dockerfile=dockerfile, buildargs=buildargs, container_limits=container_limits,
                shmsize=shmsize, labels=labels, cache_from=cache_from, target=target, 
                squash=squash, network_mode=network_mode, extra_hosts=extra_host,
                platform=platforms, use_config_proxy=use_config_proxy, isolation=isolation,
            )
            return image
        except BuildError as ee:
            return ee
        except APIError as ee:
            return ee
    
    def get_image(self, name:str):
        try:
            image = client.images.get(name=name)
            return image
        except APIError as ee:
            return ee 
    
    def get_registry_data(self, name:str, auth_config:Optional[dict]=None):
        
        try:
            data = client.images.get_registry_data(name=name, auth_config=auth_config)
            return data
        except APIError as ee:
            return ee
    def list_images(self, repository_name:str, all:Optional[bool]=None, filters:Optional[dict]=None):
        try:
            images = client.images.list(name=repository_name, all=all, filters=filters)
            return images
        except APIError as ee:
            return ee
    def load_image_previously_saved(self, data:any) -> list[str|int]:
        try:
            images = client.images.load(data=data)
            return images
        except APIError as ee:
            return ee
        
    def delete_unused_images(self)-> dict:
        try:
            response = client.images.prune(filters=None)
            return response 
        except APIError as ee:
            return ee
        
    def build_with_queit_tag(self, quiet:dict):
        
        if quiet is None:
            return TypeError(f"file path is not specifies")
        try:
            image = client.images.build(quiet=quiet)
            return image
        except APIError as ee:
            return ee
        
    def pull_images(
        self, repository:str, 
        tag:Optional[str]=None, 
        auth_config:Optional[dict]=None,
        platform:Optional[str]=None,
        all_tags:Optional[bool]=None
        
        ):
        try:
            image = client.images.pull(repository=repository)
            return image
        except APIError as ee:
            return ee
    
    
    def push_image(self, repository:str,tag:Optional[str]=None)->Any:
        try:
            server_response = client.images.push(
                repository=repository,
                tag=tag
                )
            return server_response
        except APIError as ee:
            return ee
        
    def remove_image(image:str, force:Optional[bool]=None, noprune:Optional[bool]=None):
        try:
            server_response = client.images.remove(image,force=force, noprun=noprune)
            return server_response
        except APIError as ee:
            return ee
        
    def remove_image_force(image:str):
    
        try:
            server_response = client.images.remove(image, force=True)
            return server_response
        except APIError as ee:
            return ee
        
        
    def search_image(term:str, limit:Optional[int]=None):
        try:
            response = client.images.search(term=term, limit=limit)
            return response 
        except APIError as ee:
            return ee
    
    