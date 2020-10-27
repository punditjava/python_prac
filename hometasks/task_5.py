import functools


def check_arguments(*types):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args):
            if types is not None:
                if args.__len__() < types.__len__():
                    raise TypeError
                for typ in range(types.__len__()):
                    if not isinstance(args[typ], types[typ]):
                        raise TypeError
            return f(*args)
        return wrapper
    return decorator
