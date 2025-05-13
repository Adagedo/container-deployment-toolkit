# cli.py project entry
import click


@click.group()
def cli():
    """Container Deployment Toolkit CLI"""
    pass

@cli.command()
def createprovider():
    pass
    
    