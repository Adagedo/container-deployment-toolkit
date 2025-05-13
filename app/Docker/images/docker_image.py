import docker 
from docker.errors import APIError, BuildError
from typing import Optional

# set up a client 

client = docker.DockerClient.from_env()

class DockerImageManagementService():
    
    
    def build(self, path:str) -> tuple:
        if path is None:
            return TypeError(f"file path is not specifies")
        try:
            image = client.images.build(path=path)
            return image
        except BuildError as ee:
            return BuildError
        except APIError as ee:
            return ee
    
    def get_image(self, name:str):
        try:
            image = client.images.get(name=name)
            return image
        except APIError as ee:
            return ee 
    
    def get_registry_data(self, name:str):
        
        try:
            data = client.images.get_registry_data(name=name)
            return data
        except APIError as ee:
            return ee
    def list_images(self, repository_name:str):
        try:
            images = client.images.list(name=repository_name)
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
        
    def pull_images(self, repository:str):
        try:
            image = client.images.pull(repository=repository)
            return image
        except APIError as ee:
            return ee
    
    def pull_all_images(self, repository):
        try:
            images = client.images.pull(repository=repository, all_tags=True)
            return images
        except APIError as ee:
            return ee
    
    
    def push_image(self, repository:str):
        try:
            server_response = client.images.push(repository=repository)
            return server_response
        except APIError as ee:
            return ee
        
    def remove(image:str):
        try:
            server_response = client.images.remove(image)
            return server_response
        except APIError as ee:
            return ee
        
    def remove_image_force(image:str):
    
        try:
            server_response = client.images.remove(image, force=True)
            return server_response
        except APIError as ee:
            return ee
        
    def remove_image_with_untagged_parents(image:str):
        try:
            server_response = client.images.remove(image=image, unprune=True)
            return server_response
        except APIError as ee:
            return ee
        
    def search_image(term:str, limit:int):
        try:
            response = client.images.search(term=term, limit=limit)
            return response 
        except APIError as ee:
            return ee
    
    