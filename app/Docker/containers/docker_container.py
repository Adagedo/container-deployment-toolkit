import docker 
clients = docker.DockerClient(base_url='unix://var/run/docker.sock')


class DockerContainerManagementService():
    
    def run_container(self):
        pass 
    
    def stop_container(self):
        pass 
    
    def inspect_container(self):
        pass
