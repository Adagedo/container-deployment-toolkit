from src.providers.services.aws.aws_service_provider import Aws_Provider
from src.providers.services.azure.azure_provider import AzureProvider
from src.providers.services.google.google_cloud_container.google_provider import GoogleProvider

class CloudProvider():
    def create_provider(self, provider_name:str) -> Aws_Provider | AzureProvider |GoogleProvider:
        match(provider_name):
            case 'aws':
                return Aws_Provider()
            case 'google':
                return GoogleProvider()
            case 'azure':
                return AzureProvider()
        raise NameError(f"unsupported provider -> {provider_name}")