# mark
mark for something

 ```
# compare string, specially when compare from `sys.argv`
'7777' < '100000'  # False
 
# 数据库清表操作
# select * from information_schema.innodb_trx where trx_id=27989211459;
"""
trx_id	trx_state	trx_started	trx_requested_lock_id	trx_wait_started	trx_weight	trx_mysql_thread_id	trx_query	trx_operation_state	trx_tables_in_use	trx_tables_locked	trx_lock_structs	trx_lock_memory_bytes	trx_rows_locked	trx_rows_modified	trx_concurrency_tickets	trx_isolation_level	trx_unique_checks	trx_foreign_key_checks	trx_last_foreign_key_error	trx_adaptive_hash_latched	trx_adaptive_hash_timeout	trx_is_read_only	trx_autocommit_non_locking
27989211459	ROLLING BACK	2018-05-07 00:23:35	NULL	NULL	3693117	34502269	NULL	rollback	0	0	3385372	299824680	15116250	307745	0	READ COMMITTED	1	1	NULL	0	10000	0	0
"""
# show processlist;

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
       _max += _max

 ```
