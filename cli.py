# cli.py project entry
import click
import requests
from src.providers.cloud_provider import CloudProvider

def showLogs():
    return "mthis is the logs to be shown on the page....."


def call_api() -> dict | list | None:
    try:
        response = requests.get("https://www.linked.com")
        response.raise_for_status()
        return response.json()
    except  requests.exceptions.RequestException as e:
        click.echo(message=f"error getting request, {e}")
    
@click.group()
def cli():
    """Container Deployment Toolkit CLI"""
    pass

@cli.command()
def create_provider(provider_name:str):
    provider = CloudProvider()
    provider.create_provider(provider_name=provider_name)
    click.echo(f"setting up {provider_name} enviroment...")
    
    