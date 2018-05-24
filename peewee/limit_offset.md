```
if not self.max_id:
    # self.max_id = self.from_model.select(fn.MAX(self.from_model.id).alias('id')).where(*self.from_filter).get().id or 0
    self.max_id = self.from_model.select(fn.MAX(self.from_model.id).alias('id')).get().id or 0
    assert self.max_id, 'no record'

assert self.offset <= self.max_id, 'done'

if self.current:
    self.data = self.from_model.select().where(self.from_model.id >= self.current.id, *self.from_filter).limit(self.limit).offset(self.offset)
else:
    self.data = self.from_model.select().where(*self.from_filter).limit(self.limit).offset(self.offset)
```
