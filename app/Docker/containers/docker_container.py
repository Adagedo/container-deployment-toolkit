import docker
from docker import DockerClient
from docker.errors import DockerException, ContainerError, ImageNotFound, APIError
from typing import Optional,Any
client = DockerClient.from_env()

class DockerContainerManagementService():
    
    def run_container(
        self, image:str, command:Optional[str|list]=None,
        auto_remove:Optional[bool]=None,blkio_weight_device:Optional[list[dict[str]]]=None,
        cap_add:Optional[list[str]]=None, cap_drop:Optional[list[str]]=None,
        cgroup_parent:Optional[str]=None, 
        cgroups:Optional[str]=None, 
        cpu_count:Optional[int]=None, cpu_percent:Optional[int|float]=None,
        cpu_period:Optional[int]=None, cpu_quota:Optional[int]=None, cpu_rt_runtime:Optional[int]=None,
        cpu_shares:Optional[int]=None, cpuset_cpus:Optional[str]=None, cpuset_mems:Optional[str]=None,
        detach:Optional[bool]=None, device_cgroups_rules:Optional[list]=None, 
        device_read_bps:Optional[list[dict[str]]]=None, device_read_iops:Optional[str|int|bool]=None,
        device_write_bps:Optional[str]=None, device_write_iops: Optional[str]=None,
        device:Optional[list]=None, device_request:Optional[list]=None, dns:Optional[list]=None, 
        dns_opt:Optional[list]=None, dns_search:Optional[list]=None, domainname:Optional[str|list]=None,
        entrypoint:Optional[str|list]=None, enviroment:Optional[dict[str]|list[str]]=None, 
        extra_hosts:Optional[dict[str]]=None, group_add:Optional[list]=None, healthcheck:Optional[dict]=None,
        hostname:Optional[str]=None, init_path:Optional[str]=None, ipc_mode:Optional[str]=None, 
        isolation:Optional[str]=None, kernel_memory:Optional[int|str]=None, label:Optional[dict|list]=None, 
        links:Optional[dict]=None, log_config:Optional[dict]=None, 
        lxc_conf:Optional[dict]=None, mac_address:Optional[str]=None, mem_limit:Optional[int|str]=None,
        mem_reservation:Optional[int|str]=None, mem_swappiness:Optional[int]=None, 
        memswap_limit:Optional[str|int]=None, mounts:Optional[list]=None, name:Optional[str]=None, 
        nano_cpus:Optional[int]=None, network:Optional[str]=None, network_dsiable:Optional[bool]=None,
        network_mode:Optional[str]=None, networking_config:Optional[dict[str,str]]=None, 
        oom_kill_disable:Optional[bool]=None, omm_score_adj:Optional[int]=None, pid_mode:Optional[str]=None, 
        pid_limit:Optional[int]=None, platform:Optional[str]=None, ports:Optional[dict]=None, privileged:Optional[bool]=None, 
        publish_all_ports:Optional[bool]=None, read_only:Optional[bool]=None, remove:Optional[bool]=None, 
        restat_policy:Optional[dict]=None, runtime:Optional[str]=None, security_opt:Optional[list]=None,
        shm_open:Optional[bool]=None, stdin_open:Optional[bool]=None, stdout:Optional[bool]=None, 
        stderr:Optional[bool]=None, stop_signal:Optional[str]=None, storage_opt:Optional[dict]=None,
        stream:Optional[bool]=None, sysctls:Optional[dict]=None, tmpfs:Optional[dict]=None, tty:Optional[bool]=None,
        ulimits:Optional[list]=None, use_config_proxy:Optional[bool]=None, user:Optional[str|int]=None, 
        userns_mode:Optional[str]=None, uts_mode:Optional[str]=None, version:Optional[str]=None,
        volume_driver:Optional[str]=None , volume:Optional[dict|list]=None, volume_from:Optional[list]=None, 
        working_dir:Optional[str]=None,  cpu_rt_period:Optional[dict]=None
    ):
        try: 
            container = client.containers.run(
                image=image, command=command, auto_remove=auto_remove, blkio_weight_device=blkio_weight_device, 
                cap_add=cap_add, cap_drop=cap_drop, cgroup_parent=cgroup_parent,cgroupns=cgroups, cpu_count=cpu_count, cpu_percent=cpu_percent,
                cpu_period=cpu_period, cpu_quota=cpu_quota, cpu_rt_runtime=cpu_rt_runtime, cpu_rt_period=cpu_rt_period
            )
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
