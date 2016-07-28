import os
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


_file_path = os.path.realpath(os.path.join(__file__, '..', 'configuration.yaml'))


class _Config(object):
    def __init__(self):
        if not os.path.isfile(_file_path):
            yaml.dump({}, file(_file_path, 'w'), Dumper=Dumper)
        super(_Config, self).__setattr__('_yaml_config', yaml.load(file(_file_path, 'r'), Loader=Loader))

    def __setattr__(self, k, v):
        if v is None:
            self._yaml_config.pop(k, None)
        else:
            self._yaml_config[k] = v
        yaml.dump(self._yaml_config, file(_file_path, 'w'), Dumper=Dumper)

    def __getattr__(self, k):
        try:
            return self._yaml_config[k]
        except KeyError:
            raise AttributeError

    def __str__(self):
        return str(self._yaml_config)


CONFIG = _Config()
