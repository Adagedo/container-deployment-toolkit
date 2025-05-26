import docker 
from docker import DockerClient
from docker.errors import (
    DockerException, 
    NotFound, 
    APIError, 
    InvalidVersion
)
from Orchestration_Plugins.Docker.swarm.swarm import DockerSwarm
from typing import (Optional, Any, Literal, Iterable)


request_swarm = DockerSwarm()
class DockerServices():
    
    def __init__(self):
        
        self.client = DockerClient.from_env()
    
    def create_service(
        self, image:str, command:Optional[str|Iterable[str]]=None, 
        args:Iterable[str]=None, constraints:Iterable[str]=None, 
        preferences:Iterable[tuple]=None, maxreplicas:Optional[int]=None, 
        platforms:Iterable[tuple]=None, container_labels:Optional[dict]=None, 
        endpoint_spec:Optional[Any]=None, env:Iterable[str]=None, hostname:Optional[str]=None,
        init:Optional[bool]=False, isolation:Optional[str]=None, labels:Optional[dict]=None, 
        log_driver:Optional[str]=None, log_driver_options:Optional[dict]=None, mode:Optional[Any]=None, 
        mounts:Iterable[str]=None, name:Optional[str]=None, networks:Iterable[str|int]=None,
        resources:Optional[Any]=None, 
        restart_policy:Optional[Any]=None, secrets:Iterable[str]=None, 
        stop_grace_period:Optional[int]=None, updata_config:Optional[Any]=None, 
        rollback_config:Optional[Any]=None, user:Optional[str]=None,workdir:Optional[str]=None, 
        tty:Optional[bool]=False, open_stdin:Optional[bool]=False, read_only:Optional[bool]=False, 
        stop_signal:Optional[str]=None, healthcheck:Optional[Any]=None, host:Optional[dict]=None, 
        dns_config:Optional[Any]=None, configs:Iterable[Any]=None, 
        ):
        
        try:
            request_swarm.initialise_swarm()
            services = self.client.services.create(
                image=image, command=command, args=args, 
                constraints=constraints, preferences=preferences, 
                maxreplicas=maxreplicas, platforms=platforms, container_labels=container_labels, 
                endpoint_spec=endpoint_spec, env=env, hostname=hostname, init=init, 
                isolation=isolation, labels=labels,log_driver=log_driver, log_driver_options=log_driver_options, mounts=mounts, 
                name=name, networks=networks, resources=resources, restart_policy=restart_policy, secrets=secrets, mode=mode, 
                stop_grace_period=stop_grace_period, updata_config=updata_config, rollback_config=rollback_config, user=user, open_stdin=open_stdin, 
                read_only=read_only, workdir=workdir, stop_signal=stop_signal, healthcheck=healthcheck, host=host, dns_config=dns_config, configs=configs 
            )
            
            return services
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
            
    
    def get_service(self, service_id:str, insert_defaults:Optional[bool]=False):
        
        try:
            request_swarm.initialise_swarm()
            service = self.client.services.get(service_id=service_id, insert_defaults=insert_defaults)
            return service
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
        except InvalidVersion as ee:
            return ee
        
    def list_services(self, filters:Optional[dict]=None, status:Optional[bool]=None):
        
        try:
            request_swarm.initialise_swarm()
            service = self.client.services.list(filters=filters, status=status)
            return service
        except Exception as ee:
            return ee 
        except APIError as ee:
            return ee
        except DockerException as ee:
            return ee
        except NotFound as ee:
            return ee
            
    