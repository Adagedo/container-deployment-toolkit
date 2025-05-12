import boto3

client = boto3.client('ecs')

class AwsContainerProvider():

    def create_cluster(self):
        pass

    def create_capacity_provider(self):
        pass

    def can_paginate(self):
        pass
    
    def close(self):
        pass
    
    def create_service(self):
        pass
    
    def create_task_set(self):
        pass
    
    def delete_account_setting(self):
        pass
    def delete_attributes(self):
        pass
    
    def delete_capacity_provider(self):
        pass
    
    def delete_cluster(self):
        pass
    
    def delete_service(self):
        pass
    
    def delete_task_definations(self):
        pass
    
    def delete_task_set(self):
        pass
    
    def deregister_container_instance(self):
        pass
    
    
    def deregister_tast_definition(self):
        pass 
    
    def describe_capacity_provider(self):
        pass
    
    def describe_cluster(self):
        pass
    
    def describe_container_instances(self):
        pass
    
    def describe_service_deployments(self):
        pass 
    
    def describe_service_revision(self):
        pass
    
    def describe_service(self):
        pass
    def describe_task_definition(self):
        pass
    
    def describe_task_set(self):
        pass 
    
    def describe_task(self):
        pass
    
    def discover_poll_endpointer(self):
        pass 
    
    def execute_command(self):
        pass 
    
    def get_paginator(self):
        pass
    
    def get_task_protection(self):
        pass
    
    def get_waiter(self):
        pass
    
    def list_account_settings(self):
        pass
    
    def list_attributes(self):
        pass 
    
    def list_clusters(self):
        pass
    
    def list_container_instance(self):
        pass
    
    def list_service_deployment(self):
        pass
    
    def list_service(self):
        pass
    
    
    def list_service_by_namespace(self):
        pass
    
    def list_tags_for_resource(self):
        pass
    
    def list_task_definition_families(self):
        pass
    
    def list_task_definitions(self):
        pass
    
    def list_task(self):
        pass
    
    def put_account_setting(self):
        pass
    def put_account_setting_default(self):
        pass
    
    def put_attributes(self):
        pass
    
    def put_cluster_capacity_provider(self):
        pass 

    def register_container_instance(self):
        pass
    
    def register_task_definition(self):
        pass
    
    def run_task(self):
        pass
    
    def start_task(self):
        pass
    
    def stop_service_deployment(self):
        pass
    def stop_task(self):
        pass
    
    def submit_attachment_state_changes(self):
        pass 
    
    def submit_container_state_change(self):
        pass
    
    def submit_task_state_change(self):
        pass
    
    def tag_resource(self):
        pass
    
    def untage_resource(self):
        pass 
    
    def update_capacity_provider(self):
        pass
    
    def update_cluster(self):
        pass
    
    def update_cluster_settings(self):
        pass
    
    def update_container_agent(self):
        pass
    
    def update_container_instance_state(self):
        pass
    
    def update_service(self):
        pass
    
    def update_service_primary_task_set(self):
        pass
    
    def update_task_protection(self):
        pass

    def update_task(self):
        pass
    