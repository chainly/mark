1. 弱引用(weak reference)
```
def a(b):
    b.append('1')

c = []
d = a(c)
c
['1']
d
 ``` 
2. python2 循环中间量
``` 
[ i for i in c ]
['1']
i
'1'
``` 

3. variable overwrite global in function
```
# explation
# https://stackoverflow.com/questions/12091973/python-closure-with-assigning-outer-variable-inside-inner-function
# 1. any assigned variable in function will store/treat as local variable before run f()
#  unless set by global/nonlocal
# 2. `it's a simple but effective performance optimization`, or maybe meet `explicit > implicit`
In [9]: m = 1
In [11]: def n():
    ...:    m = m +1
    ...:    return m
    ...: 

In [12]: n()
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
<ipython-input-12-6ca03bde44e5> in <module>()
----> 1 n()

<ipython-input-11-736b421bee32> in n()
      1 def n():
----> 2    m = m +1
      3    return m

UnboundLocalError: local variable 'm' referenced before assignment
```
