from comparator.gaussian import Gaussian
from comparator.uniform import Uniform
from comparator.oracle import Oracle

def comparator(name: str, **kwargs):
    """
    Returns a comparator function.
    
    :param name: The name of the comparator.
    :param kwargs: The arguments to the comparator.
    :return: The comparator function.
    """
    if name == 'gaussian':
        return Gaussian(**kwargs)
    elif name == 'uniform':
        return Uniform(**kwargs)
    elif name == 'oracle':
        return Oracle(**kwargs)
    else:
        raise ValueError("Invalid comparator")