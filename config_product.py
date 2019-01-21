from functools import reduce
from copy import deepcopy
from itertools import product


def get_key_paths(d, key_paths=[], param_lists=[], acc=[]):
    for k, v in d.items():
        if isinstance(v, dict):
            get_key_paths(v, key_paths, param_lists, acc=acc + [k])
        elif isinstance(v, list) and not k.endswith('list'):
            key_paths.append(acc + [k])
            param_lists.append(v)

    return key_paths, param_lists


def set_key_path(d, key_path, v):
    d1 = reduce(dict.get, key_path[:-1], d)
    d1[key_path[-1]] = v


def config_product(config):
    key_paths, param_lists = get_key_paths(config)

    configs = []
    for params in product(*param_lists):
        config_copy = deepcopy(config)
        for key_path, param in zip(key_paths, params):
            set_key_path(config_copy, key_path, param)

        configs.append(config_copy)

    return configs
