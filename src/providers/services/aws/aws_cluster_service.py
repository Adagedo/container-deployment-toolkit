"""the kubernetes cluster servixe"""

import boto3
client = boto3.client('eks')

class AmazonKubernetesClustersProvider():
    pass