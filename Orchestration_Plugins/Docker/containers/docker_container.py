import docker
from docker import DockerClient
from docker.errors import DockerException, ContainerError, ImageNotFound, APIError
from typing import Optional,Any, Literal
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
        isolation:Optional[str]=None, kernel_memory:Optional[int|str]=None, labels:Optional[dict|list]=None, 
        links:Optional[dict]=None, log_config:Optional[dict]=None, 
        lxc_conf:Optional[dict]=None, mac_address:Optional[str]=None, mem_limit:Optional[int|str]=None,
        mem_reservation:Optional[int|str]=None, mem_swappiness:Optional[int]=None, 
        memswap_limit:Optional[str|int]=None, mounts:Optional[list]=None, name:Optional[str]=None, 
        nano_cpus:Optional[int]=None, network:Optional[str]=None, network_dsiable:Optional[bool]=None,
        network_mode:Optional[str]=None, networking_config:Optional[dict[str,str]]=None, 
        oom_kill_disable:Optional[bool]=None, omm_score_adj:Optional[int]=None, pid_mode:Optional[str]=None, 
        pid_limit:Optional[int]=None, platform:Optional[str]=None, ports:Optional[dict]=None, privileged:Optional[bool]=None, 
        publish_all_ports:Optional[bool]=None, read_only:Optional[bool]=None, remove:Optional[bool]=False, 
        restart_policy:Optional[dict]=None, runtime:Optional[str]=None, security_opt:Optional[list]=None,
        shm_size:Optional[bool]=None, stdin_open:Optional[bool]=None, stdout:Optional[bool]=True, 
        stderr:Optional[bool]=False, stop_signal:Optional[str]=None, storage_opt:Optional[dict]=None,
        stream:Optional[bool]=None, sysctls:Optional[dict]=None, tmpfs:Optional[dict]=None, tty:Optional[bool]=None,
        ulimits:Optional[list]=None, use_config_proxy:Optional[bool]=None, user:Optional[str|int]=None, 
        userns_mode:Optional[str]=None, uts_mode:Optional[str]=None, version:Optional[str]=None,
        volume_driver:Optional[str]=None , volume:Optional[dict|list]=None, volume_from:Optional[list]=None, 
        working_dir:Optional[str]=None,  cpu_rt_period:Optional[dict]=None
    ):
        try: 
            container = client.containers.run(
                image=image, command=command, auto_remove=auto_remove, blkio_weight_device=blkio_weight_device, 
                cap_add=cap_add, cap_drop=cap_drop, cgroup_parent=cgroup_parent,cgroupns=cgroups, cpu_count=cpu_count, cpu_percent=cpu_percent,cpuset_mems=cpuset_mems,
                cpu_period=cpu_period, cpu_quota=cpu_quota, cpu_rt_runtime=cpu_rt_runtime, cpu_rt_period=cpu_rt_period,cpu_shares=cpu_shares, cpuset_cpus=cpuset_cpus, 
                detach=detach, device_cgroup_rules=device_cgroups_rules, device_read_bps=device_read_bps, device_write_bps=device_write_bps, device_write_iops=device_write_iops, 
                devices=device, device_requests=device_request, dns=dns, dns_opt=dns_opt, dns_search=dns_search, domainname=domainname, entrypoint=entrypoint, environment=enviroment, 
                extra_hosts=extra_hosts, group_add=group_add, healthcheck=healthcheck, hostname=hostname, init_path=init_path, ipc_mode=ipc_mode,isolation=isolation, kernel_memory=kernel_memory, 
                labels=labels, links=links, log_config=log_config, lxc_conf=lxc_conf, mac_address=mac_address, mem_limit=mem_limit, mem_reservation=mem_reservation, mem_swappiness=mem_swappiness,
                memswap_limit=memswap_limit, mounts=mounts,name=name, nano_cpus=nano_cpus, network=network, network_disabled=network_dsiable, network_mode=network_mode, networking_config=networking_config, 
                oom_kill_disable=oom_kill_disable, oom_score_adj=omm_score_adj, pid_mode=pid_mode, pids_limit=pid_limit, privileged=privileged, platform=platform, ports=ports, publish_all_ports=publish_all_ports,
                read_only=read_only, remove=remove, restart_policy=restart_policy, runtime=runtime, security_opt=security_opt, shm_size=shm_size, stdin_open=stdin_open, stdout=stdout, stderr=stderr, 
                stop_signal=stop_signal, storage_opt=storage_opt, stream=stream, sysctls=sysctls, tmpfs=tmpfs, tty=tty, ulimits=ulimits, use_config_proxy=use_config_proxy, user=user, userns_mode=userns_mode, 
                uts_mode=uts_mode, version=version, volume_driver=volume_driver, volumes=volume,  volumes_from=volume_from, working_dir=working_dir
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
        
    def create_container(
        self, image:str, command:str, port:Optional[int]=None,auto_remove:Optional[bool]=None,blkio_weight_device:Optional[list[dict[str]]]=None,
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
        isolation:Optional[str]=None, kernel_memory:Optional[int|str]=None, labels:Optional[dict|list]=None, 
        links:Optional[dict]=None, log_config:Optional[dict]=None, 
        lxc_conf:Optional[dict]=None, mac_address:Optional[str]=None, mem_limit:Optional[int|str]=None,
        mem_reservation:Optional[int|str]=None, mem_swappiness:Optional[int]=None, 
        memswap_limit:Optional[str|int]=None, mounts:Optional[list]=None, name:Optional[str]=None, 
        nano_cpus:Optional[int]=None, network:Optional[str]=None, network_dsiable:Optional[bool]=None,
        network_mode:Optional[str]=None, networking_config:Optional[dict[str,str]]=None, 
        oom_kill_disable:Optional[bool]=None, omm_score_adj:Optional[int]=None, pid_mode:Optional[str]=None, 
        pid_limit:Optional[int]=None, platform:Optional[str]=None, ports:Optional[dict]=None, privileged:Optional[bool]=None, 
        publish_all_ports:Optional[bool]=None, read_only:Optional[bool]=None,
        restart_policy:Optional[dict]=None, runtime:Optional[str]=None, security_opt:Optional[list]=None,
        shm_size:Optional[bool]=None, stdin_open:Optional[bool]=None,
        stop_signal:Optional[str]=None, storage_opt:Optional[dict]=None,
        stream:Optional[bool]=None, sysctls:Optional[dict]=None, tmpfs:Optional[dict]=None, tty:Optional[bool]=None,
        ulimits:Optional[list]=None, use_config_proxy:Optional[bool]=None, user:Optional[str|int]=None, 
        userns_mode:Optional[str]=None, uts_mode:Optional[str]=None, version:Optional[str]=None,
        volume_driver:Optional[str]=None , volume:Optional[dict|list]=None, volume_from:Optional[list]=None, 
        working_dir:Optional[str]=None,  cpu_rt_period:Optional[dict]=None
        
        ) -> dict[str] | str:
        try:
            container = client.containers.create(
                image=image, command=command, ports=port, auto_remove=auto_remove, blkio_weight_device=blkio_weight_device, 
                cap_add=cap_add, cap_drop=cap_drop, cgroup_parent=cgroup_parent,cgroupns=cgroups, cpu_count=cpu_count, cpu_percent=cpu_percent,cpuset_mems=cpuset_mems,
                cpu_period=cpu_period, cpu_quota=cpu_quota, cpu_rt_runtime=cpu_rt_runtime, cpu_rt_period=cpu_rt_period,cpu_shares=cpu_shares, cpuset_cpus=cpuset_cpus, 
                detach=detach, device_cgroup_rules=device_cgroups_rules, device_read_bps=device_read_bps, device_write_bps=device_write_bps, device_write_iops=device_write_iops, 
                devices=device, device_requests=device_request, dns=dns, dns_opt=dns_opt, dns_search=dns_search, domainname=domainname, entrypoint=entrypoint, environment=enviroment, 
                extra_hosts=extra_hosts, group_add=group_add, healthcheck=healthcheck, hostname=hostname, init_path=init_path, ipc_mode=ipc_mode,isolation=isolation, kernel_memory=kernel_memory, 
                labels=labels, links=links, log_config=log_config, lxc_conf=lxc_conf, mac_address=mac_address, mem_limit=mem_limit, mem_reservation=mem_reservation, mem_swappiness=mem_swappiness,
                memswap_limit=memswap_limit, mounts=mounts,name=name, nano_cpus=nano_cpus, network=network, network_disabled=network_dsiable, network_mode=network_mode, networking_config=networking_config, 
                oom_kill_disable=oom_kill_disable, oom_score_adj=omm_score_adj, pid_mode=pid_mode, pids_limit=pid_limit, privileged=privileged, platform=platform, ports=ports, publish_all_ports=publish_all_ports,
                read_only=read_only,restart_policy=restart_policy, runtime=runtime, security_opt=security_opt, shm_size=shm_size, stdin_open=stdin_open,
                stop_signal=stop_signal, storage_opt=storage_opt, stream=stream, sysctls=sysctls, tmpfs=tmpfs, tty=tty, ulimits=ulimits, use_config_proxy=use_config_proxy, user=user, userns_mode=userns_mode, 
                uts_mode=uts_mode, version=version, volume_driver=volume_driver, volumes=volume,  volumes_from=volume_from, working_dir=working_dir
            
            )
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
        
    
    def list_container_before(
        
        self, since:str=None,
        all:Optional[bool]=False,
        before:Optional[str]=None,
        limit:Optional[int]=None, filters:Optional[dict]=None, 
        sparse:Optional[bool]=False, ignore_removed:Optional[bool]=False
        ):
        try:
            containers = client.containers.list(
                all=all, since=since, 
                before=before, limit=limit, filters=filters, 
                sparse=sparse, ignore_removed=ignore_removed
                )
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
