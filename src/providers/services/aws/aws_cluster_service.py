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
        
    
    def DescribeUpdate(self):
        pass
    
    def DisassociateAccessPolicy(self):
        pass
    
    def DisassociateIdentityProviderConfig(self):
        pass
    
    def ListAccessEntries(self):
        pass
    
    def ListAccessPolicies(self):
        pass
    def ListAddon(self):
        pass
    
    def ListAssociateAccessPolicies(self):
        pass
    
    def ListCluster(self):
        pass
    
    def ListEKsAnyWhereSubscriptions(self):
        pass
    
    def ListFragteProfiles(self):
        pass
    
    def ListIdentityProviderConfig(self):
        pass
    
    def ListInsights(self):
        
        pass
    
    def ListNodeGroups(self):
        pass
    
    def ListPodIdentityAssociation(self):
        pass
    
    def ListTagsForResource(self):
        pass
    
    def ListUpdates(self):
        pass
    
    def RegisterCluster(self):
        pass
    
    
    def TagResource(self):
        pass
    
    def UnTagResource(self):
        pass
    
    def UpdateAccessEntry(self):
        pass
    
    def UpdateAddon(self):
        pass
    
    def UpdateClusterConfig(self):
        pass
    
    def UpdateClusterVersion(self):
        pass
    
    def UpdateEKsAnyWhereSubscription(self):
        pass
    
    def UpdateNodeGroupConfig(self):
        pass
    
    def UpdateNodegroupVersion(self):
        pass
    
    def UpdatePodIdentityAssociation(self):
        pass
    

class AmazonK8DataTypes():
    
    def AccessConfigResponse(self):
        pass
    
    def AccessEntry(self):
        pass 
    
    def AccessPolicy(self):
        pass
    
    def AccessScope(self):
        pass
    
    def Addon(self):
        pass
    
    def AddonCompatibilityDetail(self):
        pass
    
    
    def AddonHealth(self):
        pass
    
    def AddonInfo(self):
        pass
    
    def AddonIssue(self):
        pass
    
    def AddonPodIdentityAssocaition(self):
        pass
    
    def AddonPodIdentityConfiguration(self):
        pass
    
    def AddonVersionInfo(self):
        pass
    
    def AssociateAccessPolicy(self):
        pass
    
    def AutoScalingGroup(self):
        pass
    
    def BlockStorage(self):
        pass
    
    def Certificate(self):
        pass
    
    def ClientStat(self):
        pass
    
    def Cluster(self):
        pass
    
    def ClusterHealth(self):
        pass
    
    def clusterIssues(self):
        pass
    
    def ClusterVersionInformation(self):
        pass
    
    def Compatibility(self):
        pass
    
    def ComputeConfigRequest(self):
        pass
    
    def ComputeConfigResponse(self):
        pass
    
    def ConnectorConfigRequest(self):
        pass
    
    def ConnectorConfigResponse(self):
        pass
    
    def ControlPanelPlacementRequest(self):
        pass
    
    def ControlPanelPlacementResponse(self):
        pass
    
    def CreateAccessConfigRequest(self):
        pass
    
    def DeprecationDetail(self):
        pass
    
    def EKsAnyWhereSubscription(self):
        pass
    
    def EKsAnyWhereSubscriptionTerm(self):
        pass
    
    def ElasticLoadBalancing(self):
        pass
    
    def EncryptionConfig(self):
        pass
    
    def ErrorDetail(self):
        pass
    
    def FargateProfile(self):
        pass
    
    def FargateProfileHealth(self):
        pass
    
    def FargateProfileIssue(self):
        pass
    
    def FargateProfileSelctor(self):
        pass
    
    def Identity(self):
        pass
    
    def IdentityProviderConfig(self):
        pass
    
    def IdentityProviderConfigResponse(self):
        pass
    
    def IdentityProviderConfigResponse(self):
        pass
    
    def Insight(self):
        pass
    
    def InsightCategoySpecificSummary(self):
        pass
    
    def InsightResourceDetail(self):
        pass
    
    def InsightFilter(self):
        pass
    
    def InsightStatus(self):
        pass
    
    def InsightSummary(self):
        pass
    def Issue(self):
        pass
    
    def KubernetesNetworkConfigRequest(self):
        pass
    
    def KubernetesNetworkConfigResponse(self):
        pass
    
    def LaunchTemplateSpecification(self):
        pass
    
    def License(self):
        pass
    
    def Logging(self):
        pass
    
    def LogSetUp(self):
        pass
    
    def MarketPlaceInformation(self):
        pass
    
    def NodeGroup(self):
        pass
    
    def NodeGroupHealth(self):
        pass
    
    def NodegroupResource(self):
        pass
    
    def NodegroupScalingConfig(self):
        pass
    
    def NodegroupUpdateconfig(self):
        pass
    
    def NodeRepairConfig(self):
        pass
    
    def OIDC(self):
        pass
    
    def OIDCIdentityProviderConfig(self):
        pass
    
    def OIDCProviderConfigRequest(self):
        pass
    
    def OutPostConfigReuest(self):
        pass
    
    def OutPostConfigResponse(self):
        pass
    
    def PodIdentityAssociation(self):
        pass
    
    def PodIdentityAssociationSummary(self):
        pass
    
    def Provider(self):
        pass
    
    def RemoteAccessConfig(self):
        pass
    
    def RemoteNetworkConfigRequest(self):
        pass
    
    def ReomteNetworkConfigResponse(self):
        pass
    
    def RemoteNodeNetwork(self):
        pass
    
    def RemotePodNetwork(self):
        pass
    
    def StorageConfigRequest(self):
        pass
    
    def StorageConfigResponse(self):
        pass
    
    def Taint(self):
        pass
    
    def Update(self):
        pass
    
    def UpdateAccessConfigRequest(self):
        pass
    
    def UpdateLabelsPayload(self):
        pass
    
    def UpdateParams(self):
        pass
    
    def UpdateTaintPayload(self):
        pass
    
    def UpgradePolicyRequest(self):
        pass
    
    def UpgradePolicyResponse(self):
        pass
    
    def VpcConfigRequest(self):
        pass
    
    def VpcConfigResponse(self):
        pass
    
    def ZonalShiftConfigRquest(self):
        pass
    
    def ZonalShiftConfigResponse(self):
        pass


class AmazonK8Aauth():
    
    def AssumedRoleUser(self):
        pass
    
    def Credentials(self):
        pass
    
    def PodIdentityAssociation(self):
        pass
    
    def Subject(self):
        pass
        
    
class AmazonKubernetesClustersProvider(
    AmazonK8Actions, 
    AmazonK8DataTypes,
    AmazonK8Aauth
):
    
    def __init__(self):
        super().__init__()
