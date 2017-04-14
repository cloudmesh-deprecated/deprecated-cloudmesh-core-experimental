import click

from .aws import aws
from .openstack import openstack


@click.group()
def boot():
    pass

boot.add_command(aws)
boot.add_command(openstack)
