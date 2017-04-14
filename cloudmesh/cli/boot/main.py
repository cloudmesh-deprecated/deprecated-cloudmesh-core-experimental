import click

from .aws import aws
from .openstack import openstack


@click.group()
def boot():
    "Boot machine(s)"
    pass

boot.add_command(aws)
boot.add_command(openstack)
