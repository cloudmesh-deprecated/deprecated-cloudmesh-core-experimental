
from cloudmesh.aws.provider import Provider

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
@click.option('-n', '--name', default='cloudmesh')
@click.option('-i', '--image', default='ami-f4cc1de2')
@click.option('-t', '--instance-type', default='t2.small')
@click.option('-k', '--sshkey', help='The SSH key to allow login')
@click.option('-x', '--secgroups', help='Comma-separated list of security group names to apply (eg foo,bar,baz)')
@click.option('-P', '--public-ip', is_flag=True, help='Associate a public IP')
def aws(name, image, instance_type, sshkey, secgroups, public_ip):
    """Boot on AWS"""

    if secgroups:
        secgroups = secgroups.split(',')
    else:
        secgroups = []

    p = Provider()
    r = p.allocate_node(
        name=name,
        key=sshkey,
        image=image,
        flavor=instance_type,
        security_groups=secgroups)

    

    # ec2 = boto3.resource('ec2')

    # vpc = default_get(ec2.vpcs, vpc, ec2.Vpc)
    # print vpc.tags
    # subnet = default_get(vpc.subnets, subnet, ec2.Subnet)
    # print subnet.tags


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

