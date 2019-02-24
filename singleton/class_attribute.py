# like `from testfixtures import LogCapture` # No: this is for log instances
# use class's class_attribute; basely same as metaclass.attr
class A():
  
    _instance = None  # not set()
  
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
         
        return cls._instance

a = A()
b = A()
print(a, b)
