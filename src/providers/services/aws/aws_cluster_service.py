"""the kubernetes cluster servixe"""

import boto3
client = boto3.client('eks')

class AmazonK8Actions():
    
    def AssociateAccessPolicy(self):
        pass
    
    def AssociateEncryptionPolicyConfig(self):
        pass
    
    def AssociateIdentityProviderConfig(self):
        pass
    
    def CreateAccessEntry(self):
        pass
    
    def CreateAddon(self):
        pass
    
    def CreateCluster(self):
        pass
    
    def CreateEKsAnyWhereSubscription(self):
        pass
    
    def CreateFargateProfile(self):
        pass
    
    def CreateNodeGroup(self):
        pass
    
    def CreatePodIdentityAssociation(self):
        pass
    
    def DeleteAccessEntry(self):
        pass
    
    def DeleteAddon(self):
        pass
    
    def DeleteCluster(self):
        pass
    
    def DeleteEKsAnyWhereSubscription(self):
        pass
    
    def DeleteFragateProfile(self):
        pass
    
    def DeleteNodeGroup(self):
        pass
    
    def DeletePodIdentityAssociation(self):
        pass
    
    def DeregisterCluster(self):
        pass
    
    def DescribetAccessEntry(self):
        pass
    
    def DescribeAddon(self):
        pass
    
    def DescribeAddonConfiguration(self):
        pass
    
    def DescribeAddonVersions(self):
        pass
    
    def DescribeEKsAnyWhereSubscription(self):
        pass
    
    def DescribeFragateProfile(self):
        pass
    
    def DescribeIdentityProviderConfig(self):
        pass
    
    def DescribeInsight(self):
        pass
    
    def DescribeNodeGroup(self):
        pass
    
    def DescribePodIdentityAssociation(self):
        pass
    
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
