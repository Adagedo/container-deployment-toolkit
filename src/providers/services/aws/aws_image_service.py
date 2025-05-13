# the image service

import boto3

client = boto3.client('ecr')

class AmazonImageRegistryProvider():
    
    def batch_check_layer_availability(self):
        pass
    
    def batch_delete_image(self):
        pass
    
    def batch_get_image(self):
        pass
    
    def batch_get_repository_scanning_configuration(self):
        pass
    
    def complete_layer_upload(self):
        pass
    
    def create_pull_through_cache_rule(self):
        pass
    
    def create_repository(self):
        pass
    
    def create_repository_creation_template(self):
        
        pass
    
    def delete_life_cycle_policy(self):
        pass
    
    def delete_pull_through_cache_rule(self):
        pass
    
    def delete_registry_rule(self):
        pass
    
    def delete_repository(self):
        pass
    
    def delete_repository_creation_template(self):
        pass
    
    def delete_repository_policy(self):
        pass
    
    def describe_image_replication_status(self):
        pass
    
    def describe_image(self):
        pass
    
    def describe_image_scan_finding(self):
        pass
    
    def describe_pull_through_cache_rule(self):
        pass
    
    def describe_registry(self):
        pass
    
    def describe_repositories(self):
        pass
    
    def describe_repository_creation_template(self):
        pass
    
    def get_account_setting(self):
        pass
    
    # might stand as the authentication gate way for us
    def get_authorization_token(self):
        pass
    
    def get_download_url_for_layer(self):
        pass
    
    def get_life_cycle_policy(self):
        pass
    
    def get_life_cycle_policy_preview(self):
        pass
    
    def get_registory_policy(self):
        pass
    
    def get_registry_scanning_configuration(self):
        pass
    
    def get_repository_policy(self):
        pass
    
    def initate_layer_upload(self):
        pass
    
    def list_images(self):
        pass 
    
    def list_tages_for_resource(self):
        pass
    
    def put_account_setting(self):
        pass
    
    def put_image(self):
        pass
    
    def put_imgage_scanning_configuration(self):
        pass
    
    def put_image_tage_mutability(self):
        pass
    
    def put_life_cycle_policy(self):
        pass
    
    def put_registry_policy(self):
        pass 
    
    def put_registory_scanning_configuration(self):
        pass 
    
    def put_replication_repository(self):
        pass
    
    def set_repository_policy(self):
        pass
    
    def start_image_scan(self):
        pass
    
    def start_life_cycle_policy_preview(self):
        pass
    
    def untage_resource(self):
        pass
    
    def update_pull_through_cache_rule(self):
        pass
    
    def update_repository_creation_template(self):
        pass
    
    def upload_layer_part(self):
        pass
    
    def validate_pull_through_cache_rule(self):
        pass
     

