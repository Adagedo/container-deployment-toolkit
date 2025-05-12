import boto3 

client = boto3.client("lambda")
clients_premit = boto3.client('iam')
class AmazonClientAuthenticationService():
    
    def __init__(self):
        pass 
