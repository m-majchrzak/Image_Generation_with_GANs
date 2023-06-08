import copy
import itertools
import random
import numpy as np
import torch


def set_seeds(seed):
    torch.manual_seed(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.use_deterministic_algorithms(True)  # Needed for reproducible results


def make_configs(base_config, combinations):
    product_input = [p['values'] for p in combinations.values()]
    product = [p for p in itertools.product(*product_input)]
    configs = []
    for p in product: # for each combination
        config = copy.deepcopy(base_config)
        for i, parameter in enumerate(combinations.values()): # for each parameter in config
            for name in parameter['dict_path'][:-1]: # finish when pointing at second-last element from path
                pointer = config[name]
            pointer[parameter['dict_path'][-1]] = p[i] # set desired value
        configs.append(config)
    return configs

