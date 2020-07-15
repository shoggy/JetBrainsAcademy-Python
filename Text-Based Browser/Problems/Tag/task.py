def tagged(func):
    def wrapper(args):
        return f"<title>{func(args)}</title>"

    return wrapper
