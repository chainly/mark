"""
# __new__ higher than __init__
In [58]: class A(type):
    ...:     def __init__(self,*a,**b):
    ...:         print('init',a,b)
    ...:         super().__init__(*a, **b)
    ...:     def __call__(self,*a,**b):
    ...:         print('call',a,b)
    ...:         super().__call__(*a, **b)
    ...:         
    ...:         
    ...:         

In [59]: class B(metaclass=A):
    ...:     def __init__(self):
    ...:         print('B')
    ...:         
init ('B', (), {'__module__': '__main__', '__qualname__': 'B', '__init__': <function B.__init__ at 0x7fc17aba0b70>}) {}

In [60]: b = B()
call () {}
B
"""

# http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_solution_156
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

# Example
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')
