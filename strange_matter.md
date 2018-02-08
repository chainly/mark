1. use huawei_router to nat OUTER_IP:9999 to INNER_IP:ANY_PORT failed (tcp send/send_ack/ack good
  , but client can send data(GET / ...) and server blocked at socket.recv(),
  then rest/final good!!!, no firewall!, see: [server_packages_capture](./aaa)).Still unkown!!!

2. `msg` is overwrite when `Exception` occurred, and delete after getting out of `except` block
```
# python3
msg = 'sdfsdf'
try:
    1/0
except Exception as msg:
    pass
print(msg)
NameError: name 'msg' is not defined
```

3. in `peewee`, `module.select().limit(x).offset(y).get()`, always return `module.select().limit(1).offset(0).get()`
  see:
```
class SelectQuery(Query):

    def get(self):
        clone = self.paginate(1, 1)
        try:
            return next(clone.execute())
        except StopIteration:
            raise self.model_class.DoesNotExist(
                'Instance matching query does not exist:\nSQL: %s\nPARAMS: %s'
                % self.sql())

    @returns_clone
    def paginate(self, page, paginate_by=20):
        if page > 0:
            page -= 1
        self._limit = paginate_by
        self._offset = page * paginate_by
```
