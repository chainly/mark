```
# when get one singleton instance like this/scrapy.signal
# pp
#   xx (yy=object())
#   __file__

from pp.xx import yy
print(id(yy), sys.modules.get('pp.xx'))

from xx import yy
print(id(yy), sys.modules.get('xx'))
from .. import yy
print(id(yy), sys.modules.get('xx'))

# *they are different, as use different cache!*

# why
# ref: https://docs.python.org/3/reference/import.html#the-module-cache

```
