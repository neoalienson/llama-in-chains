from pyaml_env import parse_config, BaseConfig
import os

def read_config():
    _config = parse_config('default.yaml')

    if not os.path.isfile('config.yaml'):
        return BaseConfig(_config)
    return BaseConfig({**_config, **parse_config('config.yaml')})

config = read_config()
