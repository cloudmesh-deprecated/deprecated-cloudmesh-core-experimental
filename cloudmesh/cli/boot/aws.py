
import click

import boto3

import logging
logger = logging.getLogger(__name__)


@click.command()
@click.option('-i', '--image', default='ami-f4cc1de2')
@click.option('-t', '--instance-type', default='t2.small')
def aws(image, instance_type):
    """Boot on AWS"""
    logger.info('AWS %s %s', image, instance_type)

    ec2 = boto3.resource('ec2')
    i = ec2.Image(image)
    print list(ec2.subnets.all())
