from src.providers.services.aws.aws_cluster_service import AmazonKubernetesClustersProvider
from src.providers.services.aws.aws_container_service import AwsContainerProvider
from src.providers.services.aws.aws_image_service import AmazonImageRegistryProvider

class Aws_Provider(
    AwsContainerProvider, 
    AmazonImageRegistryProvider, 
    AmazonKubernetesClustersProvider
):
    
    def __init__(self) -> None:
        super().__init__()
    
    def deploy(self) -> None:
        pass
    
        

        