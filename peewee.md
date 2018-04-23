Q: 
```
Traceback (most recent call last):
  File "/home/work/python/python36/lib/python3.6/site-packages/twisted/internet/defer.py", line 1386, in _inlineCallbacks
    result = g.send(result)
StopIteration: REP

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/work/python/python36/lib/python3.6/site-packages/twisted/internet/defer.py", line 1386, in _inlineCallbacks
    result = g.send(result)
StopIteration: http://sp2.zingfront.com/sp_opera/485f74bab94dc9fe5f6c7cc7288ba64d.jpg

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/work/python/python36/lib/python3.6/site-packages/twisted/internet/defer.py", line 1386, in _inlineCallbacks
    result = g.send(result)
StopIteration: ITEM

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 3830, in execute_sql
    cursor.execute(sql, params or ())
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/cursors.py", line 166, in execute
    result = self._query(query)
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/cursors.py", line 322, in _query
    conn.query(q)
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/connections.py", line 855, in query
    self._execute_command(COMMAND.COM_QUERY, sql)
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/connections.py", line 1071, in _execute_command
    raise err.InterfaceError("(0, '')")
pymysql.err.InterfaceError: (0, '')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/work/Socialpeta2.0/sp_ads/pipelines/save_unique_relation.py", line 17, in process_item
    SpEtlUniqueRelation.get(SpEtlUniqueRelation.unique_key == item['unique_key'])
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 4988, in get
    return sq.get()
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 3220, in get
    return next(clone.execute())
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 3274, in execute
    self._qr = ResultWrapper(model_class, self._execute(), query_meta)
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 2939, in _execute
    return self.database.execute_sql(sql, params, self.require_commit)
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 3837, in execute_sql
    self.commit()
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 3656, in __exit__
    reraise(new_type, new_type(*exc_args), traceback)
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 135, in reraise
    raise value.with_traceback(tb)
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 3830, in execute_sql
    cursor.execute(sql, params or ())
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/cursors.py", line 166, in execute
    result = self._query(query)
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/cursors.py", line 322, in _query
    conn.query(q)
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/connections.py", line 855, in query
    self._execute_command(COMMAND.COM_QUERY, sql)
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/connections.py", line 1071, in _execute_command
    raise err.InterfaceError("(0, '')")
peewee.InterfaceError: (0, '')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 3830, in execute_sql
    cursor.execute(sql, params or ())
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/cursors.py", line 166, in execute
    result = self._query(query)
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/cursors.py", line 322, in _query
    conn.query(q)
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/connections.py", line 855, in query
    self._execute_command(COMMAND.COM_QUERY, sql)
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/connections.py", line 1071, in _execute_command
    raise err.InterfaceError("(0, '')")
pymysql.err.InterfaceError: (0, '')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/work/python/python36/lib/python3.6/site-packages/twisted/internet/defer.py", line 653, in _runCallbacks
    current.result = callback(current.result, *args, **kw)
  File "/home/work/Socialpeta2.0/sp_ads/pipelines/save_unique_relation.py", line 24, in process_item
    model.save()
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 5170, in save
    pk_from_cursor = self.insert(**field_dict).execute()
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 3584, in execute
    cursor = self._execute()
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 2939, in _execute
    return self.database.execute_sql(sql, params, self.require_commit)
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 3837, in execute_sql
    self.commit()
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 3656, in __exit__
    reraise(new_type, new_type(*exc_args), traceback)
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 135, in reraise
    raise value.with_traceback(tb)
  File "/home/work/python/python36/lib/python3.6/site-packages/peewee.py", line 3830, in execute_sql
    cursor.execute(sql, params or ())
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/cursors.py", line 166, in execute
    result = self._query(query)
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/cursors.py", line 322, in _query
    conn.query(q)
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/connections.py", line 855, in query
    self._execute_command(COMMAND.COM_QUERY, sql)
  File "/home/work/python/python36/lib/python3.6/site-packages/pymysql/connections.py", line 1071, in _execute_command
    raise err.InterfaceError("(0, '')")
peewee.InterfaceError: (0, '') 

```
Replay:
```
1. exec `a = AdIdfa.select().where(AdIdfa.id > 12).get()`
2. close network or block connection
3. exec `a = AdIdfa.select().where(AdIdfa.id > 12).get()` and get `(2013, 'Lost connection to MySQL server during query ([Errno 60] Operation timed out)')`
4. exec `a = AdIdfa.select().where(AdIdfa.id > 12).get()` again and you get it
```

S: close and get new conn
```
try:
    a = AdIdfa.select().where(AdIdfa.id > 12).get()
except Exception as err:
    import sys
    tp = sys.exc_info()[2].tb_next
    while tp:
        if 'self' in tp.tb_frame.f_locals:
            import peewee
            c = tp.tb_frame.f_locals["self"]
            if isinstance(c, peewee.MySQLDatabase):
                if c.is_closed():
                    c.get_conn()
                else:
                    c.close()
                    c.get_conn()
                break
        tp = tp.tb_next        
    print(err)
else:    
    print(a._data)
    
# more commonly
def reconnect_database_when_interface_error():
  # find used db, close and get new connection
  exc_info = sys.exc_info()
  if isinstance(exc_info[1], InterfaceError):
      tp = exc_info[2].tb_next
      while tp:
          if 'self' in tp.tb_frame.f_locals:
              c = tp.tb_frame.f_locals["self"]
              if isinstance(c, peewee.MySQLDatabase):
                  if c.is_closed():
                      c.get_conn()
                  else:
                      c.close()
                      c.get_conn()
                  break
          tp = tp.tb_next
```
