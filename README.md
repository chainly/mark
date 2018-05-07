# mark
mark for something

 ```
 # compare string, specially when compare from `sys.argv`
 '7777' < '100000'  # False
 
 # 数据库清表操作
def delete_core_params_table(self):
   #ScrapyAdmobCoreParams.truncate_table()
   # we have not right to truncate, use delete instand, though too slowly!
   # *切勿中断，否者会回滚, 按区间删*
   _min = 0
   _max = 10000
   for i in range(100000000000):
       r = ScrapyAdmobCoreParams.delete().where(ScrapyAdmobCoreParams.id > _min, ScrapyAdmobCoreParams.id < _max ).execute()
       if not r:
           break
       _min += _max
       max += max
 ```
