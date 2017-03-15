from collections import namedtuple

from keystoneauth1.session import Session

from cloudmesh.api.provider import Provider as ProviderInterface
from cloudmesh.api.provider import Result

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

    def _nova_list_to_results(self, attr):
        values = getattr(self.nova, attr).list()
        return [Result(str(value.id), Dotdict(value.to_dict()))
                for value in values]

    @property
    def name(self):
        return 'openstack'      # FIXME needs self inspection for more descriptive name

    def nodes(self):
        return self._nova_list_to_results('servers')

    def secgroups(self):
        return self._nova_list_to_results('security_groups')

    def flavors(self):
        return self._nova_list_to_results('flavors')

    def images(self):
        return self._nova_list_to_results('images')

    def addresses(self):
        return self._nova_list_to_results('floating_ips')

    def networks(self):
        return self._nova_list_to_results('networks')

    ################################ nodes

    def allocate_node(self, name=None, image=None, flavor=None, networks=None, **kwargs):

        # Sanity check
        logger.debug('OpenStack allocate_node sanity check')
        vars = locals()
        required = ['name', 'image', 'flavor', 'networks']
        for _param_name in required:
            val = vars[_param_name]
            if not val:
                msg = 'Required argument %s not specified' % _param_name
                logger.critical(msg)
                raise ValueError(msg)

        logger.info('Allocating OpenStack node with name=%s, image=%s, flavor=%s, networks=%s, %s',
                    name, image, flavor, networks, str(kwargs))

        server = self.nova.servers.create(name=name, image=image, flavor=flavor, nics=networks, **kwargs)
        return Result(str(server.id), Dotdict(server.to_dict()))


    def deallocate_node(self, *args, **kwargs): raise NotImplementedError()

    ################################ images

    def allocate_ip(self, *args, **kwargs): raise NotImplementedError()
    def deallocate_ip(self, *args, **kwargs): raise NotImplementedError()
    def associate_ip(self, *args, **kwargs): raise NotImplementedError()
    def disassociate_ip(self, *args, **kwargs): raise NotImplementedError()

    ################################ security groups

    def allocate_secgroup(self, *args, **kwargs): raise NotImplementedError()
    def deallocate_secgroup(self, *args, **kwargs): raise NotImplementedError()
    def modify_secgroup(self, *args, **kwargs): raise NotImplementedError()

    ################################ keys

    def allocate_key(self, *args, **kwargs): raise NotImplementedError()
    def deallocate_key(self, *args, **kwargs): raise NotImplementedError()
    def modify_key(self, *args, **kwargs): raise NotImplementedError()

    ################################ images

    def allocate_image(self, *args, **kwargs): raise NotImplementedError()
    def deallocate_image(self, *args, **kwargs): raise NotImplementedError()



if __name__ == '__main__':
    from os import getenv as e
    logging.basicConfig(level='DEBUG')
    for name in 'requests keystoneauth'.split():
        logging.getLogger(name).setLevel('INFO')

    p = Provider(
        username = e('OS_USERNAME'),
        password = e('OS_PASSWORD'),
        tenant_name = e('OS_TENANT_NAME'),
        auth_url = e('OS_AUTH_URL'),
        cacert = e('OS_CACERT'),
    )

    print p.name

    print 'Nodes'
    for r in p.nodes():
        print r, r.name
    print

    print 'Security groups'
    for r in p.secgroups():
        print r
        for rule in r.rules:
            print '\t', rule.ip_protocol, rule.from_port, rule.to_port, rule.ip_range.cidr
    print

    print 'Flavors'
    for r in p.flavors():
        print r, r.name, r.vcpus, r.ram, r.disk
    print

    print 'Images'
    for r in p.images():
        print r, r.name
    print

    print 'Addresses'
    for r in p.addresses():
        print r, r.pool, r.ip, '->', r.fixed_ip, '(', r.instance_id, ')'
    print
