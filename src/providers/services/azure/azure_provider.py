from src.providers.services.azure.azure import AzureManagementService

class AzureProvider(AzureManagementService):
    def __init__(self):
        super().__init__()