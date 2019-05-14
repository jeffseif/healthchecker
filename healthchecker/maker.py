import functools
import json
import subprocess


DEFAULT_CONFIG_PATH = './config.json'


def maker(path, target):
    return subprocess.run(['make', '-C', path, target], stdout=subprocess.PIPE).stdout


def maker_generator(app, config_path=DEFAULT_CONFIG_PATH):
    with open(config_path, 'r') as f:
        for rule, (path, target) in json.load(f).items():
            yield rule, functools.partial(maker, path, target)
