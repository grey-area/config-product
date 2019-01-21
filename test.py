import json
import os
from config_product import config_product


if __name__ == '__main__':
    with open('config.json') as f:
        config = json.load(f)

    configs = config_product(config)
    configs_dir = 'configs'
    os.makedirs(configs_dir, exist_ok=True)

    for c_i, c in enumerate(configs):
        with open(os.path.join(configs_dir, f'config_{c_i}.json'), 'w') as f:
            json.dump(c, f, indent=2)
