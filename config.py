from pyaml_env import parse_config, BaseConfig
import os

config = parse_config('default.yaml')

if os.path.isfile('config.yaml'):
    config = {**config, **parse_config('config.yaml')}

config = BaseConfig(config)