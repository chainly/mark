# run
  run()
  - mainLoop()
    - runUntilCurrent()
      - self.threadCallQueue  # reactor.callFromThread
      - self._pendingTimedCalls  # reactor.callLater
    - doIteration()  # doSelect, IOEvent
  - 

# thread
## callFromThread
  callFromThread
    - self.threadCallQueue.append((f, args, kw))
  runUntilCurrent
    - for (f, a, kw) in self.threadCallQueue: f(*a, **kw)
    
## callInThread
  - self.getThreadPool().callInThread(_callable, *args, **kwargs)
    - self.getThreadPool()
      - self._initThreadPool()
        - self.threadpool = threadpool.ThreadPool
        - self.callWhenRunning(self.threadpool.start)
        - self.addSystemEventTrigger('during', 'shutdown', self._stopThreadPool)
    - callInThread  # twisted.internet.thread.deferToThread
      - callInThreadWithCallback
        - context  # like global dict with call, get
        - self._team.do(inContext)  # this seems like just run in thread, nothing with reactor
                                    # or @defer.inlineCallbacks
                                    # reactor.callInThread(f, deferred=d, *args, **kwargs) d.callback(r) to move back
    
