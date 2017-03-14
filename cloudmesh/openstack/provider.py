from collections import namedtuple

from keystoneauth1.session import Session

from cloudmesh.api.provider import Provider as ProviderInterface
from cloudmesh.util import Dotdict

import logging
logger = logging.getLogger(__name__)


AuthResult = namedtuple('AuthResult', ['keystone', 'nova'])


def auth_keystone_v2(**authinfo):
    logger.debug('Using Keystone V2 authentication')
    from keystoneauth1.identity import v2
    from keystoneclient.v2_0.client import Client as Keystone
    from novaclient.client import Client as Nova

    authinfo = Dotdict(authinfo)
    cacert = authinfo.get('cacert', None)
    for param in 'username tenant_name auth_url cacert'.split():
        logger.debug('Authenticating with {}={}'.format(param, authinfo.get(param, None)))

    auth = v2.Password(
        username = authinfo.username,
        password = authinfo.password,
        tenant_name = authinfo.tenant_name,
        auth_url = authinfo.auth_url,
    )

    sess = Session(auth=auth)
    keystone = Keystone(session=sess, cacert=cacert)
    nova = Nova(2, session=sess)

    return AuthResult(keystone=keystone, nova=nova)



class Provider(ProviderInterface):

    def __init__(self, keystone_version='2', **authinfo):

        if keystone_version == '2':
            auth = auth_keystone_v2(**authinfo)
        else:
            msg = 'Unsupported keystone version {}'.format(keystone_version)
            logger.critical(msg)
            raise NotImplementedError(msg)

        self.keystone = auth.keystone
        self.nova = auth.nova

    @property
    def secgroups(self): raise NotImplementedError()
    @property
    def flavors(self): raise NotImplementedError()
    @property
    def images(self): raise NotImplementedError()
    @property
    def nodes(self): raise NotImplementedError()
    @property
    def name(self): raise NotImplementedError()
    @property
    def addresses(self): raise NotImplementedError()


    def deallocate_image(self, *args, **kwargs): raise NotImplementedError()
    def allocate_image(self, *args, **kwargs): raise NotImplementedError()
    def modify_key(self, *args, **kwargs): raise NotImplementedError()
    def deallocate_key(self, *args, **kwargs): raise NotImplementedError()
    def allocate_key(self, *args, **kwargs): raise NotImplementedError()
    def modify_secgroup(self, *args, **kwargs): raise NotImplementedError()
    def deallocate_secgroup(self, *args, **kwargs): raise NotImplementedError()
    def allocate_secgroup(self, *args, **kwargs): raise NotImplementedError()
    def disassociate_ip(self, *args, **kwargs): raise NotImplementedError()
    def associate_ip(self, *args, **kwargs): raise NotImplementedError()
    def deallocate_ip(self, *args, **kwargs): raise NotImplementedError()
    def allocate_ip(self, *args, **kwargs): raise NotImplementedError()
    def deallocate_node(self, *args, **kwargs): raise NotImplementedError()
    def allocate_node(self, *args, **kwargs): raise NotImplementedError()



if __name__ == '__main__':
    from os import getenv as e
    logging.basicConfig(level='DEBUG')

    p = Provider(
        username = e('OS_USERNAME'),
        password = e('OS_PASSWORD'),
        tenant_name = e('OS_TENANT_NAME'),
        auth_url = e('OS_AUTH_URL'),
        cacert = e('OS_CACERT'),
    )

    print p.keystone.users.list()
    print p.nova.servers.list()
