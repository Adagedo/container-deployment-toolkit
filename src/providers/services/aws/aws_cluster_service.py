"""the kubernetes cluster servixe"""

import boto3
from typing import Optional
import typing
class AmazonK8Actions():
    
    def __init__(self):
        self.client =  boto3.client('eks')
    
    def AssociateAccessPolicy(
        self,
        clusterName:str, 
        principalArn:str, 
        policyArn:str,
        accessScope:dict[str, str]
        )->dict[str, str]:
        
        try:
            response = self.client.associate_access_policy(
                clusterName=clusterName, 
                principalArn=principalArn, 
                policyArn=policyArn, 
                accessScope=accessScope
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        
    
    def AssociateEncryptionPolicyConfig(self, clusterName:str, encryptionConfig:list[dict])->dict:
        
        try:
            response = self.client.associate_encryption_config(
                clusterName=clusterName, 
                encryptionConfig=encryptionConfig
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ThrottlingException as e:return e
        except self.client.exceptions.ResourceInUseExceptions as e:return e
        
        
    
    def AssociateIdentityProviderConfig(
        self, 
        clusterName:str, 
        oidc:dict[str, str], 
        tags:str, 
        clientRequestToken:str, 
        )->dict[str]:
        
        try:
            
            response = self.client.associate_identity_provider_config(
                clusterName=clusterName, 
                oidc=oidc, 
                tags=tags, 
                clientRequestToken=clientRequestToken
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ThrottlingException as e:return e
        except self.client.exceptions.ResourceInUseExceptions as e:return e
        
    def close(self):
        try:
            self.client.close()
            print("closing connection...")
        except Exception as e: return e
            
            
    def CreateAccessEntry(
        self, 
        clusterName:str, 
        principalArn:Optional[str]=None, 
        kubernetesGroups:typing.Iterable[str]=None, 
        tags:typing.Optional[dict]=None, 
        clientRequestToken:Optional[str]=None, 
        username:Optional[str]=None, 
        type:Optional[str]=None, 
        )->dict:
        
        try:
            
            response = self.client.create_access_entry(
                clusterName=clusterName, 
                principalArn=principalArn, 
                kubernetesGroups=kubernetesGroups, 
                tags=tags,clientRequestToken=clientRequestToken,
                username=username   
            )
            
            return response
        
                
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ThrottlingException as e:return e
        except self.client.exceptions.ResourceInUseExceptions as e:return e
        
    
    def CreateAddon(
        self,
        clusterName:Optional[str]=None,
        addonName:Optional[str]=None,
        addonVersion:Optional[str]=None,
        serviceAccountRoleArn:Optional[str]=None,
        resolveConflicts:Optional[str]='OVERWRITE'|'NONE'|'PRESERVE',
        clientRequestToken:Optional[str]=None,
        configurationValues:Optional[str]=None,
        podIdentityAssociations:Optional[dict]=None
        )->dict:
        
        try:
            
            response = self.client.create_addon(
                clusterName=clusterName, 
                addonName=addonName,
                addonVersion=addonVersion,
                serviceAccountRoleArn=serviceAccountRoleArn,
                resolveConflicts=resolveConflicts,
                clientRequestToken=clientRequestToken,
                configurationValues=configurationValues,
                podIdentityAssociations=podIdentityAssociations
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ThrottlingException as e:return e
        except self.client.exceptions.ResourceInUseExceptions as e:return e
        
        
    
    def CreateCluster(
        self, 
        name:Optional[str]=None, 
        version:Optional[str]=None,
        roleArn:Optional[str]=None,
        resourcesVpcConfig:Optional[dict]=None,
        kubernetesNetworkConfig:Optional[dict]=None,
        logging:Optional[dict]=None, 
        clientRequestToken:Optional[str]=None, 
        tags:Optional[dict]=None, 
        encryptionConfiglist:Optional[dict]=None,
        outpostConfig:Optional[dict]=None,
        accessConfig:Optional[dict]=None,
        bootstrapSelfManagedAddons:Optional[bool]=None,
        upgradePolicy:Optional[dict]=None, 
        zonalShiftConfig:Optional[dict]=None,
        remoteNetworkConfig:Optional[dict]=None,
        computeConfig:Optional[dict]=None,
        storageConfig:Optional[dict]=None,
        )-> dict:
        
        try:
            
            response = self.client.create_cluster(
                name=name, 
                version=version, 
                roleArn=roleArn,
                resourcesVpcConfig=resourcesVpcConfig,
                kubernetesNetworkConfig=kubernetesNetworkConfig,
                logging=logging,
                clientRequestToken=clientRequestToken,
                tags=tags,
                encryptionConfiglist=encryptionConfiglist,
                outpostConfig=outpostConfig,
                accessConfig=accessConfig,
                bootstrapSelfManagedAddons=bootstrapSelfManagedAddons,
                upgradePolicy=upgradePolicy,
                zonalShiftConfig=zonalShiftConfig,
                remoteNetworkConfig=remoteNetworkConfig,
                computeConfig=computeConfig,
                storageConfig=storageConfig   
            )
            
            return response
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ThrottlingException as e:return e
        except self.client.exceptions.ResourceInUseExceptions as e:return e
        
    
    def CreateEKsAnyWhereSubscription(
        self, 
        name:Optional[str]=None, 
        term:Optional[dict]=None,
        licenseQuantity:Optional[int]=None, 
        licenseType:Optional[str]=None, 
        autoRenew:Optional[bool]=False, 
        clientRequestToken:Optional[str]=None, 
        tags:Optional[dict]=None
        )->dict:
        
        try:
            
            response = self.client.create_eks_anywhere_subscription(
                name=name, 
                term=term, 
                licenseQuantity=licenseQuantity,
                licenseType=licenseType,
                autoRenew=autoRenew,
                clientRequestToken=clientRequestToken,
                tags=tags
            )
            
            return response
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ResourceLimitExceededException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ServiceUnavailableException as e:return e
        
    
    def CreateFargateProfile(
        self, 
        fargateProfileName:Optional[str]=None, 
        clusterName:Optional[str]=None, 
        podExecutionRoleArn:Optional[str]=None, 
        subnets:typing.Iterable[str]=None, 
        selectors:typing.Iterable[dict]=None, 
        clientRequestToken:Optional[str]=None, 
        tags:Optional[dict]=None
        )->dict:
        
        try:
            
            response = self.client.create_fargate_profile(
                fargateProfileName=fargateProfileName,
                clusterName=clusterName,
                podExecutionRoleArn=podExecutionRoleArn,
                subnets=subnets,
                selectors=selectors ,
                clientRequestToken=clientRequestToken, 
                tags=tags
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ResourceLimitExceededException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.UnsupportedAvailabilityZoneException as e:return e
    
    def CreateNodeGroup(
        self,
        clusterName:Optional[str]=None, 
        nodegroupName:Optional[str]=None, 
        scalingConfig:Optional[dict]=None,
        diskSize:Optional[int]=None, 
        subnet:typing.Iterable[str]=None, 
        instanceTypes:typing.Iterable[str]=None, 
        amiType:Optional[str]='AL2_x86_64'|'AL2_x86_64_GPU'|'AL2_ARM_64'|'CUSTOM'|'BOTTLEROCKET_ARM_64'|'BOTTLEROCKET_x86_64'|'BOTTLEROCKET_ARM_64_FIPS'|'BOTTLEROCKET_x86_64_FIPS'|'BOTTLEROCKET_ARM_64_NVIDIA'|'BOTTLEROCKET_x86_64_NVIDIA'|'WINDOWS_CORE_2019_x86_64'|'WINDOWS_FULL_2019_x86_64'|'WINDOWS_CORE_2022_x86_64'|'WINDOWS_FULL_2022_x86_64'|'AL2023_x86_64_STANDARD'|'AL2023_ARM_64_STANDARD'|'AL2023_x86_64_NEURON'|'AL2023_x86_64_NVIDIA'|'AL2023_ARM_64_NVIDIA',
        remoteAccess:Optional[dict]=None, 
        nodeRole:Optional[str]=None, 
        labels:Optional[dict]=None, 
        taints:typing.Iterable[dict]=None, 
        tags:Optional[dict]=None, 
        clientRequestToken:Optional[str]=None, 
        launchTemplate:Optional[dict]=None,
        updateConfig:Optional[dict]=None, 
        nodeRepairConfig:Optional[dict[str, bool]]=None, 
        capacityType:Optional[str]='ON_DEMAND'|'SPOT'|'CAPACITY_BLOCK',
        version:Optional[str]=None, 
        releaseVersion:Optional[str]=None
        )-> dict:
        
        try:
            response = self.client.create_nodegroup(
                clusterName=clusterName,
                nodegroupName=nodegroupName,
                scalingConfig=scalingConfig,
                diskSize=diskSize,
                subnet=subnet,
                instanceTypes=instanceTypes,
                amiType=amiType,
                remoteAccess=remoteAccess,
                nodeRole=nodeRole,
                labels=labels,
                taints=taints,
                tags=tags,
                clientRequestToken=clientRequestToken,
                launchTemplate=launchTemplate,
                updateConfig=updateConfig,
                nodeRepairConfig=nodeRepairConfig,
                capacityType=capacityType,
                version=version,releaseVersion=releaseVersion
            )

            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ResourceLimitExceededException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ServiceUnavailableException as e:return e
        except self.client.exceptions.ResourceInUseException as e:return e
    
    def CreatePodIdentityAssociation(
        self,
        clusterName:Optional[str]=None,
        namespace:Optional[str]=None,
        serviceAccount:Optional[str]=None,
        roleArn:Optional[str]=None, 
        clientRequestToken:Optional[str]=None, 
        tags:Optional[dict]=None
        )-> dict:

        try:

            response = self.client.create_pod_identity_association(
                clusterName=clusterName,
                namespace=namespace,
                serviceAccount=serviceAccount,
                roleArn=roleArn,
                clientRequestToken=clientRequestToken,
                tags=tags
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ResourceLimitExceededException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ResourceInUseException as e:return e

    
    def DeleteAccessEntry(
        self,
        clusterName:Optional[str]=None, 
        principalArn:Optional[str]=None        
        )->dict:
        
        try:
            response = self.client.delete_access_entry(
                clusterName=clusterName, 
                principalArn=principalArn
            )
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e

        
        pass
    
    def DeleteAddon(self, clusterName:Optional[str]=None, addonName:Optional[str]=None, preserve:Optional[str]=None)->dict:
        try:
            
            response = self.client.delete_addon(
                clusterName=clusterName, 
                addonName=addonName, 
                preserve=preserve
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
    
    def DeleteCluster(self, name:str)->dict:
        try:
            response = self.client.delete_cluster(name=name)
            return response 
        except Exception as e: return e
    
    def DeleteEKsAnyWhereSubscription(self, id:str)->dict:
        try:
            
            response = self.client.delete_eks_anywhere_subscription(
                id=id
            )
            
            return response
           
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
        
    
    def DeleteFragateProfile(self, clusterName:str, fargateProfileName:str)->dict:
        
        try:
            
            response = self.client.delete_fragate_profile(
                clusterName=clusterName, 
                fargateProfileName=fargateProfileName
            )
            
            return response
        
                   
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
        
    
    def DeleteNodeGroup(self, clusterName:str, nodegroupName:str)->dict:
        
        try:
            response = self.client.delete_nodegroup(
                clusterName=clusterName, 
                nodegroupName=nodegroupName
            )
            return response
                   
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ResourceInUseException as e:return e
        except self.client.exceptions.ServiceUnavailableException as e:return e
    
    def DeletePodIdentityAssociation(self, clustername:str, associationId:str)->dict:
        
        try:
            
            res = self.client.delete_pod_identity_association(
                clusterName=clustername, 
                associationId=associationId
            )
            return res
        
                           
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
        
    
    def DeregisterCluster(self, name:str)->dict:
        try:
            res = self.client.deregister_cluster(name=name)
            return res
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ServiceUnavailableException as e:return e
        except self.client.exceptions.AccessDeniedException as e:return e
        except self.client.exceptions.ClientException as e:return e
        
        
        
    def DescribetAccessEntry(self, clusterName:str, principalArn:str)->dict:
        try:
            
            res = self.client.describe_access_entry(
                clusterName=clusterName, 
                principalArn=principalArn
            )
            return res
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        
    
    def DescribeAddon(self, clusterName:str, addonName:str)->dict:
        
        try:
            res = self.client.describe_addon(
                clusterName=clusterName, 
                addonName=addonName
            )
            return res
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
    
    def DescribeAddonConfiguration(self, addonName:str, addonVersion:str)->dict:
        
        try:
            response = self.client.describe_addon_configuration(
                addonName=addonName, 
                addonVersion=addonVersion
            )
            
            return response
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        
    
    def DescribeAddonVersions(
        self,
        kubernetesVersion:Optional[str]=None, 
        maxResult:Optional[int]=None, 
        nextToken:Optional[str]=None, 
        addonName:Optional[str]=None, 
        types:typing.Iterable[str]=None, 
        publishers:typing.Iterable[str]=None, 
        owners:typing.Iterable[str]=None
        )->dict:
        
        try:
            
            response = self.client.describe_addon_versions(
                kubernetesVersion=kubernetesVersion,
                maxResult=maxResult,
                nextToken=nextToken,
                addonName=addonName,
                types=types,
                publishers=publishers,
                owners=owners
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        
        
    def DescribeCluster(self, name:str)->dict:
        
        try:
            response = self.client.describe_cluster(name=name)
            
            return response
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ServiceUnavailableException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
    
    def DescribeClusterVersions(
        self,
        clusterType:Optional[str]=None,
        maxResults:Optional[str]=None, 
        nextToken:Optional[str]=None, 
        defaultOnly:Optional[bool]=True|False,
        includeAll:Optional[bool]=True|False,
        status:Optional[str]='unsupported'|'standard-support'|'extended-support',
        versionStatus:Optional[str]='UNSUPPORTED'|'STANDARD_SUPPORT'|'EXTENDED_SUPPORT',
        clusterVersions:typing.Iterable[str]=None
        
    )->dict:
        try:
            
            res = self.client.describe_cluster_versions(
                clusterType=clusterType,
                maxResults=maxResults,
                nextToken=nextToken,
                defaultOnly=defaultOnly,
                includeAll=includeAll,
                status =status ,
                versionStatus=versionStatus,
                clusterVersions=clusterVersions
            )
            
            return res
        
               
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        
    def DescribeEKsAnyWhereSubscription(self, id:str)->dict:
        
        try:
            
            response = self.client.describe_eks_anywhere_subscription(id=id)
            return response
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ServiceUnavailableException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        
        
    
    def DescribeFargateProfile(self, clusterName:str, fargateProfileName:str)->dict:
        try:
            
            response = self.client.describe_fargate_profile(
                clusterName=clusterName,
                fargateProfileName=fargateProfileName
            )
            
            return response 
        
                
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ServiceUnavailableException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
    
    def DescribeIdentityProviderConfig(self, clusterName:str, identityProviderCconfig:dict)->dict:
        
        try:
            
            response = self.client.describe_identity_provider_config(
                clusterName=clusterName, 
                identityProviderCconfig=identityProviderCconfig
            )
            
            return response
        
                        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ServiceUnavailableException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        
        
    def DescribeInsight(self, clusterName:str, id:str)->dict:
        
        try:
            response = self.client.describe_insight(
                clusterName=clusterName, 
                id=id
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        
    
    def DescribeNodeGroup(self, clusterName:str, nodegroupName:str)->dict:
        
        try:
            
            response = self.client.describe_nodegroup(
                clusterName=clusterName, 
                nodegroupName=nodegroupName
            )
            return response 
        
                
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ServiceUnavailableException as e:return e
        
    
    def DescribePodIdentityAssociation(self, clusterName:str, associationId:str)->dict:
        
        try:
            
            response = self.client.describe_pod_identity_association(
                clusterName=clusterName, 
                associationId=associationId
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        
    
    def DescribeUpdate(
        self,
        name:str,
        updateId:str,
        nodegroupName:Optional[str]=None,
        addonName:Optional[str]=None
        )->dict:
        
        try:
            
            response = self.client.describe_update(
                name=name,
                updateId=updateId,
                nodegroupName=nodegroupName,
                addonName=addonName
            )
            
            return response
        
                
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
    
    def DisassociateAccessPolicy(
        self,
        clusterName:str,
        principalArn:str,
        policyArn:str
        )->dict:
        
        try:
            
            response = self.client.disassociate_access_policy(
                clusterName=clusterName,
                principalArn=principalArn,
                policyArn=policyArn
            )
            
            return response
        
                        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        
    
    def DisassociateIdentityProviderConfig(
        self,
        clusterName:str,
        identityProviderCconfig:dict, 
        clientRequestToken:Optional[str]=None, 
        )->dict:
        
        try:
            
            response = self.client.disassociate_identity_provider_config(
                clusterName=clusterName, 
                identityProviderCconfig=identityProviderCconfig, 
                clientRequestToken=clientRequestToken
            )
            return response
        
                            
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ThrottlingException as e:return e
        
        
    
    def ListAccessEntries(
        self,
        clusterName:str,
        associatedPolicyArn:str,
        maxResults:Optional[int]=None,
        nextToken:Optional[str]=None    
        )->dict:
        
        try:
            
            response = self.client.list_access_entries(
                clusterName=clusterName, 
                associatedPolicyArn=associatedPolicyArn,
                nextToken=nextToken,
                maxResults=maxResults
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
    
        
        
    
    def ListAccessPolicies(self, maxResult:int, nextToken:str)->dict:
        
        try:
            response = self.client.list_access_policies(
                maxResult=maxResult,
                nextToken=nextToken
            )
            
            return response 
         
        except self.client.exceptions.ServerException as e:return e
        
    def ListAddons(
        self,
        clusterName:str,
        maxResults:int, 
        nextToken:str
        )->dict:
        
        try:
            response = self.client.list_addons(
                clusterName=clusterName, 
                maxResult=maxResults,
                nextToken=nextToken
            )
            return response
        
                
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
        
    
    def ListAssociateAccessPolicies(
        self,
        clusterName:str,
        principalArn:str,
        maxResults:Optional[int]=None,
        nextToken:Optional[str]=None,
        )->dict:
        
        try:
            
            response = self.client.list_associated_access_policies(
                clusterName=clusterName,
                principalArn=principalArn,
                maxResults=maxResults,
                nextToken=nextToken
            )
            
            return response
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
    
    def ListCluster(self, maxResults:Optional[int]=None, nextToken:Optional[str]=None, include:typing.Iterable[str]=None)->dict:
        
        try:
            
            response = self.client.list_clusters(
                maxResults=maxResults,
                nextToken=nextToken,
                include=include
            )
            
            return response 
        
                
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ServiceUnavailableException as e:return e
    
    def ListEKsAnyWhereSubscriptions(self,maxResults:int, nextToken:str, includeStatus:typing.Iterable[str]=['CREATING'|'ACTIVE'|'UPDATING'|'EXPIRING'|'EXPIRED'|'DELETING'])->dict:
        
        try:
            response = self.client.list_eks_anywhere_subscriptions(
                maxResults=maxResults,
                nextToken=nextToken,
                includeStatus=includeStatus
            )
            
            return response 
        
                        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ServiceUnavailableException as e:return e
    
    def ListFargteProfiles(self, clusterName:str, maxResults:Optional[int]=1,nextToken:Optional[str]=None)->dict:
        
        try:
            
            response = self.client.list_fargate_profiles(
                clusterName=clusterName,
                maxResults=maxResults,
                nextToken=nextToken
            )
            
            return response
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        
    def ListIdentityProviderConfig(self, clusterName:str, maxResults:Optional[int]=1,nextToken:Optional[str]=None)->dict:
        
        try:
            response = self.client.list_identity_provider_configs(
                clusterName=clusterName,
                maxResults=maxResults,
                nextToken=nextToken
            )
            
            return response
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ServiceUnavailableException as e:return e
    
    def ListInsights(self,clusterName:str, filter:Optional[dict], maxResults:Optional[int]=1, nextToken:Optional[str]=None)->dict:
        
        try:
            response = self.client.list_insights(
                clusterName=clusterName,
                maxResults=maxResults,
                nextToken=nextToken
            )
            
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        

    def ListNodeGroupsg(self, clusterName:str, maxResults:Optional[int]=1,nextToken:Optional[str]=None)->dict:
        
        try:
            
            response = self.client.list_nodegroups(
                clusterName=clusterName,
                maxResults=maxResults,
                nextToken=nextToken
            )
            
            return response 
        
                
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ServiceUnavailableException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
            
        
    
    def ListPodIdentityAssociation(
        self,
        clusterName:str,
        namespace:Optional[str]=None,
        serviceAccount:Optional[str]=None, 
        maxResults:Optional[int]=1,
        nextToken:Optional[str]=None
        )->dict:
        
        try:
            
            response = self.client.list_pod_identity_associations(
                clusterName=clusterName,
                namespace=namespace,
                serviceAccount=serviceAccount,
                maxResults=maxResults,
                nextToken=nextToken
            )
            
            return response 
        
                        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        
    
    def ListTagsForResource(self, resourceArn:str)->dict:
        
        try:
            
            response = self.client.list_tags_for_resource(resourceArn=resourceArn)
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.BadRequestException as e:return e
        except self.client.exceptions.NotFoundException as e:return e
  
        
    def ListUpdates(self,
        name:str,
        nodegroupName:Optional[str]=None,
        addonName:Optional[str]=None,
        nextToken:Optional[str]=None,
        maxResults:Optional[int]=1
        ):
        
        try:
            
            response = self.client.list_updates(
                name=name, 
                nodegroupName=nodegroupName,
                addonName=addonName, 
                nextToken=nextToken, 
                maxResults=maxResults
            )
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
    
    def RegisterCluster(self, name:str, connectorConfig:Optional[dict]=None, clientRequestToken:Optional[str]=None, tags:Optional[dict]=None)->dict:
        
        try:
            response = self.client.register_cluster(
                name=name, 
                connectorConfig=connectorConfig,
                clientRequestToken=clientRequestToken,
                tags=tags
            )
            return response 
        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceLimitExceededException as e:return e
        except self.client.exceptions.ServiceUnavailableException as e:return e
        except self.client.exceptions.AccessDeniedException as e:return e
        except self.client.exceptions.ResourceInUseException as e:return e
        except self.client.exceptions.ResourcePropagationDelayException as e:return e
        
        
    
    
    def TagResource(self, resourceArn:str, tags:dict)->dict:
        try:
            response = self.client.tag_resource(
                resourceArn=resourceArn,
                tags=tags
            )
            
            return response
        
                
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.BadRequestException as e:return e
        except self.client.exceptions.NotFoundException as e:return e
                
    def UnTagResource(self, resoourceArn:str, tagKeys:list)->dict:
        
        try:
            response = self.client.untag_resource(
                resresoourceArn=resoourceArn,
                tagKeys=tagKeys
            )
            
            return response 
        
                        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.BadRequestException as e:return e
        except self.client.exceptions.NotFoundException as e:return e
    
    def UpdateAccessEntry(self, clusterName:str, principalArn:str, kubernetesGroups:typing.Iterable[str]=None, clientRequestToken:Optional[str]=None, username:Optional[str]=None)->dict:
        
        try:
            
            response = self.client.update_access_entry(
                clusterName=clusterName,
                principalArn=principalArn,
                kubernetesGroups=kubernetesGroups,
                clientRequestToken=clientRequestToken,
                username=username
            )
            
            return response 
        
                
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
    
    def UpdateAddon(
        self,
        clusterName:str, 
        addonName:str,
        addonVersion:Optional[str]=None, 
        serviceAccountRoleArn:Optional[str]=None, 
        resolveConflicts:Optional[str]='OVERWRITE'|'NONE'|'PRESERVE',
        clientRequestToken:Optional[str]=None, 
        configurationValues:Optional[str]=None, 
        podIdentityAssociations:typing.Iterable[dict]=None
        )->dict:
        
        try:
            
            response = self.client.update_addon(
                clusterName=clusterName,
                addonName=addonName,
                serviceAccountRoleArn=serviceAccountRoleArn,
                addonVersion=addonVersion,
                resolveConflicts=resolveConflicts,
                clientRequestToken=clientRequestToken,
                configurationValues=configurationValues,
                podIdentityAssociations=podIdentityAssociations
            )
            return response 
        
                        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ResourceInUseException as e:return e
    
    def UpdateClusterConfig(
        self,
        name:str, 
        resourcesVpcConfig:Optional[dict]=None,
        logging:Optional[dict]=None, 
        clientRequestToken:Optional[str]=None, 
        accessConfig:Optional[dict]=None,
        upgradePolicy:Optional[str]=None, 
        zonalShiftConfig:Optional[dict]=None, 
        computeConfig:Optional[dict]=None, 
        kubernetesNetworkConfig:Optional[dict]=None, 
        storageConfig:Optional[dict]=None, 
        remoteNetworkConfig:Optional[dict]=None
        )-> dict:
        
        try:
            
            response = self.client.update_cluster_config(
                name=name,
                resourcesVpcConfig=resourcesVpcConfig,
                logging=logging,
                clientRequestToken=clientRequestToken,
                accessConfig=accessConfig,
                upgradePolicy=upgradePolicy,
                upgradePolicy=upgradePolicy,
                zonalShiftConfig=zonalShiftConfig,
                computeConfig=computeConfig,
                kubernetesNetworkConfig=kubernetesNetworkConfig,
                storageConfig=storageConfig,
                remoteNetworkConfig=remoteNetworkConfig
            )
            
            return response 
        
                                
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ResourceInUseException as e:return e
        except self.client.exceptions.ThrottlingException as e:return e
        
    
    def UpdateClusterVersion(self, name:str, version:str, clientRequestToken:Optional[str]=None, force:Optional[bool]=False)->dict:
        
        
        try:
            
            response = self.client.update_cluster_version(
                name=name, 
                version=version,
                clientRequestToken=clientRequestToken, force=force
            )
            
            return response 
        
                                        
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ResourceInUseException as e:return e
        except self.client.exceptions.ThrottlingException as e:return e
        except self.client.exceptions.InvalidStateException as e:return e
    
    def UpdateEKsAnyWhereSubscription(self, id:str, autoRenew:str, clientRequestToken:str)->dict:
        
        try:
            
            response = self.client.update_eks_anywhere_subscription(
                id=id, 
                autoRenew=autoRenew, 
                clientRequestToken=clientRequestToken
            )
            
            return response 
        
                                               
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ResourceInUseException as e:return e

        
        
    
    def UpdateNodeGroupConfig(
        self, 
        clustername:str, 
        nodegroupName:str,
        labels:Optional[dict]=None, 
        taints:Optional[dict]=None,
        scalingConfig:Optional[dict]=None, 
        updateConfig:Optional[dict]=None, 
        nodeRepairConfig:Optional[dict]=None, 
        clientRequestToken:Optional[str]=None
    )->dict:
        
        try:
            
            response = self.client.update_nodegroup_config(
                clusterName=clustername, 
                nodegroupName=nodegroupName,
                labels=labels,
                taints=taints,
                scalingConfig=scalingConfig,
                updateConfig=updateConfig,
                nodeRepairConfig=nodeRepairConfig,
                clientRequestToken=clientRequestToken
            )
            
            return response
        
                                                       
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ResourceInUseException as e:return e
        
        
    def UpdateNodegroupVersion(
        self,
        clusterName:str, 
        nodegroupName:str, 
        version:str, 
        releaseVersion, 
        launchTemplate:Optional[dict]=None, 
        force:Optional[bool]=False, 
        clientRequestToken:Optional[str]=None
        )->dict:
        
        try:
            
            response = self.client.update_nodegroup_version(
                clusterName=clusterName,
                nodegroupName=nodegroupName,
                version=version,
                releaseVersion=releaseVersion,
                launchTemplate=launchTemplate,
                force=force,
                clientRequestToken=clientRequestToken
            )
            
            return response
        
                                                               
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ResourceInUseException as e:return e
         
    
    def UpdatePodIdentityAssociation(
        self, 
        clusterName:str, 
        associationId:str,
        roleArn:str, 
        clientRequestToken:str, 
    )->dict:
        
        try:
            
            response = self.client.update_pod_identity_association(
                clusterName=clusterName,
                associationId=associationId,
                roleArn=roleArn,
                clientRequestToken=clientRequestToken
            )
            
            return response
        
                                                                 
        except self.client.exceptions.ServerException as e:return e
        except self.client.exceptions.InvalidRequestException as e:return e
        except self.client.exceptions.InvalidParameterException as e:return e
        except self.client.exceptions.ResourceNotFoundException as e:return e
        except self.client.exceptions.ClientException as e:return e
        except self.client.exceptions.ResourceInUseException as e:return e    


    
class AmazonKubernetesClustersProvider(
    AmazonK8Actions
):
    
    def __init__(self):
        super().__init__()
