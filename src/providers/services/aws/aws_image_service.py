# the image service

import boto3

client = boto3.client('ecr')

class AmazonImageRegistryProvider():
    
    
    def create_repository(self, repository_name:str, registry_id:str, auth:any)->dict[str] | None:
        try:
            if auth:
                response = client.create_repository(
                registryId=registry_id,
                repositoryName= repository_name,
                tags=[
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                    imageTagMutability='MUTABLE'|'IMMUTABLE',
                    imageScanningConfiguration={
                    'scanOnPush': True|False
                },
                encryptionConfiguration={
                'encryptionType': 'AES256'|'KMS'|'KMS_DSSE',
                'kmsKey': 'string'
                })
            else:
                raise Exception("user not authenticated")
        except Exception as ee:
            raise Exception(ee)
            

        return response if auth is not False else None
    
    def batch_check_layer_availability(self, registryId:str, repository_name:str, auth:any) -> dict[str]:
        try:
            if auth:
                response = client.batch_check_layer_availability(
                registryId='string',
                repositoryName='string',
                layerDigests=[
                    'string',
                    ]
                )
                return response
            else:
                raise Exception("not authenticated")
        except Exception as ee:
            return ee
        
        
    def batch_delete_image(self, registry_id:str, repository_name:str, auth:bool) -> dict[str]:
        try:
            if auth:
                response = client.batch_delete_image(
                registryId='string',
                repositoryName='string',
                imageIds=[
                        {
                        'imageDigest': 'string',
                        'imageTag': 'string'
                        },
                    ]   
                )
                return response
            else:
                raise Exception("auth error")
        except Exception as ee:
            return ee
    
    def batch_get_image(self, registry_id:str, repository_name:str, auth:bool)-> dict[str]:
        try:
            if auth:
                response = client.batch_get_image(
                registryId='string',
                repositoryName='string',
                imageIds=[
                    {
                        'imageDigest': 'string',
                        'imageTag': 'string'
                    },
                ],
                    acceptedMediaTypes=[
                        'string',
                    ]
                )
            else:
                raise Exception("exception")
        except Exception as ee:
            return ee 

