import shade

from collections import namedtuple

from cloudmesh.api.provider import Provider as ProviderInterface
from cloudmesh.api.provider import Result

from cloudmesh.util import Dotdict

import logging
logger = logging.getLogger(__name__)


class Provider(ProviderInterface):

    def __init__(self, **kwargs):

        self._cloud = shade.openstack_cloud(**kwargs)

    def _cloud_list_to_results(self, attr, *args, **kwargs):
        values = Dotdict(getattr(self._cloud, 'list_%s' % attr)(*args, **kwargs))
        return [Result(str(value.id), value)
                for value in values]

    @property
    def name(self):
        return 'openstack'      # FIXME needs self inspection for more descriptive name

    def nodes(self):
        return self._cloud_list_to_results('servers')

    def secgroups(self):
        return self._cloud_list_to_results('security_groups')

    def flavors(self):
        return self._cloud_list_to_results('flavors')

    def images(self):
        return self._cloud_list_to_results('images')

    def addresses(self):
        return self._cloud_list_to_results('floating_ips')

    def networks(self):
        return self._cloud_list_to_results('networks')

    ################################ nodes

    def allocate_node(self, name=None, image=None, flavor=None, network=None, **kwargs):

        # Sanity check
        logger.debug('OpenStack allocate_node sanity check')
        vars = locals()
        required = ['name', 'image', 'flavor', 'network']
        for _param_name in required:
            val = vars[_param_name]
            if not val:
                msg = 'Required argument %s not specified' % _param_name
                logger.critical(msg)
                raise ValueError(msg)

        logger.info('Allocating OpenStack node with name=%s, image=%s, flavor=%s, networks=%s, %s',
                    name, image, flavor, networks, str(kwargs))

        server = self._cloud.create_server(name=name,
                                           image=image,
                                           flavor=flavor,
                                           network=network,
                                           **kwargs)

        return Result(str(server.id), Dotdict(server))


    def deallocate_node(self, ident):
        logger.info('Deallocating OpenStack node %s', ident)
        self._cloud.delete_server(ident, delete_ips=True)

    def get_node(self, ident):
        n = Dotdict(self._cloud.get_server(ident))
        return Result(str(n.id), n)

    ################################ images

    def allocate_ip(self):
        ip = self._cloud.available_floating_ip()
        return Result(str(ip.id), ip)

    def deallocate_ip(self, ident):
        logger.debug('Deallocating IP %s', ident)
        self._cloud.delete_floating_ip(ident)

    def associate_ip(self, ip_ident, node_ident):
        logger.debug('Associating IP %s to node %s', ip_ident, node_ident)
        node = self._cloud.get_server(node_ident)
        ip_munch = self._cloud.get_floating_ip(ip_ident)
        ip = ip_munch.floating_ip_address
        self._cloud.add_ip_list(node, [ip])

    def disassociate_ip(self, ip_ident, node_ident):
        logger.debug('Disassociating IP %s from node %s', ip_ident, node_ident)
        self._cloud.detach_ip_from_server(node_ident, ip_ident)

    def get_ip(self, ident):
        logger.debug('Retrieving IP %s', ident)
        ip = Dotdict(self._cloud.get_floating_ip(ident))
        return Result(str(ip.id), ip)

    ################################ security groups

    def allocate_secgroup(self, *args, **kwargs): raise NotImplementedError()
    def deallocate_secgroup(self, *args, **kwargs): raise NotImplementedError()
    def modify_secgroup(self, *args, **kwargs): raise NotImplementedError()
    def get_secgroup(self, *args, **kwargs): raise NotImplementedError()

    ################################ keys

    def allocate_key(self, name, value, fingerprint):
        logger.debug('Allocating keypair %s %s', name, fingerprint)
        known = self._cloud.get_keypair(name)

        if known and known.fingerprint == fingerprint:
            logger.debug('Key %s %s is already registered')
            return Result(str(known.id), Dotdict(known))

        elif known and not known.fingerprint == fingerprint:
            msg = 'A key by name %s is already registered but its fingerprint %s does not match %s'
            logger.warning(msg, name, known.fingerprint, fingerprint)
            raise ValueError(name, known.fingerprint, fingerprint)

        else:
            logger.debug('Registering %s %s', name, fingerprint)
            self._cloud.create_keypair(name, value)

    def deallocate_key(self, ident):
        logger.debug('Deallocating key %s', ident)
        self._cloud.delete_keypair(ident)

    def modify_key(self, name, value, fingerprint):
        logger.debug('Replacing key %s with %s', key, fingerprint)
        self.deallocate_key(name)
        self.allocate_key(name, value, fingerprint)

    def get_key(self, *args, **kwargs): raise NotImplementedError()

    ################################ images

    def allocate_image(self, *args, **kwargs): raise NotImplementedError()
    def deallocate_image(self, *args, **kwargs): raise NotImplementedError()
    def get_image(self, *args, **kwargs): raise NotImplementedError()



if __name__ == '__main__':
    from os import getenv as e
    logging.basicConfig(level='INFO')
    for name in 'requests keystoneauth'.split():
        logging.getLogger(name).setLevel('INFO')

    p = Provider()

    print p.name

    print 'Nodes'
    for r in p.nodes():
        print r, r.name
    print

    print 'Security groups'
    for r in p.secgroups():
        print r.name
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
        print r.id, r.floating_ip_address, '->', r.fixed_ip_address
    print

    print 'Keys'
    p.deallocate_key('testname')
    p.allocate_key('testname', open('testing/data/testkey.pub').read(),
                   'd6:28:ee:83:6a:0d:bc:1c:3c:af:40:75:67:fa:13:41')
    print

    print 'Allocate node'
    networks = filter(lambda r: r.name.startswith(e('OS_TENANT_NAME')), p.networks())[0]
    node = p.allocate_node(name='badi-cm2test',
                           image='CC-Ubuntu14.04',
                           flavor='m1.small',
                           network=networks)
    print node, p.get_node(node.id).status
    print

    print 'IP'
    ip = p.allocate_ip()
    print ip.id, ip.floating_ip_address
    print

    print 'Get IP'
    r = p.get_ip(ip.id)
    print r.id, ':', r.floating_ip_address
    print

    print 'Associate', ip.floating_ip_address, '->', node.name
    p.associate_ip(ip.id, node.id)
    print

    print 'Disassociate', ip.floating_ip_address
    p.disassociate_ip(ip.id, node.id)
    print

    print 'Deallocate node'
    p.deallocate_node(node.id)
    print

    print 'Deallocate floating ip'
    p.deallocate_ip(ip.id)
    print
