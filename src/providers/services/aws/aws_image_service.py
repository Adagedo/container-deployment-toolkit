# the image service

import boto3
from typing import Optional,Iterable


class AmazonImageRegistryProvider():
    
    def __init__(self):
        
        self.client =  boto3.client('ecr')
        
        
    def batch_check_layer_availability(self, 
        registry_id:Optional[str]=None, 
        repositoryName:Optional[str]=None, 
        layerDigest:Iterable[str]=None)->dict[str,list[dict[str,str]]]|dict[str]:
        
        try:
            response = self.client.batch_check_layer_availability(
                registryId=registry_id,
                repositoryName=repositoryName,
                layerDigest=layerDigest
            )
            
            return response 
        except Exception as e:
            return e
        

    
    def batch_delete_image(self,registry_id:Optional[str]=None, repositoryName:Optional[str]=None, ImageIds:Iterable[str]=None)->dict[str]:
        
        try:
            response = self.client.batch_delete_image(
                registryId=registry_id, 
                repositoryName=repositoryName, 
                ImageIds=ImageIds
            )
            
            return response 
        except Exception as e:
            return e
    
    def batch_get_image(self,registry_id:Optional[str]=None, 
        repositoryName:Optional[str]=None, 
        ImageIds:Iterable[str]=None)->dict[str]:
        
        
        try:
            
            response = self.client.batch_get_image(
                registryId=registry_id, 
                repositoryName=repositoryName, 
                ImageIds=ImageIds
            )
            
            return response
        except Exception as e:
            return e 
        
        
    
    def batch_get_repository_scanning_configuration(self, repositoryNames:Iterable[str])->dict[str]:
        
        try:
            
            response = self.client.batch_get_repository_scanning_configuration(
                repositoryNames=repositoryNames
            )
            return response 
        except Exception as e:
            return e
        
    def complete_layer_upload(
        self, registryId:Optional[str]=None, 
        repositoryName:Optional[str]=None, 
        uploadId:Optional[str]=None, 
        layerDigests:Iterable[str]=None
        )->dict[str]:
        
        try:
            
            response = self.client.complete_layer_upload(
                registryId=registryId, 
                respositoryName=repositoryName, 
                uploadId=uploadId, 
                layerDigests=layerDigests
            )
            
            return response 
        
        except Exception as e:
            return e
        
    
    def create_pull_through_cache_rule(
        self,
        ecrRepositoryPrefix:Optional[str]=None, 
        upstreamRegistryUrl:Optional[str]=None, 
        registryId:Optional[str]=None, 
        upstreamRegistry:Optional[str]='ecr'|'ecr-public'|'quay'|'k8s'|'docker-hub'|'github-container-registry'|'azure-container-registry'|'gitlab-container-registry'|None,
        credentialArn:Optional[str]=None, 
        upstreamRepositoryPrefix:Optional[str]=None
    )->dict[str]:
        
        try:
            
            response = self.client.create_pull_through_cache_rule(
                
            )
            return response 
        except self.client.exceptions.ServerException as e:
            return e
        except self.client.exceptions.InvalidParameterExceptions as e:
            return e
        except self.client.exceptions.ValidationException as e:
            return e
        except self.client.exceptions.PullThroughCacheRuleAlreadyExistsException as e:
            return e 
        except self.client.exceptions.UnsupportedUpstreamRegistryException as e:
            return e
        except self.client.exceptions.LimitExceededException as e:
            return e
        except self.client.exceptions.UnableToAccessSecretException as e:
            return e
        except self.client.exceptions.SecretNotFoundException as e:
            return e
        except self.client.exceptions.UnableToDecryptSecretValueException as e:
            return e
        
    
    def create_repository(
        self, 
        registryId:Optional[str]=None, 
        repositoryName:Optional[str]=None, 
        tags:Iterable[dict[str]]=None, 
        imageTagMutability:Optional[str]= "MUTABLE" | "IMMUTABLE"|None,
        imageScanningConfiguration:Optional[dict[str, bool]]={"scanOnPush":True|False},
        encryptionConfiguration:Optional[dict[str,str]]={"encryptionType":"AES256"|"KMS"|"KMS_DSSE", "kemKey":str},
    )-> dict[str]:
        try:
            
            response = self.client.create_repository(
                registryId=registryId, 
                repositoryName=repositoryName, 
                tags=tags, 
                imageTagMutability=imageTagMutability, 
                encryptionConfiguration=encryptionConfiguration, 
                imageScanningConfiguration=imageScanningConfiguration
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e:
            return e 
        except self.client.exceptions.InvalidParameterException as e:
            return e 
        except self.client.exceptions.InvalidTagParameterException as e:
            return e
        except self.client.exceptions.TooManyTagsException as e:
            return e
        except self.client.exceptions.RepositoryAlreadyExistsException as e:
            return e
        except self.client.exceptions.LimitExceedeException as e:
            return e
        except self.client.exceptions.KmsException as e:
            return e
        
    def create_repository_creation_template(
        self, 
        prefix:Optional[str]=None, 
        description:Optional[str]=None, 
        imageTagMutability:Optional[str]= "MUTABLE" | "IMMUTABLE"|None,
        encryptionConfiguration:Optional[dict[str,str]]={"encryptionType":"AES256"|"KMS"|"KMS_DSSE", "kemKey":str},
        resourceTags:Iterable[list[dict[str, str]]]=None, 
        repositoryPolicy:Optional[str]=None, 
        lifeCyclePolicy:Optional[str]=None, 
        appliedFor:Optional[Iterable[str]]=["REPLICATION"|"PULL_THROUGH_CACHE"],
        customRoleArn:Optional[str]=None, 
        
)->dict[str]:
        
        try:
            
            response = self.client.create_repository_creation_template(
                prefix=prefix,
                description=description,
                encryptionConfiguration=encryptionConfiguration,
                imageTagMutability=resourceTags,
                repositoryPolicy=repositoryPolicy,
                lifecyclePolicy=lifeCyclePolicy,
                appliedFor=appliedFor,
                customRoleArn=customRoleArn
            )
            return response 
        except self.client.exceptions.ServerExcetion as e:return e
        except self.client.exceptions.Validationxception as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.LimitExceededException as e:return e
        except self.client.TemplateAlreadyExistsException as e:return e

    
    def delete_lifecycle_policy(
        self, 
        registryId:Optional[str]=None, 
        repositoryName:Optional[str]=None,
        )->dict[str]:
        
        try:
            response = self.client.delete_lifecycle_policy(
                registryId=registryId,
                repositoryName=repositoryName
            )
            return response 
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.RepositoryNotFoundException as e:return e
        except self.client.exceptions.LifecyclePolicyFoundException as e: return e
        except self.client.exceptions.ValidationException as e:return e
        
    def delete_pull_through_cache_rule(
        self,
        ecrRepositoryPrefix:Optional[str]=None, 
        registryId:Optional[str]=None
        )-> dict[str]:
        
        try:
            response = self.client.delete_pull_through_cache_rule(
                ecrRepositoryPrefix=ecrRepositoryPrefix,
                registryId=registryId,
            )
            
            return response 
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.PullThroughCacheRuleNotFoundException as e:return e
        except self.client.exceptions.ValidationException as e:return e
        
    
    def delete_registry_rule(self):
            
        pass
    def delete_registry_policy(self):
        try:
            response =self.client.delete_registry_policy()
            return response 
        except self.client.exceptions.RegistryPolicyNotFoundException as e:return e
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ValidationException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
    def delete_repository(
        self,
        registryId:Optional[str]=None, 
        repositoryName:Optional[str]=None, 
        force:Optional[bool]=False
        )-> dict:
        
        try:
            
            response = self.client.delete_repository(
                registryId=registryId,
                repositoryName=repositoryName,
                force=force
            )
            
            return response 
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
        except self.client.exceptions.RepositoryNotEmptyException as e: return e
        except self.client.exceptions.KmsException as e: return e
    
    def delete_repository_creation_template(self, prefix:Optional[str]=None)->dict[str]:
        try:
            
            response = self.client.delete_repository_creation_template(
                prefix=prefix
            )
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.ValidationException as e: return e
        except self.client.exceptions.TemplateNotFound as e: return e
        
        
    def delete_repository_policy(self, registryId:Optional[str]=None, repositoryName:Optional[str]=None)->dict[str]:
        
        try:
            response = self.client.delete_repository_policy(
                registryId=registryId, 
                repositoryName=repositoryName
            )
            return response 
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
        except self.client.exceptions.RepositoryPolicyNotFoundException as e: return e
    
    
    def describe_image_replication_status(self, registryId:Optional[str]=None,repositoryName:Optional[str]=None, imageId:Optional[dict[str, str]]=None)->dict[set]:
        
        try:
            
            response = self.client.describe_image_replication_status(
                repositoryName=repositoryName, 
                imageId=imageId, 
                registryId=registryId
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
        except self.client.exceptions.ValidationException as e: return e
        except self.client.exceptions.ImageNotFoundException as e: return e
        
    
    def describe_image(self):
        pass
    
    def describe_image_scan_finding(
        self,
        registryId:Optional[str]=None, 
        repositoryName:Optional[str]=None, 
        imageId:Optional[dict]=None, 
        nextToken:Optional[str]=None, 
        maxResult:Optional[str]=None
        )-> dict[str]:
        
        try:
            response = self.client.describe_image_scan_findings(
                registryId=registryId, 
                respositoryName=repositoryName, 
                imageId=imageId, 
                nextToken=nextToken, 
                maxResults=maxResult
            )
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
        except self.client.exceptions.ScanNotFoundException as e: return e
        except self.client.exceptions.ImageNotFoundException as e: return e
        except self.client.exceptions.ValidationException as e: return e
        pass
    
    def describe_pull_through_cache_rule(
        self,
        registryId:Optional[str]=None, 
        ecrRepositoryPrefixses:Iterable[str]=None, 
        nextToken:Optional[str]=None, 
        maxResults:Optional[str]=None
        )->dict:
        
        try:
            response = self.client.describe_pull_through_cache_rules(
                registryId=registryId, 
                ecrRepositoryPrefixses=ecrRepositoryPrefixses, 
                nextToken=nextToken, 
                maxResults=maxResults
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.PullThroughCacheRuleNotFoundException as e :return e
        except self.client.exceptions.ValidationException as e: return e
    
    def describe_registry(self):
        pass
    
    
    def describe_repositories(
        self, 
        registryId:Optional[str]=None, 
        repositoryNames:Iterable[str]=None,
        nextToken:Optional[str]=None, 
        maxResults:Optional[int]=None
    )-> dict[str]:
        
        try:
            response = self.client.describe_repositories(
                registryId=registryId, 
                repositoryNames=repositoryNames, 
                nextToken=nextToken, 
                maxResults=maxResults
            )
            
            return response
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
  
    
    def describe_repository_creation_template(
        self, 
        prefixes:Iterable[str]=None, 
        nextToken:Optional[str]=None, 
        maxResults:Optional[int]=None
    )->dict[str]:
        
        try:
            
            response = self.client.describe_repository_creation_templates(
                prefixes=prefixes, 
                maxResults=maxResults, 
                nextToken=nextToken
            )
            
            
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.ValidationException as e: return e
    
    def get_account_setting(self, name:Optional[str]=None):
        try:
            response = self.client.get_account_setting(
                name=name
            )
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.ValidationException as e: return e
    
    # not again
    def get_authorization_token(self, registryIds:Iterable[str]=None):
        
        try:
            
            response = self.client.get_authorization_token(
                registryIds=registryIds
            )
            return response 
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e

    
    def get_download_url_for_layer(
        self, 
        registryId:Optional[str]=None, 
        repositoryName:Optional[str]=None, 
        layerDigest:Optional[str]=None
    )->dict[str]:
        
        try:
            response = self.client.get_download_url_for_layer(
                registryId=registryId, 
                repositoryName=repositoryName,
                layerDigest=layerDigest
            )
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
        except self.client.exceptions.LayerNotFoundException as e: return e
        except self.client.exceptions.UnableToGetUpstreamLayerException as e: return e
        except self.client.exceptions.LayerInaccessibleException as e: return e
    
    def get_lifecycle_policy(self, registryId:Optional[str]=None, repositoryName:Optional[str]=None):
        
        try:
            response = self.client.get_lifecycle_policy(
                registryId=registryId, 
                repositoryName=repositoryName
            )
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
        except self.client.exceptions.LifecycleNotFoundException as e: return e
        except self.client.exceptions.ValidationException as e: return e

    
    def get_life_cycle_policy_preview(
        self,
        registryId:Optional[str]=None, 
        repositoryName:Optional[str]=None, 
        imageIds:Iterable[str]=None, 
        nextToken:Optional[str]=None, 
        maxResults:Optional[int]=None, 
        filter:Optional[dict[str]]={'tagStatus': 'TAGGED'|'UNTAGGED'|'ANY'}
        )->dict[str]:
        
        try:
            
            response = self.client.get_lifecycle_policy_preview(
                registryId=registryId, 
                repositoryName=repositoryName, 
                imageIds=imageIds,
                nextToken=nextToken, 
                maxResults=maxResults,
                filter=filter
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
        except self.client.exceptions.LifecyclePolicyPreviewNotFound as e: return e
        except self.client.exceptions.ValidationException as e: return e
        
    def get_paginator(self, opt_name:Optional[str]=None):
        try:
           response = self.client.get_paginator(
                operation_name=opt_name
            )
           return response 
        except Exception as e:return e
    def get_registory_policy(self):
        try:
            
            response = self.client.get_registry_policy()
            return response 
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryPolicyNotFoundException as e :return e
        except self.client.exceptions.ValidationException as e: return e
        pass
    
    def get_registry_scanning_configuration(self):
        try:
            response = self.client.get_registry_scanning_configuration()
            return response 
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.ValidationException as e: return e
    
    def get_repository_policy(self, registryId:Optional[str]=None, repositoryName:Optional[str]=None)->dict[str]:
        
        try:
            
            response = self.client.get_repository_policy(
                registryId=registryId, 
                repositoryName=repositoryName
            )
            return response
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
        except self.client.exceptions.RepositoryPolicyNotFoundException as e: return e

        
        
    def initate_layer_upload(self, registryId:Optional[str]=None, repositoryName:Optional[str]=None)->dict[str]:
        
        try:
            
            response = self.client.initiate_layer_upload(
                registryId=registryId, 
                repositoryName=repositoryName
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
        except self.client.exceptions.KmsExceptions as e: return e
        
    
    def list_images(
        self,
        registryId:Optional[str]=None, 
        repositoryName:Optional[str]=None, 
        imageIds:Iterable[str]=None, 
        nextToken:Optional[str]=None, 
        maxResults:Optional[int]=None, 
        filter:Optional[dict[str]]={'tagStatus': 'TAGGED'|'UNTAGGED'|'ANY'}
    )->dict[str]:
        
        try:
            
            response = self.client.list_images(
                registryId=registryId, 
                repositoryName=repositoryName, 
                imageIds=imageIds,
                nextToken=nextToken, 
                maxResults=maxResults,
                filter=filter
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
    
        
    def list_tags_for_resource(self, resourceArn:Optional[str]=None):
        
        try:
            response = self.client.list_tags_for_resource(
                resourceArn=resourceArn
            )
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e

      
    
    def put_account_setting(self, name:Optional[str]=None, value:Optional[str]=None)->dict[str]:
        
        try:
            
            response = self.client.put_account_setting(
                name=name, 
                value=value
            )
            return response
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
        except self.client.exceptions.LimitExceededException as e: return e
        
    
    def put_image(
        self,
        registryId:Optional[str]=None,
        repositoryName:Optional[str]=None,
        imageManifest:Optional[str]=None,
        imageManifestMediaType:Optional[str]=None,
        imageTag:Optional[str]=None,
        imageDigest:Optional[str]=None,
        
    )->dict[str]:
        
        try:
            
            response = self.client.put_image(
                    registryId=registryId,
                    repositoryName=repositoryName,
                    imageManifest=imageManifest,
                    imageManifestMediaType=imageManifestMediaType,
                    imageTag=imageTag,
                    imageDigest=imageDigest
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
        except self.client.exceptions.LimitExceededException as e: return e
        except self.client.exceptions.ImageAlreadyExistsException as e: return e
        except self.client.exceptions.LayersNotFoundException as e: return e
        except self.client.exceptions.ImageTagAlreadyExistsException as e: return e
        except self.client.exceptions.KmsException as e: return e
        except self.client.exceptions.ImageDigestDoesNotMatchException as e: return e
        
        
    
    def put_image_scanning_configuration(
            self,
            registryId:str,
            repositoryName:str,
            imageScanningConfiguration:Optional[dict[str,bool]]=None
        )->dict[str]:
        
        try:
            
            response = self.client.put_image_scanning_configuration(
                registryId=registryId, 
                repositoryName=repositoryName,
                imageScanningConfiguration=imageScanningConfiguration
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
        except self.client.exceptions.ValidationException as e: return e

        
        
        
        pass
    
    def put_image_tage_mutability(
        self,    
        registryId:str,
        repositoryName:str,
        imageTagMutability:Optional[str]='MUTABLE'|'IMMUTABLE'
        ):
        
        try:
            
            response = self.client.put_image_tag_mutability(
                registryId=registryId
                repositoryName=repositoryName,
                imageTagMutability=imageTagMutability
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
     
    
    def put_life_cycle_policy(
        self,
        registryId:Optional[str]=None,
        repositoryName:Optional[str]=None,
        lifecyclePolicyText:Optional[str]=None
        )->dict[str]:
        
        try:
            
            response = self.client.put_lifecycle_policy(
                registryId=registryId,
                repositoryName=repositoryName,
                lifecyclePolicyText=lifecyclePolicyText
            )
            
            return response 
        
        except self.client.exceptions.InvalidParameterException as e: return e
        except self.client.exceptions.ServerException as e :return e
        except self.client.exceptions.ValidationException as e :return e
        except self.client.exceptions.RepositoryNotFoundException as e :return e
    
    def put_registry_policy(self, policy_test:str):
        try:
            response = self.client.put_registry_policy(
                policyText=policy_test
            )
            
            return response 
        except self.client.exceptions.ServerException as e: return e
        except self.client.exceptions.InvalidParameterException as e :return e 
        except self.client.exceptions.ValidationException as e :return e 
    
    
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
     

