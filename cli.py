# cli.py project entry
import click
import crud


@click.group()
def cli():
    """Container Deployment Toolkit CLI"""
    pass

@cli.command()
def createprovider():
    pass
cli.add_command(crud.show)
cli.add_command(crud.findme)
cli.add_command(crud.commit)
cli.add_command(crud.run)
cli.add_command(crud.info)
