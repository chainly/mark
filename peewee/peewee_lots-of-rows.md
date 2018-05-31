- http://peewee.readthedocs.io/en/latest/peewee/querying.html#iterating-over-lots-of-rows

---
    # for memory usage too much (~3g for 43w) even use iterator
    self.limit = 10000
    self.offset = 0
    #self.maxid = 0
--

[1 ,10000]
[10001 ,20000]
.
.
.
