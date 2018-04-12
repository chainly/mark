## inlineCallbacks
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


## Deferred
    d = Deferred()
    d.addCallback(f1)
    d.adderrBack(f2)
    f3: d.callback(v)
    
    # equal
    f4(f1?, f2?): v = f3(); (f1(v))?; (f2(v))? 
    
