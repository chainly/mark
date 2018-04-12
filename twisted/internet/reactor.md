# run
  run()
  - mainLoop()
    - runUntilCurrent()
      - self.threadCallQueue
      - self._pendingTimedCalls
    - doIteration()  # doSelect, IOEvent



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
