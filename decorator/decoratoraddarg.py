# when Add Arguments to Wrapped Functions, this example should be used!
# should not change orignal function!!!
# http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#decoratoraddarg
from functools import wraps

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
    
"""
>>> @optional_debug
... def spam(a,b,c):
...     print(a,b,c)
...
>>> spam(1,2,3)
1 2 3
>>> spam(1,2,3, debug=True)
Calling spam
1 2 3

"""
