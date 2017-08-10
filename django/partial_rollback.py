#coding: utf8
from django.test import TestCase

# Create your tests here.
"""
Savepoints are available with the SQLite (≥ 3.6.8), PostgreSQL, Oracle and MySQL (when using the InnoDB storage engine) backends.
Other backends provide the savepoint functions, but they’re empty operations – they don’t actually do anything.
"""
# https://docs.djangoproject.com/en/1.10/topics/db/transactions/#django.db.transaction.atomic
from django.db import transaction
from django.http import HttpResponse,HttpResponseBadRequest,JsonResponse,HttpResponseServerError,HttpResponseForbidden
from eam.models import Test
@transaction.atomic
def test(req, tid=None):
    first_one = None
    try:
        first_one = Test.objects.filter()[0]
    except IndexError:
        first_one = Test.objects.create(id=1, status=0)
    else:
        first_one.status = 1
        # even call save ,still rollbacked.
        first_one.save()
    finally:
        print(first_one and first_one.status)
    # only Exceptions cause rollback, not HttpCode
    if first_one and first_one.status == 0:
        return HttpResponse(first_one and first_one.status)
    raise Exception(first_one and first_one.status)
    return HttpResponseForbidden(first_one and first_one.status)
    return HttpResponse(first_one and first_one.status)

def foo():
    """
    If one on-commit function within a given transaction raises an uncaught exception, 
    no later registered functions in that same transaction will run. 
    This is, of course, the same behavior as if you’d executed the functions sequentially 
    yourself without on_commit().
    """
    print('foo save succ')
def bar():
    print('bar save succ')
    
# rollback limited!
# just copy from https://docs.djangoproject.com/en/1.8/topics/db/transactions/#django.db.transaction.clean_savepoints
# any error in transaction.atomic(with out it transaction.* is useless) will roll all back,
# we can only transaction.savepoint_rollback(sid1) to save partly
# transaction.savepoint_commit(sp1) ==> save if no error in transaction.atomic, and no rollback any more
@transaction.atomic
def test(req, tid=None):
    # if want to rollback partly , we can use this
    #with transaction.atomic():

    first_one = None
    try:
        first_one = Test.objects.filter()[0]
    except IndexError:
        first_one = Test.objects.create(id=1, status=0)
    else:
        if first_one.status != 0 or first_one.msg != 0:
            res = first_one.delete()
            
            return HttpResponse(res)
        sp1 = transaction.savepoint()
        # committed--> foo, or rollback.        
        first_one.status = 1
        first_one.save()
        transaction.on_commit(foo)
        # if transaction.savepoint_commit
        # we can't rollback this
        # django.db.utils.OperationalError: (1305, 'SAVEPOINT s139922296198912_x1 does not exist')
        transaction.savepoint_commit(sp1)         
        # even call save ,still rollbacked.
        # use use savepoint
        
        """                
        with transaction.atomic(savepoint = True):
            # only Exceptions in this transaction cause rollback 
            # also cause rollback outside, unless caughted
            # then why I need this savepoint?
            # https://docs.djangoproject.com/en/1.11/topics/db/transactions/#topics-db-transactions-savepoints
            # parted submit
            transaction.on_commit(bar)
            first_one.status = 2
            first_one.msg = 2
            first_one.save()
            #raise Exception(first_one and first_one.status)
        """
        # partly submit
        # https://docs.djangoproject.com/en/1.11/topics/db/transactions/#topics-db-transactions-savepoints
        sp2 = transaction.savepoint()
        #first_one.id = 2
        first_one.status = 2
        first_one.msg = 2
        first_one.save()
        # 
        #transaction.savepoint_rollback(sid)
        # but it still rollback with outside error
        
        # manuly control
        #transaction.set_rollback(rollback=False)            
        # rollback any way
        #transaction.set_rollback(rollback=True)            

    # try not to use finally, unless you know what you are doing
    finally:
        print(first_one and first_one.status)
        
    if first_one and first_one.status == 0:
        return HttpResponse(first_one and first_one.status)
    sp3 = transaction.savepoint()
    first_one.status = 3
    # if no save, it won't save in database ==> status = 1
    first_one.save()
    # excute in order 
    
    # rollback all, except transaction.savepoint_commit(sid)
    try:
        raise Exception(first_one and first_one.status)
        #print('a')
    except:
        # OperationalError: (1305, 'SAVEPOINT s139991688427264_x1 does not exist')
        #transaction.savepoint_rollback(sp1)
        transaction.savepoint_rollback(sp2)
        return HttpResponse(first_one and first_one.status)
    else:
        transaction.savepoint_commit(sp3)
    transaction.commit()    
    # only Exceptions cause rollback, not HttpCode
    return HttpResponseForbidden(first_one and first_one.status)
    return HttpResponse(first_one and first_one.status)


import time

def test(req, tid=None):
    # https://docs.djangoproject.com/en/1.10/ref/models/querysets/#select-for-update
    """
    - Currently, the postgresql, oracle, and mysql database backends support select_for_update(). 
     However, MySQL has no support for the nowait argument. 
    - select_for_update() normally fails in autocommit mode
     you should use TransactionTestCase.
    - if another transaction has already acquired a lock on one of the selected rows,
     the query will block until the lock is released. 
    - timeout required, innodb_lock_wait_timeout | task_timeout | proxy_read_timeout from http_server
    """
    start = time.time()
    with transaction.atomic():
        first_one = None
        try:
            if tid:
                first_one = Test.objects.select_for_update(nowait=False).filter(id = tid)[0]
            else:
                first_one = Test.objects.select_for_update(nowait=False).filter()[0]
        except IndexError:
            first_one = Test.objects.create(id=tid, status=0)
        finally:
            mid = time.time()
            first_one.status += 1
            if not tid:
                time.sleep(20)
            first_one.save()
        end = time.time()
        """
        cool@cool-pc:mysql$curl http://127.0.0.1:8000/test/
        0.0245349407196 20.0191941261 98
        cool@cool-pc:mysql$curl http://127.0.0.1:8000/test/3
        0.0256159305573 0.000590085983276 1
        cool@cool-pc:mysql$curl http://127.0.0.1:8000/test/1
        8.2829811573 0.00146794319153 99cool@cool-pc:mysql$
        """
        return HttpResponse((mid - start, ' ',end - mid, ' ',first_one.status))
