```
import io
f = io.BytesIO()
f.write(b'dfd')
f.seek(0)
f.read()
Out[57]: b'dfd'

pickle.dump(a, f)
f.tell()
Out[60]: 61
pickle.dump(a, f)
f.tell()
Out[62]: 119
c = pickle.load(f)
Traceback (most recent call last):
  File "/Users/chengcong/anaconda/envs/python36/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2910, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-63-c97fbf390712>", line 1, in <module>
    c = pickle.load(f)
EOFError: Ran out of input
f.seek(3)
Out[64]: 3
c = pickle.load(f)
c
Out[66]: api.models.sp_raw.scrapy_admob_task.ScrapyAdmobTask
c = pickle.load(f)
c
Out[68]: api.models.sp_raw.scrapy_admob_task.ScrapyAdmobTask
c = pickle.load(f)
Traceback (most recent call last):
  File "/Users/chengcong/anaconda/envs/python36/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2910, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-69-c97fbf390712>", line 1, in <module>
    c = pickle.load(f)
EOFError: Ran out of input
```
