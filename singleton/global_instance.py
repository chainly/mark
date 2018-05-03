# http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_discussion_156
# 
class _Spam:
    def __init__(self):
        print('Creating Spam')

_spam_instance = None  # or just import it like `scrapy.signals.*_*`
def Spam():
    global _spam_instance
    if _spam_instance is not None:
        return _spam_instance
    else:
        _spam_instance = _Spam()
        return _spam_instance
