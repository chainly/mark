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

---

    # offset bigger, cost more
    # use this
    self.cur = self.min = 0
    self.max = max(id)
    itv = 10000
    
    do_loop:
        if self.cur >= self.max: done

        where_start = id > self.cur
        where_end = id <= self.cur+self.itv
        
        for_loop:
            self.cur = i
        self.cur = self.cur+self.itv
