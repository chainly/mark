from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
    
class Test(models.Model):
    
    id = models.CharField(primary_key=True, 
                          db_index=True, 
                          db_column='id',
                          max_length=50 )
    status = models.IntegerField(default=0,)
    msg = models.IntegerField(default=0,)

    class Meta:
        db_table = 'tests_test'
        
    def __unicode__(self):
        return '%r'%self.id
