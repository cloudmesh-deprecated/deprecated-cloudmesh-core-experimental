
import yaml
from traits.api import File, HasTraits, Instance

from cloudmesh.util import Dotdict


class Config(HasTraits):
    """
    The Cloudmesh configuration
    """

    filename = File(exists=True)
    _config = Instance(Dotdict)

    def __init__(self, filename=None):
        super(Config, self).__init__(filename=filename)

        with open(self.filename) as fd:
            d = yaml.load(fd)
            self._config = Dotdict(d)

    def get_cloud(self, cloudname):
        "Retrieve the configuration properties for the given cloud"
        return self._config.cloudmesh.clouds[cloudname]





################################################################
# Tests
################################################################

def test_config(tmpdir):
    s = """
meta:
  version: 4.1
  kind: clouds
  filename: TBD
  location: TBD
  prefix: null
cloudmesh:
  profile:
    firstname: Badi
    lastname: Abdul-Wahid
    email: badi@iu.edu
    user: badi
  github:
    username: TBD
  clouds:
    kilo:
      cm_heading: India OpenStack, Kilo
      cm_host: india
      cm_label: kilo
      cm_type: openstack
      cm_type_version: kilo
      cm_openrc: TBD
      credentials:
        OS_AUTH_URL: TBD
        OS_PASSWORD: TBD
        OS_TENANT_NAME: TBD
        OS_USERNAME: TBD
        OS_PROJECT_DOMAIN_ID: TBD
        OS_USER_DOMAIN_ID: TBD
        OS_PROJECT_NAME: TBD
        OS_IMAGE_API_VERSION: TBD
        OS_VOLUME_API_VERSION: TBD
        OS_CACERT: TBD
      default:
        flavor: m1.small
        image: Ubuntu-14.04-64
"""

    print tmpdir
    yaml = tmpdir.join('config.yaml')
    yaml.write(s)

    c = Config(yaml.strpath)
    assert isinstance(c, Config)

    kilo = c.get_cloud('kilo')
    assert isinstance(kilo, dict)

    assert kilo.cm_host == 'india'
    assert kilo.credentials.OS_AUTH_URL == 'TBD'
    assert kilo.default.flavor == 'm1.small'
    assert kilo.default.image == 'Ubuntu-14.04-64'
