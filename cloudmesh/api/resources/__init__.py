from abc import ABCMeta, abstractmethod, abstractproperty
from six import add_metaclass

from cloudmesh.util.patterns import Composite


@add_metaclass(ABCMeta)
class Resource(object):

    @abstractproperty
    def data(self):
        "A :class:`dict` representing the metadata about this resource"

    @abstractmethod
    def allocate(self):
        "Allocate this resource"

    @abstractmethod
    def deallocate(self):
        "Deallocate this resource"


class ResourceComposite(Resource):

    def __init__(self, elements):

        for elem in elements:
            assert isinstance(elem, Resource)

        self.composite = Composite(elements)

    @property
    def data(self):
        return None

    def getattr(self, name):
        "Return a list of attributes for each element"

        def gen():
            for elem in self.composite.elements:
                yield getattr(elem, name)

        return list(gen())

    def allocate(self):
        self.composite.allocate()

    def deallocate(self):
        self.composite.deallocate()


################################################################ TESTING

class _TestResource_TmpDir(Resource):

    @property
    def data(self):
        return dict(path=self.path, type='dir')

    def allocate(self):
        import tempfile
        self.path = tempfile.mkdtemp(prefix='cloudmesh.resource.test')
        return self.path

    def deallocate(self):
        import shutil
        shutil.rmtree(self.path)


class _TestResource_TmpFile(Resource):

    @property
    def data(self):
        return dict(path=self.path, type='file', file=self.file)

    def allocate(self):
        import tempfile
        self.file, self.path = tempfile.mkstemp()
        return self.file


    def deallocate(self):
        import os
        os.close(self.file)
        os.unlink(self.path)


def test_resource_tmpdir():

    import os.path

    r = _TestResource_TmpDir()

    r.allocate()

    path = r.data['path']

    assert os.path.exists(path)
    assert os.path.isdir(path)

    r.deallocate()
    assert not os.path.exists(path)


def test_resource_tmpfile():

    import os.path

    r = _TestResource_TmpFile()

    r.allocate()

    path = r.data['path']

    assert os.path.exists(path)
    assert os.path.isfile(path)

    r.deallocate()
    assert not os.path.exists(path)


def test_resource_composite():

    import os.path

    resources = ResourceComposite([
        _TestResource_TmpDir(),
        _TestResource_TmpDir(),
        _TestResource_TmpFile(),
        _TestResource_TmpFile(),
    ])

    resources.allocate()

    paths = resources.getattr('path')
    for p in paths:
        assert os.path.exists(p)

    resources.deallocate()
    for p in paths:
        assert not os.path.exists(p)
