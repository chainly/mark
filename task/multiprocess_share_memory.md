## copy on write is impossible due to reference counts!

   https://stackoverflow.com/a/1269055/6493535

> This extremely limited form of sharing can still be a lifesaver in some cases (although it's extremely limited: 
> remember for example that adding a reference to a shared object counts as "altering" that object, due to reference counts,
> and so will force a page copy!).

### test
#### base code

```
import sys
sys.path.insert(0, '/home/work/socialpeta2.0')
#from api.models.sp_raw.scrapy_audience_network_task_new import ScrapyAudienceNetworkTaskNew
#q = ScrapyAudienceNetworkTaskNew.select().limit(100000)
#l = list(q)
#print(len(l))

import time
time.sleep(5)


import multiprocessing
n=2


def w():
    print('111')
    time.sleep(20)


p = multiprocessing.Pool(n)
for i in range(n):
    p.apply_async(w, (), error_callback=lambda r: print(r))

p.close()
p.join()
```

#### t1
- main with `l` 

```
  PID USER	 PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
130687 work      20   0  540m 347m 4112 S  0.0  2.2   0:16.20 python3
```

#### t2
- main with `l`
- `print(len(l)) in w`

```
  PID USER	 PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
 50892 work	 20   0  769m 348m 4236 S  0.0  2.2   0:15.89 python3   # add for pool
 51449 work	 20   0  547m 345m 1124 S  0.0  2.2   0:00.00 python3
 51450 work	 20   0  547m 345m 1124 S  0.0  2.2   0:00.00 python3
 ```
 
#### t3
- no l
```
PID USER	 PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
68768 work	 20   0  405m  11m 3532 S  0.0  0.1   0:00.10 python3
68794 work	 20   0  183m 7404 1072 S  0.0  0.0   0:00.00 python3
68795 work	 20   0  183m 7408 1068 S  0.0  0.0   0:00.00 python3
```
 
#### t4
```
import sys

#import tracemalloc
#tracemalloc.start()

sys.path.insert(0, '/home/work/socialpeta2.0')
#from api.models.sp_raw.scrapy_audience_network_task_new import ScrapyAudienceNetworkTaskNew
#q = ScrapyAudienceNetworkTaskNew.select().limit(100000)
#l = list(q)
from multiprocessing import Array
l = Array('c', b',dfdfdfdfasdfsadfsadf'*1000000)
#print(len(l))

#del q, ScrapyAudienceNetworkTaskNew, Array
#print(locals())
#import gc
#gc.collect()

import time
time.sleep(5)

#snapshot = tracemalloc.take_snapshot()
#print(snapshot.statistics('lineno'))

import multiprocessing
n=2

def w():
    print(len(l))
    print('111')
    time.sleep(20)


p = multiprocessing.Pool(n)
for i in range(n):
    p.apply_async(w, (), error_callback=lambda r: print(r))

p.close()
p.join()
```

```
51 ~= 23 + 28
?28m?
PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
4355 work      20   0  451m  51m  23m S  0.0  0.3   0:07.35 python3
5227 work      20   0  229m  28m 1112 S  0.0  0.2   0:00.00 python3
5228 work      20   0  229m  28m 1112 S  0.0  0.2   0:00.00 python3
```
