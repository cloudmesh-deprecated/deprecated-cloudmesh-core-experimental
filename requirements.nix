{ pkgs
, buildPythonPackage
, fetchurl
, extras ? []
, ...
}:

with pkgs;
with pythonPackages;

rec {

  cffi = buildPythonPackage {
      name = "cffi-1.9.1";
      src = fetchurl {
        url = "https://pypi.python.org/packages/a1/32/e3d6c3a8b5461b903651dd6ce958ed03c093d2e00128e3f33ea69f1d7965/cffi-1.9.1.tar.gz";
        sha256 = "563e0bd53fda03c151573217b3a49b3abad8813de9dd0632e10090f6190fdaf8";
      };
      format = "setuptools";
      buildInputs = [ libffi ];
      propagatedBuildInputs = [ pycparser ];
      doCheck = false;
    }
    ;
  python-magnumclient = buildPythonPackage {
      name = "python-magnumclient-2.5.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/09/06/f05ed36123184b7b051e87a9992c7ec3a55779604741d893f9ba30ab594e/python_magnumclient-2.5.0-py2.py3-none-any.whl";
        sha256 = "8f8deebb9661e1de8f279792220ad7995fa3926a8fcd88edaab412152cba0d5e";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ msgpack-python oslo-serialization monotonic stevedore iso8601 netifaces pytz cryptography requestsexceptions requests positional os-client-config enum34 ipaddress wrapt decorator keystoneauth1 cliff pycparser oslo-i18n debtcollector funcsigs unicodecsv oslo-utils pbr cffi PyYAML osc-lib Babel prettytable cmd2 simplejson netaddr idna asn1crypto ];
      doCheck = false;
    }
    ;
  netaddr = buildPythonPackage {
      name = "netaddr-0.7.19";
      src = fetchurl {
        url = "https://pypi.python.org/packages/0c/13/7cbb180b52201c07c796243eeff4c256b053656da5cfe3916c3f5b57b3a0/netaddr-0.7.19.tar.gz";
        sha256 = "38aeec7cdd035081d3a4c306394b19d677623bf76fa0913f6695127c7753aefd";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  funcsigs = buildPythonPackage {
      name = "funcsigs-1.0.2";
      src = fetchurl {
        url = "https://pypi.python.org/packages/94/4a/db842e7a0545de1cdb0439bb80e6e42dfe82aaeaadd4072f2263a4fbed23/funcsigs-1.0.2.tar.gz";
        sha256 = "a7bb0f2cf3a3fd1ab2732cb49eba4252c2af4240442415b4abce3b87022a8f50";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  prettytable = buildPythonPackage {
      name = "prettytable-0.7.2";
      src = fetchurl {
        url = "https://pypi.python.org/packages/ef/30/4b0746848746ed5941f052479e7c23d2b56d174b82f4fd34a25e389831f5/prettytable-0.7.2.tar.bz2";
        sha256 = "853c116513625c738dc3ce1aee148b5b5757a86727e67eff6502c7ca59d43c36";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  Babel = buildPythonPackage {
      name = "Babel-2.3.4";
      src = fetchurl {
        url = "https://pypi.python.org/packages/b4/ec/acd307eac2e23f9cab1c8bdbe29b3b1d43215e31c32f8aa91b3a97925b5b/Babel-2.3.4-py2.py3-none-any.whl";
        sha256 = "3318ed2960240d61cbc6558858ee00c10eed77a6508c4d1ed8e6f7f48399c975";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ pytz ];
      doCheck = false;
    }
    ;
  pycparser = buildPythonPackage {
      name = "pycparser-2.17";
      src = fetchurl {
        url = "https://pypi.python.org/packages/be/64/1bb257ffb17d01f4a38d7ce686809a736837ad4371bcc5c42ba7a715c3ac/pycparser-2.17.tar.gz";
        sha256 = "0aac31e917c24cb3357f5a4d5566f2cc91a19ca41862f6c3c22dc60a629673b6";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  python-heatclient = buildPythonPackage {
      name = "python-heatclient-1.8.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/49/5b/004b251ed9a5ddd19b4151cf3f7601f2e076004bb95b4230f09208e1497e/python_heatclient-1.8.0-py2.py3-none-any.whl";
        sha256 = "c7d5f9fb70f4da0d05c3c87093333062cc016af794060719d169efa38217ee5b";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ msgpack-python monotonic stevedore iso8601 netifaces pytz python-swiftclient futures requestsexceptions requests positional os-client-config wrapt keystoneauth1 cliff oslo-serialization oslo-i18n debtcollector funcsigs unicodecsv prettytable pbr PyYAML osc-lib Babel oslo-utils cmd2 simplejson netaddr ];
      doCheck = false;
    }
    ;
  requestsexceptions = buildPythonPackage {
      name = "requestsexceptions-1.2.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/b6/ac/659483588ad847056ddf01062bca15995b95463efb859e9e2672847dca84/requestsexceptions-1.2.0-py2.py3-none-any.whl";
        sha256 = "f4b43338e69bb7038d2a4ad8cce6b9240e2d272aaf437bd18a2dc9eba25a735c";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ pbr ];
      doCheck = false;
    }
    ;
  vcversioner = buildPythonPackage {
      name = "vcversioner-2.16.0.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/5a/6b/6f5da157648cadbaf83f625c395cd23ff6be3421268b7bf54523b8d9aaab/vcversioner-2.16.0.0-py2-none-any.whl";
        sha256 = "1b81bd26218944e6c86b03c7a840e058c697f014a03374296dc2f8969d1adf36";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  SQLAlchemy = buildPythonPackage {
      name = "SQLAlchemy-1.1.6";
      src = fetchurl {
        url = "https://pypi.python.org/packages/24/de/66d96cbad7a91443af1399469e9aa0aec8a41669ba6d0faae8b8411ddb27/SQLAlchemy-1.1.6.tar.gz";
        sha256 = "815924e3218d878ddd195d2f9f5bf3d2bb39fabaddb1ea27dace6ac27d9865e4";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  jsonschema = buildPythonPackage {
      name = "jsonschema-2.6.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/58/b9/171dbb07e18c6346090a37f03c7e74410a1a56123f847efed59af260a298/jsonschema-2.6.0.tar.gz";
        sha256 = "6ff5f3180870836cae40f06fa10419f557208175f13ad7bc26caa77beb1f6e02";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [ functools32 vcversioner ];
      doCheck = false;
    }
    ;
  msgpack-python = buildPythonPackage {
      name = "msgpack-python-0.4.8";
      src = fetchurl {
        url = "https://pypi.python.org/packages/21/27/8a1d82041c7a2a51fcc73675875a5f9ea06c2663e02fcfeb708be1d081a0/msgpack-python-0.4.8.tar.gz";
        sha256 = "1a2b19df0f03519ec7f19f826afb935b202d8979b0856c6fb3dc28955799f886";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  jmespath = buildPythonPackage {
      name = "jmespath-0.9.2";
      src = fetchurl {
        url = "https://pypi.python.org/packages/10/3b/968949a364f7f9fb9ff5acec3b98df2d74c201ab5f0cd07fa6c48ea227c2/jmespath-0.9.2-py2.py3-none-any.whl";
        sha256 = "3f03b90ac8e0f3ba472e8ebff083e460c89501d8d41979771535efe9a343177e";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  debtcollector = buildPythonPackage {
      name = "debtcollector-1.12.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/73/27/27ad27e66c1d4bf602583cfec1c65966f7c7f756cf5099023a9a979169d2/debtcollector-1.12.0-py2.py3-none-any.whl";
        sha256 = "34a048a530b47944ecba1e17fdcef9fec169ec07e8831b52142df635359be343";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ funcsigs wrapt pbr six ];
      doCheck = false;
    }
    ;
  python-novaclient = buildPythonPackage {
      name = "python-novaclient-7.1.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/76/6e/61118a2bfdce3843948b9e7fbb9c8b964ad96d2ba18ffb8cb841f82fc9f7/python_novaclient-7.1.0-py2.py3-none-any.whl";
        sha256 = "ff46aabc20c39a9fad9ca7aa8f15fd5145852d7385a47e111df7bfd7cd106a65";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ oslo-serialization keystoneauth1 simplejson prettytable ];
      doCheck = false;
    }
    ;
  python-ironicclient = buildPythonPackage {
      name = "python-ironicclient-1.11.1";
      src = fetchurl {
        url = "https://pypi.python.org/packages/d0/6b/4758f84a2c6d756f64d1a6bd2be04ca7d2481b67f38509293223137fce81/python_ironicclient-1.11.1-py2.py3-none-any.whl";
        sha256 = "6c0695cd4bf7ed84be92c8f206fa56b98af8969144313e5f52ec5e74aabf9326";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ msgpack-python monotonic stevedore iso8601 jsonpointer python-cinderclient python-novaclient pytz dogpile-cache requestsexceptions requests functools32 positional os-client-config jsonpatch prettytable wrapt keystoneauth1 cliff oslo-serialization openstacksdk oslo-i18n debtcollector funcsigs unicodecsv oslo-utils python-glanceclient pbr deprecation PyYAML osc-lib Babel netifaces cmd2 rfc3986 python-openstackclient simplejson warlock netaddr oslo-config jsonschema python-keystoneclient ];
      doCheck = false;
    }
    ;
  wrapt = buildPythonPackage {
      name = "wrapt-1.10.10";
      src = fetchurl {
        url = "https://pypi.python.org/packages/a3/bb/525e9de0a220060394f4aa34fdf6200853581803d92714ae41fc3556e7d7/wrapt-1.10.10.tar.gz";
        sha256 = "42160c91b77f1bc64a955890038e02f2f72986c01d462d53cb6cb039b995cdd9";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  rfc3986 = buildPythonPackage {
      name = "rfc3986-0.4.1";
      src = fetchurl {
        url = "https://pypi.python.org/packages/82/53/c3ee5a1869fdf5d1d02c344ed939769b886178ec7ba91d5200e1c779bc87/rfc3986-0.4.1-py2.py3-none-any.whl";
        sha256 = "6823e63264be3da1d42b3ec0e393dc8e6d03fd5e28d4291b797c76cf33759061";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  deprecation = buildPythonPackage {
      name = "deprecation-1.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/ab/fe/edad444ecab087e57dd32a10e38ef0d7448b3ab8ff8bfa65b022d3a43a1c/deprecation-1.0.tar.gz";
        sha256 = "36d2a2356ca89fb73f72bfb866a2f28e183535a7f131a3b34036bc48590165b6";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  python-glanceclient = buildPythonPackage {
      name = "python-glanceclient-2.6.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/6e/c1/b9d59ad77dba5d7f036d23b7aadea89447305aa145aaaa5cf1f76a849c38/python_glanceclient-2.6.0-py2.py3-none-any.whl";
        sha256 = "e77e63de240f4e183a0960c83eb434774746156571c9ea7e7ef4421365b1a762";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ monotonic pbr iso8601 jsonpointer pytz requests functools32 positional jsonpatch wrapt keystoneauth1 stevedore oslo-i18n debtcollector funcsigs prettytable warlock Babel oslo-utils netifaces netaddr jsonschema ];
      doCheck = false;
    }
    ;
  positional = buildPythonPackage {
      name = "positional-1.1.1";
      src = fetchurl {
        url = "https://pypi.python.org/packages/83/73/1e2c630d868b73ecdea381ad7b081bc53888c07f1f9829699d277a2859a8/positional-1.1.1.tar.gz";
        sha256 = "ef845fa46ee5a11564750aaa09dd7db059aaf39c44c901b37181e5ffa67034b0";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [ wrapt pbr ];
      doCheck = false;
    }
    ;
  jsonpatch = buildPythonPackage {
      name = "jsonpatch-1.15";
      src = fetchurl {
        url = "https://pypi.python.org/packages/be/c1/947048a839120acefc13a614280be3289db404901d1a2d49b6310c6d5757/jsonpatch-1.15.tar.gz";
        sha256 = "ae23cd08b2f7246f8f2475363501e740c4ef93f08f2a3b7b9bcfac0cc37fceb1";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [ jsonpointer ];
      doCheck = false;
    }
    ;
  python-designateclient = buildPythonPackage {
      name = "python-designateclient-2.6.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/f8/15/4ac00b87d121e3bc44bc04b6025e0014c8e38ac7f65e693db0e18de2d15c/python_designateclient-2.6.0-py2.py3-none-any.whl";
        sha256 = "cfc980c1f7c77ad87113b3d67b04aa08adedd94b8d456aed29df3358e9be048e";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ monotonic Babel iso8601 netifaces pytz requestsexceptions requests functools32 positional os-client-config wrapt keystoneauth1 cliff stevedore oslo-i18n debtcollector funcsigs unicodecsv prettytable pbr PyYAML osc-lib oslo-utils cmd2 simplejson netaddr jsonschema ];
      doCheck = false;
    }
    ;
  oslo-serialization = buildPythonPackage {
      name = "oslo.serialization-2.17.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/d7/32/48e99c029160452fff0ef8f929c1340010deea7e986dd748efd3a4ba371c/oslo.serialization-2.17.0-py2.py3-none-any.whl";
        sha256 = "4aaa022cb81d51d4469b050bb8f85f6de85e6f17c4b64afec06d9224b9953013";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ oslo-i18n pbr debtcollector monotonic funcsigs wrapt iso8601 netifaces oslo-utils netaddr Babel pytz msgpack-python ];
      doCheck = false;
    }
    ;
  traits = buildPythonPackage {
      name = "traits-4.6.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/56/47/03f50e82e1ff1e8a602c5f2cf12f08675f79a7169629fe4ce521e59d265f/traits-4.6.0.tar.bz2";
        sha256 = "c71c3165526e5375f74358968fd70a258a65d6c8768210ee4e4f88347a4ab853";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  osc-lib = buildPythonPackage {
      name = "osc-lib-1.3.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/47/8b/3c1ef95bcac763a4f3caa2348b641422b6283c89eb4736eeeebdbbffa28a/osc_lib-1.3.0-py2-none-any.whl";
        sha256 = "4817d2d7e3332809d822046297650fec70eceff628be419046ebd66577d16b03";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ monotonic pbr iso8601 netifaces pytz requestsexceptions requests positional os-client-config wrapt keystoneauth1 cliff stevedore oslo-i18n debtcollector funcsigs unicodecsv oslo-utils Babel PyYAML prettytable cmd2 simplejson netaddr ];
      doCheck = false;
    }
    ;
  python-swiftclient = buildPythonPackage {
      name = "python-swiftclient-3.3.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/8f/af/1b91e9aa23e182707bd9309808ccc285501be4f737f1e1862a6c83039797/python_swiftclient-3.3.0-py2.py3-none-any.whl";
        sha256 = "e822b9b743807cff87e018ef54a25a21c54b2eb3651cb5e8d6a27705e4acca8b";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ requests futures six ];
      doCheck = false;
    }
    ;
  warlock = buildPythonPackage {
      name = "warlock-1.2.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/0f/d4/408b936a3d9214b7685c35936bb59d9254c70ff319ee6a837b9efcf5615e/warlock-1.2.0.tar.gz";
        sha256 = "7c0d17891e14cf77e13a598edecc9f4682a5bc8a219dc84c139c5ba02789ef5a";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [ jsonschema jsonpatch six ];
      doCheck = false;
    }
    ;
  openstacksdk = buildPythonPackage {
      name = "openstacksdk-0.9.14";
      src = fetchurl {
        url = "https://pypi.python.org/packages/a8/02/c999d8932cfdc4ea953260d909587e94483e21c6b298b5c9f6d7e97b0c29/openstacksdk-0.9.14-py2.py3-none-any.whl";
        sha256 = "7d1a1fcf5586c6b16b409270d5b861d0969ac0a14a1a5ddfdf95df5be5daab89";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ requestsexceptions requests positional stevedore os-client-config iso8601 wrapt pbr deprecation keystoneauth1 PyYAML ];
      doCheck = false;
    }
    ;
  PyYAML = buildPythonPackage {
      name = "PyYAML-3.12";
      src = fetchurl {
        url = "https://pypi.python.org/packages/4a/85/db5a2df477072b2902b0eb892feb37d88ac635d36245a72a6a69b23b383a/PyYAML-3.12.tar.gz";
        sha256 = "592766c6303207a20efc445587778322d7f73b161bd994f227adaa341ba212ab";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  python-keystoneclient = buildPythonPackage {
      name = "python-keystoneclient-3.10.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/ee/a9/c51a1657f655171d599b43be31b6df5b6d47d83e91595ca43de7bee950cd/python_keystoneclient-3.10.0-py2.py3-none-any.whl";
        sha256 = "f30dd06d03f1f85af0cfa18c270e23d2ffd9e776c11c1b534f6ea503e4f31d80";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ oslo-serialization keystoneauth1 oslo-config ];
      doCheck = false;
    }
    ;
  keystoneauth1 = buildPythonPackage {
      name = "keystoneauth1-2.19.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/ad/41/29e8c0c943756b9a2ee704f0a6bcf176c8fc11a93a73f1c62c38f3e1d385/keystoneauth1-2.19.0-py2.py3-none-any.whl";
        sha256 = "65f326456bcb0bb6bde03a23bb29f85fdb2df10a3e6b65f88a6536829983175d";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ requests positional stevedore iso8601 wrapt pbr ];
      doCheck = false;
    }
    ;
  cryptography = buildPythonPackage {
      name = "cryptography-1.8.1";
      src = fetchurl {
        url = "https://pypi.python.org/packages/ec/5f/d5bc241d06665eed93cd8d3aa7198024ce7833af7a67f6dc92df94e00588/cryptography-1.8.1.tar.gz";
        sha256 = "323524312bb467565ebca7e50c8ae5e9674e544951d28a2904a50012a8828190";
      };
      format = "setuptools";
      buildInputs = [ openssl ];
      propagatedBuildInputs = [ pycparser cffi ipaddress idna asn1crypto enum34 packaging ];
      doCheck = false;
    }
    ;
  oslo-config = buildPythonPackage {
      name = "oslo.config-3.23.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/21/4e/e7a54a345705c0c5ba832ed4348f0e35884f9492a271023253999f7e35fe/oslo.config-3.23.0-py2.py3-none-any.whl";
        sha256 = "7772c5c2a110a29854b03c0e7df82d60352e7165df04e65913e84c88e3a377f4";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ rfc3986 oslo-i18n Babel debtcollector stevedore wrapt pbr pytz funcsigs netaddr ];
      doCheck = false;
    }
    ;
  python-neutronclient = buildPythonPackage {
      name = "python-neutronclient-6.1.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/6d/bf/aa1ebe9de4a92648afe29e692c07d410fde6e1fc914f3dfa3773f39208f5/python_neutronclient-6.1.0-py2.py3-none-any.whl";
        sha256 = "55f9e9b5cba27f6d9bc2b1b4d894764cb94e42054ebf5a1d701b1bf5ac5ecb4a";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ msgpack-python monotonic stevedore iso8601 netifaces pytz requestsexceptions requests positional os-client-config wrapt keystoneauth1 cliff oslo-serialization oslo-i18n debtcollector funcsigs unicodecsv prettytable pbr PyYAML osc-lib Babel oslo-utils cmd2 rfc3986 simplejson netaddr oslo-config python-keystoneclient ];
      doCheck = false;
    }
    ;
  munch = buildPythonPackage {
      name = "munch-2.1.1";
      src = fetchurl {
        url = "https://pypi.python.org/packages/84/dc/d897cb427f15029e04745a3de611d8ed3d97e9a0ef894547a0ba261f2807/munch-2.1.1.tar.gz";
        sha256 = "648b650d1eb0173bd83c29f2eea2568b7591c1e05c87971387d170c71c6397e8";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [ six ];
      doCheck = false;
    }
    ;
  monotonic = buildPythonPackage {
      name = "monotonic-1.3";
      src = fetchurl {
        url = "https://pypi.python.org/packages/96/b3/3e9fa0bdf132a971571cbf0e3f0c8b38834f4f7af8ca9523794f4f5895e0/monotonic-1.3.tar.gz";
        sha256 = "2b469e2d7dd403f7f7f79227fe5ad551ee1e76f8bb300ae935209884b93c7c1b";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  iso8601 = buildPythonPackage {
      name = "iso8601-0.1.11";
      src = fetchurl {
        url = "https://pypi.python.org/packages/c0/75/c9209ee4d1b5975eb8c2cba4428bde6b61bd55664a98290dd015cdb18e98/iso8601-0.1.11.tar.gz";
        sha256 = "e8fb52f78880ae063336c94eb5b87b181e6a0cc33a6c008511bac9a6e980ef30";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  python-cinderclient = buildPythonPackage {
      name = "python-cinderclient-2.0.1";
      src = fetchurl {
        url = "https://pypi.python.org/packages/83/2f/aefb6215b7576969c4fca15f35dc3d931a8c22520b0c786e27074de834b5/python_cinderclient-2.0.1-py2.py3-none-any.whl";
        sha256 = "aa6c3614514d28bd13006a2220a559f10088ceb54b7506888131f95942c158bc";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ requests oslo-i18n pbr debtcollector monotonic stevedore simplejson netifaces oslo-utils prettytable iso8601 netaddr Babel keystoneauth1 pytz positional funcsigs wrapt ];
      doCheck = false;
    }
    ;
  pytz = buildPythonPackage {
      name = "pytz-2016.10";
      src = fetchurl {
        url = "https://pypi.python.org/packages/f5/fa/4a9aefc206aa49a4b5e0a72f013df1f471b4714cdbe6d78f0134feeeecdb/pytz-2016.10-py2.py3-none-any.whl";
        sha256 = "a1ea35e87a63c7825846d5b5c81d23d668e8a102d3b1b465ce95afe1b3a2e065";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  cmd2 = buildPythonPackage {
      name = "cmd2-0.7.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/9b/58/e88fda298b521e6073d4dd7f305cf661d805d1c06fd86f44ccc2f271a800/cmd2-0.7.0.tar.gz";
        sha256 = "5ab76a1f07dd5fd1cc3c15ba4080265f33b80c7fd748d71bd69a51d60b30f51a";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [ six pyparsing ];
      doCheck = false;
    }
    ;
  functools32 = buildPythonPackage {
      name = "functools32-3.2.3-2";
      src = fetchurl {
        url = "https://pypi.python.org/packages/c5/60/6ac26ad05857c601308d8fb9e87fa36d0ebf889423f47c3502ef034365db/functools32-3.2.3-2.tar.gz";
        sha256 = "f6253dfbe0538ad2e387bd8fdfd9293c925d63553f5813c4e587745416501e6d";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  os-client-config = buildPythonPackage {
      name = "os-client-config-1.26.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/f4/de/5feba3da1a4b65053418e7ad738ccc76a6da5e0a484e8647905ee5cd93c5/os_client_config-1.26.0-py2.py3-none-any.whl";
        sha256 = "f9a14755f9e498eb5eef553b8b502a08a033fe3993c7152ce077696b1d37c4f4";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ requestsexceptions keystoneauth1 PyYAML appdirs ];
      doCheck = false;
    }
    ;
  unicodecsv = buildPythonPackage {
      name = "unicodecsv-0.14.1";
      src = fetchurl {
        url = "https://pypi.python.org/packages/6f/a4/691ab63b17505a26096608cc309960b5a6bdf39e4ba1a793d5f9b1a53270/unicodecsv-0.14.1.tar.gz";
        sha256 = "018c08037d48649a0412063ff4eda26eaa81eff1546dbffa51fa5293276ff7fc";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  ipaddress = buildPythonPackage {
      name = "ipaddress-1.0.18";
      src = fetchurl {
        url = "https://pypi.python.org/packages/4e/13/774faf38b445d0b3a844b65747175b2e0500164b7c28d78e34987a5bfe06/ipaddress-1.0.18.tar.gz";
        sha256 = "5d8534c8e185f2d8a1fda1ef73f2c8f4b23264e8e30063feeb9511d492a413e1";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  decorator = buildPythonPackage {
      name = "decorator-4.0.11";
      src = fetchurl {
        url = "https://pypi.python.org/packages/cc/ac/5a16f1fc0506ff72fcc8fd4e858e3a1c231f224ab79bb7c4c9b2094cc570/decorator-4.0.11.tar.gz";
        sha256 = "953d6bf082b100f43229cf547f4f97f97e970f5ad645ee7601d55ff87afdfe76";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  cliff = buildPythonPackage {
      name = "cliff-2.4.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/39/09/dd3b36a9e3ab1ca59ca89e4c6861d477110423dae7d72e026a69d6abc003/cliff-2.4.0-py2-none-any.whl";
        sha256 = "85ef50b1990c6eff557d15732ec1a3a16d7f957b26c922a14dce6100177ce3fb";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ cmd2 stevedore unicodecsv prettytable pbr PyYAML ];
      doCheck = false;
    }
    ;
  oslo-i18n = buildPythonPackage {
      name = "oslo.i18n-3.14.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/ce/99/da741d5576da5e875dbaa2b0d09a88e452115309dcf8671f6e6e7fbce9e7/oslo.i18n-3.14.0-py2.py3-none-any.whl";
        sha256 = "8fee2c53b06645681ff048d21ec3b8eb64bd27879d20701f51b2ec122944786c";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ Babel pbr six ];
      doCheck = false;
    }
    ;
  simplejson = buildPythonPackage {
      name = "simplejson-3.10.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/40/ad/52c1f3a562df3b210e8f165e1aa243a178c454ead65476a39fa3ce1847b6/simplejson-3.10.0.tar.gz";
        sha256 = "953be622e88323c6f43fad61ffd05bebe73b9fd9863a46d68b052d2aa7d71ce2";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  oslo-utils = buildPythonPackage {
      name = "oslo.utils-3.23.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/e6/ef/1f87375d71296c3d80ff913e7d9015e53cae09a097a3f5650f6280c74207/oslo.utils-3.23.0-py2.py3-none-any.whl";
        sha256 = "64d1492471260ca2033b341db547ae9ddc6011825fb6855ddf75bfbf9765e8fa";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ oslo-i18n debtcollector monotonic iso8601 netifaces netaddr pyparsing ];
      doCheck = false;
    }
    ;
  pbr = buildPythonPackage {
      name = "pbr-2.0.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/e9/c0/8f7f54d7b9b8ceb73ac30d769fdd722431e95ad0d2cd689def382e8b9eec/pbr-2.0.0-py2.py3-none-any.whl";
        sha256 = "d9b69a26a5cb4e3898eb3c5cea54d2ab3332382167f04e30db5e1f54e1945e45";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  enum34 = buildPythonPackage {
      name = "enum34-1.1.6";
      src = fetchurl {
        url = "https://pypi.python.org/packages/c5/db/e56e6b4bbac7c4a06de1c50de6fe1ef3810018ae11732a50f15f62c7d050/enum34-1.1.6-py2-none-any.whl";
        sha256 = "6bd0f6ad48ec2aa117d3d141940d484deccda84d4fcd884f5c3d93c23ecd8c79";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  python-openstackclient = buildPythonPackage {
      name = "python-openstackclient-3.9.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/f7/02/cc20ac2b50af74781186fcf8b0599acbfb21238122c830a0cfce936526ef/python_openstackclient-3.9.0-py2.py3-none-any.whl";
        sha256 = "3c48e9bbdff8a7679f04fe6a03d609c75e597975f9f43de7ec001719ec554ad9";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ python-glanceclient openstacksdk osc-lib python-keystoneclient python-novaclient python-cinderclient ];
      doCheck = false;
    }
    ;
  futures = buildPythonPackage {
      name = "futures-3.0.5";
      src = fetchurl {
        url = "https://pypi.python.org/packages/9c/3f/1d818ea03fb2956a2bdfa8f8a3b1319590f0f151a5584a8a3ae45085066c/futures-3.0.5-py2-none-any.whl";
        sha256 = "f7f16b6bf9653a918a03f1f2c2d62aac0cd64b1bc088e93ea279517f6b61120b";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  jsonpointer = buildPythonPackage {
      name = "jsonpointer-1.10";
      src = fetchurl {
        url = "https://pypi.python.org/packages/f6/36/6bdd302303e8bc7c25102dbc1eabb3e3d97f57b0f8f414f4da7ea7ab9dd8/jsonpointer-1.10.tar.gz";
        sha256 = "9fa5dcac35eefd53e25d6cd4c310d963c9f0b897641772cd6e5e7b89df7ee0b1";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  stevedore = buildPythonPackage {
      name = "stevedore-1.21.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/3e/9b/79ad5d29da9453a81707ae0730543d3ea21061dd98afbf0b5d0eaa20a9b9/stevedore-1.21.0-py2.py3-none-any.whl";
        sha256 = "a015fb150871247e385153e98cc03c373a857157628b4746bfdf8501e82e9a3d";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ pbr six ];
      doCheck = false;
    }
    ;
  netifaces = buildPythonPackage {
      name = "netifaces-0.10.5";
      src = fetchurl {
        url = "https://pypi.python.org/packages/a7/4c/8e0771a59fd6e55aac993a7cc1b6a0db993f299514c464ae6a1ecf83b31d/netifaces-0.10.5.tar.gz";
        sha256 = "59d8ad52dd3116fcb6635e175751b250dc783fb011adba539558bd764e5d628b";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  shade = buildPythonPackage {
      name = "shade-1.17.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/96/9a/35ab65c5ef258c10d4397dd8a5e2587b98958258594e023e534d84b41610/shade-1.17.0-py2-none-any.whl";
        sha256 = "3f225cbcbf748e4e380e4dbf9f569d90452da3d202d35ece7b434eb9d1ef190b";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ python-heatclient jmespath munch python-ironicclient python-designateclient python-neutronclient python-magnumclient ];
      doCheck = false;
    }
    ;
  requests = buildPythonPackage {
      name = "requests-2.12.5";
      src = fetchurl {
        url = "https://pypi.python.org/packages/bf/99/af6139323bac0ca0c6023eabbdc526579525f5584278d001dd2e169f8300/requests-2.12.5-py2.py3-none-any.whl";
        sha256 = "d57dae49f4267e8cb378aff9e426c9304a78794d03e945e39bfc607355715658";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  idna = buildPythonPackage {
      name = "idna-2.5";
      src = fetchurl {
        url = "https://pypi.python.org/packages/d8/82/28a51052215014efc07feac7330ed758702fc0581347098a81699b5281cb/idna-2.5.tar.gz";
        sha256 = "3cb5ce08046c4e3a560fc02f138d0ac63e00f8ce5901a56b32ec8b7994082aab";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  asn1crypto = buildPythonPackage {
      name = "asn1crypto-0.22.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/97/ba/7e8117d8efcee589f4d96dd2b2eb1d997f96d27d214cf2b7134ad8acf6ab/asn1crypto-0.22.0-py2.py3-none-any.whl";
        sha256 = "d232509fefcfcdb9a331f37e9c9dc20441019ad927c7d2176cf18ed5da0ba097";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  dogpile-cache = buildPythonPackage {
      name = "dogpile.cache-0.6.2";
      src = fetchurl {
        url = "https://pypi.python.org/packages/9d/a9/ba70aadc6170841a1c6145e9039d4b1c2a4ef8c44cd0ca9b09ab79be9120/dogpile.cache-0.6.2.tar.gz";
        sha256 = "73793471af07af6dc5b3ee015abfaca4220caaa34c615537f5ab007ed150726d";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  

}