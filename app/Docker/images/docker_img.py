import docker 
# set up a client 

clients = docker.DockerClient(base_url="unix://var/run/docker.sock")