
import click

import boto3

import logging
logger = logging.getLogger(__name__)


def default_get(collection, query, mk):
    if query and ':' in query:
        tag, val = query.split(':', 1)
        group = collection.filter(Filters=[dict(Name='tag:{}'.format(tag), Values=[val])]).limit(1)
        return list(group)[0]
    elif query:
        res = mk(query)
        res.reload()
        return res
    else:
        group = collection.filter(Filters=[dict(Name='tag:Name', Values=['default'])]).limit(1)
        return list(group)[0]



@click.command()
@click.option('-i', '--image', default='ami-f4cc1de2')
@click.option('-t', '--instance-type', default='t2.small')
@click.option('-v', '--vpc', help='The PVC to launch in')
@click.option('-s', '--subnet', help='The Subnet of the VPC to use')
def aws(image, instance_type, vpc, subnet):
    """Boot on AWS"""
    logger.info('AWS %s %s', image, instance_type)

    ec2 = boto3.resource('ec2')

    vpc = default_get(ec2.vpcs, vpc, ec2.Vpc)
    print vpc.tags
    subnet = default_get(vpc.subnets, subnet, ec2.Subnet)
    print subnet.tags


    # # pick subnet
    # subnet_filters = []
    # if ':' in subnet:           # filter
    #     key, val = subnet.split(':', 1)
    #     print key, val
    #     group = ec2.subnets.filter(Filters=[dict(Name='tag', Values=[val])])
    #     for subnet in group:
    #         break
    # else:
    #     subnet = ec2.Subnet(subnet)
    #     subnet.reload()

