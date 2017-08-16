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
