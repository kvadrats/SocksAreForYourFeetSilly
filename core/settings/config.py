import yaml


class StaticObjectDictionary(type):
    def __getitem__(cls, val):
        return cls._objects[val]

    def __getattr__(cls, item):
        cls.load()
        return cls.__dict__[item]


class AbstractStaticYaml(object):
    __metaclass__ = StaticObjectDictionary

    @classmethod
    def load(cls):
        cls._objects = yaml.load(open(cls.file_absolute_path))
