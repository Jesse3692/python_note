"""工具类"""


def printer(func):
    """打印函数的返回值

    Args:
        func ([type]): [description]
    """
    def inner(*args, **kwargs):
        print(func(*args, **kwargs))
        return func(*args, **kwargs)
    return inner
