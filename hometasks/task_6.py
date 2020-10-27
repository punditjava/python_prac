from functools import partial


def set_attributes(wrapper, f):
    wrapper.__module__ = f.__module__
    wrapper.__name__ = f.__name__
    wrapper.__doc__ = f.__doc__
    return wrapper


def substitutive(f):
    args_count = f.__code__.co_argcount

    def wrapper(*args, **kwargs):
        if args_count == args.__len__():
            return f(*args, **kwargs)
        elif args_count < args.__len__():
            raise TypeError

        used_args = []
        if args.__len__() != 0:
            used_args += args

        return set_attributes(partial(wrapper, *used_args), f)

    return set_attributes(wrapper, f)
