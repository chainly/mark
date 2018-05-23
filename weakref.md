- see `asyncio.task.Task._all_tasks`, use `weakref` to cache object
> A primary use for weak references is to implement caches or mappings holding large objects, 
where it’s desired that a large object not be kept alive solely because it appears in a cache or mapping

*read [this](http://doc.sagemath.org/html/en/reference/misc/sage/misc/weak_dict.html) later!*

- see `copy.deepcopy.memo`, use `d = {hash: result} to cache result

- for a copy to modify , use `copy.deepcopy`


1. case `cascade delete`,
```
import weakref
class A():
    c = 10
def cb(r):
    if r in l:
        l.remove(r)
    if r in d:
        d.pop(r)
# for delete cascade
l = []
d = {}
aaa = A()
xxx = weakref.ref(aaa, cb)
l.append(xxx)
d[xxx] = 1
del aaa
l
Out[51]: []
d
Out[52]: {}


# for proxy:
xxx = weakref.proxy(aaa, cb)
d[xxx] = 1
Traceback (most recent call last):
  File "/Users/chengcong/anaconda/envs/python36/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2910, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-6-4a9ad995d19f>", line 1, in <module>
    d[xxx] = 1
TypeError: unhashable type: 'weakproxy'
```
