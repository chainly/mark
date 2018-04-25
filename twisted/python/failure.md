# Failure
```
from twisted.python.failure import Failure
try:
    1/0
except Exception as err:
    try:
        raise RuntimeError
    except Exception as err:
        import sys
        e = err
        exc = sys.exc_info()
        f = Failure()
        
e
Out[7]: RuntimeError()

exc
Out[8]: (RuntimeError, RuntimeError(), <traceback at 0x1059ddb88>)

exc[2]
Out[9]: <traceback at 0x1059ddb88>

import traceback
traceback.print_tb(exc[2])
  File "<ipython-input-6-11fe7329c523>", line 5, in <module>
    raise RuntimeError
exc[2].tb_next
f.getTraceback()
Out[13]: 'Traceback (most recent call last):\n  File "/Applications/PyCharm.app/Contents/helpers/pydev/_pydev_bundle/pydev_ipython_console_011.py", line 428, in add_exec\n    self.ipython.run_cell(line, store_history=True)\n  File "/Users/chengcong/anaconda/envs/python36/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2728, in run_cell\n    interactivity=interactivity, compiler=compiler, result=result)\n  File "/Users/chengcong/anaconda/envs/python36/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2850, in run_ast_nodes\n    if self.run_code(code, result):\n  File "/Users/chengcong/anaconda/envs/python36/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2910, in run_code\n    exec(code_obj, self.user_global_ns, self.user_ns)\n--- <exception caught here> ---\n  File "<ipython-input-6-11fe7329c523>", line 5, in <module>\n    raise RuntimeError\nbuiltins.RuntimeError: \n'
print(f.getTraceback())
Traceback (most recent call last):
  File "/Applications/PyCharm.app/Contents/helpers/pydev/_pydev_bundle/pydev_ipython_console_011.py", line 428, in add_exec
    self.ipython.run_cell(line, store_history=True)
  File "/Users/chengcong/anaconda/envs/python36/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2728, in run_cell
    interactivity=interactivity, compiler=compiler, result=result)
  File "/Users/chengcong/anaconda/envs/python36/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2850, in run_ast_nodes
    if self.run_code(code, result):
  File "/Users/chengcong/anaconda/envs/python36/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2910, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
--- <exception caught here> ---
  File "<ipython-input-6-11fe7329c523>", line 5, in <module>
    raise RuntimeError
builtins.RuntimeError: 

# *https://docs.python.org/3.3/library/traceback.html?highlight=traceback#traceback.print_exception*
In [15]: traceback.print_exception(*exc)
Traceback (most recent call last):
  File "<ipython-input-4-e6b8b013f644>", line 3, in <module>
    1/0
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<ipython-input-6-11fe7329c523>", line 5, in <module>
    raise RuntimeError
builtins.RuntimeError: 

exc == f.getTracebackObject()
Out[15]: False

exc[2] == f.getTracebackObject()
Out[16]: True

e == f.value
Out[17]: True

f.type
Out[18]: RuntimeError
```

```
traceback.format_exception(f.type, f.value, f.getTracebackObject())
Out[44]: 
['Traceback (most recent call last):\n',
 '  File "<ipython-input-43-8ba8603a184c>", line 3, in <module>\n    1/0\n',
 'ZeroDivisionError: division by zero\n',
 '\nDuring handling of the above exception, another exception occurred:\n\n',
 'Traceback (most recent call last):\n',
 '  File "<ipython-input-43-8ba8603a184c>", line 5, in <module>\n    raise RuntimeError\n',
 'RuntimeError\n']
```
