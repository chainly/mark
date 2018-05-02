## inlineCallbacks
> ---------------------> return  
 ----　　　　　　　----> return  
 　　----reactor---

  return _inlineCallbacks(None, gen, Deferred())
### _inlineCallbacks
    while True:
        result = g.send(result)
            # done/returnValue() was called
            StopIteration as e
            deferred.callback(getattr(e, "value", None))  # def a():
                                                          #     yield 1
                                                          #     return 2
                                                          # g = a()
                                                          # next(g)
                                                          # try:
                                                          #    next(g)
                                                          # except StopIteration as e:
                                                          #    e.value # 2
            return deferred

            # error
            deferred.errback()
            return deferred

            # get an Deferred: This allow us to move to reactor, and callback to back here
            gotResult:
                - waiting[0] = False  # Deferred have callback yet: set waiting = False
                - _inlineCallbacks  # No, wait deferred.callback and continue loop
            result.addBoth(gotResult)
            # Deferred have callback yet
            reset and continue loop
            # No, wait deferred.callback and continue loop
            waiting[0] = False
            return deferred

### _inlineCallbacks.cancel and cron jobs

    import time
    @defer.inlineCallbacks
    def gg():
        n = 0
        # _inlineCallbacks's deferred havn't use cancel
        #def cancel(df):
            #print(df, 'camcel!')
            #df._suppressAlreadyCalled = True
            #return df        

        def do_add(r):
            #n += 1
            print(time.time(), n)
            r = repr(r) if isinstance(r, failure.Failure) else r  # else get Unhandled error in Deferred: CancelledError
            return r
        while True:
            print(time.time(), n)
            n += 1
            d = defer.Deferred(canceller=cancel)
            d.debug = True
            d.addBoth(do_add)
            reactor.callLater(5, d.callback, 111)
            try:
                r = yield d
            except Exception as err:
                print('11111', err)
    d = gg()
    d.addBoth(lambda r : print(repr(r)))
    reactor.addSystemEventTrigger('before', 'shutdown', d.cancel)
    reactor.run()
    print('11', d.result, d.callbacks)


## Deferred
    d = Deferred()
    d.addCallback(f1)
    d.adderrBack(f2)
    f3: d.callback(v)
    
    # equal
    f4(f1?, f2?): v = f3(); (f1(v))?; (f2(v))? 
    
### Deferred.cancel

    from twisted.internet import defer, reactor, threads
    from twisted.python import failure

    def cancel(df):
        ## https://stackoverflow.com/a/37443701/6493535
        # if callback:
        #    self.errback(failure.Failure(CancelledError()))
        #  get to errback chain
        print('cancel', df)
        df.debug = True
        #df.callbacks = df.callbacks[:1]

        # here we need to callback or done by d.cancel with 
        # self.errback(failure.Failure(CancelledError()))
        df.errback(failure.Failure(defer.CancelledError('cancelled!')))
        # you can set it True equal to defer.Deferred(canceller=None), no AlreadyCalledError raise
        df._suppressAlreadyCalled = True
        return df

    def errback(r):
        print(1, r)
        return r

    def callback(r):
        print(1, r)
        return 1    

    def final(r):
        # handle all `result` in fanal, else `Unhandled error in Deferred:`
        r = repr(r) if isinstance(r, failure.Failure) else r
        print(3, r)
        return r

    def c(r):
        print(2, r)
        return failure.Failure(Exception())  # Exception instance required!


    d = defer.Deferred(canceller=cancel)
    # add to be addCallbacks as pairs
    d.addCallbacks(callback, errback)
    d.addBoth(c)
    d.addBoth(final)
    """
    cancel <Deferred at 0x10eb32278>
    1 [Failure instance: Traceback (failure with no frames): <class 'twisted.internet.defer.CancelledError'>: 
    ]
    3 1
    2 [Failure instance: Traceback (failure with no frames): <class 'Exception'>: 
    ]
    raise AlreadyCalledError
    """
    d.cancel()  # basely equal to d.errback(failure.Failure(CancelledError()))
    try:
        d.callback(10000)
    except Exception as err:
        print(111, type(err), repr(err))
    else:
        print(d.result)
    #d.cancel()  # nothing

