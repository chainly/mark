> see https://stackoverflow.com/a/50268231/6493535 for `isinstance` in `relative and absolutely import` </p>
> also for [signal](singleton/singleton_with_module_cache_warning.md)

For the real differences, we can find it in `code`, but I can't find the implement of the default behavior of the `isinstance()`. 
 
However we can get the similar one [abc.__instancecheck\_\_](https://github.com/python/cpython/blob/master/Lib/_py_abc.py#L92-L147) according to [\_\_instancecheck\_\_](https://docs.python.org/3/reference/datamodel.html#customizing-instance-and-subclass-checks).

From above `abc.__instancecheck__`, after using test below:


    # file tree
    # /test/__init__.py
    # /test/aaa/__init__.py
    # /test/aaa/aa.py
    class b():
    pass

    # /test/aaa/a.py
    import sys
    sys.path.append('/test')
    
    from aaa.aa import b
    from aa import b as c
    
    d = b()
    
    print(b, c, d.__class__)
    for i in [b, c, object]:
        print(i, '__subclasses__',  i.__subclasses__())
        print(i, '__mro__', i.__mro__)
        print(i, '__subclasshook__', i.__subclasshook__(d.__class__))
        print(i, '__subclasshook__', i.__subclasshook__(type(d)))
    print(isinstance(d, b))
    print(isinstance(d, c))

    <class 'aaa.aa.b'> <class 'aa.b'> <class 'aaa.aa.b'>
    <class 'aaa.aa.b'> __subclasses__ []
    <class 'aaa.aa.b'> __mro__ (<class 'aaa.aa.b'>, <class 'object'>)
    <class 'aaa.aa.b'> __subclasshook__ NotImplemented
    <class 'aaa.aa.b'> __subclasshook__ NotImplemented
    <class 'aa.b'> __subclasses__ []
    <class 'aa.b'> __mro__ (<class 'aa.b'>, <class 'object'>)
    <class 'aa.b'> __subclasshook__ NotImplemented
    <class 'aa.b'> __subclasshook__ NotImplemented
    <class 'object'> __subclasses__ [..., <class 'aaa.aa.b'>, <class 'aa.b'>]
    <class 'object'> __mro__ (<class 'object'>,)
    <class 'object'> __subclasshook__ NotImplemented
    <class 'object'> __subclasshook__ NotImplemented
    True
    False

I get this conclusion,
For `type`:

    # according to `abc.__instancecheck__`, they are maybe different! I have not found negative one 
    type(INSTANCE) ~= INSTANCE.__class__
    type(CLASS) ~= CLASS.__class__
  
For `isinstance`:

    # guess from `abc.__instancecheck__`
    return any(c in cls.__mro__ or c in cls.__subclasses__ or cls.__subclasshook__(c) for c in {INSTANCE.__class__, type(INSTANCE)})

BTW: better not to mix use `relative and absolutely import`, use `absolutely import` from project_dir( added by `sys.path`)
