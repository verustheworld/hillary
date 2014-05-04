from django.db import models

# Create your models here.
class rcp(models.Model):
    year = models.IntegerField(null=True)
    race = models.CharField(max_length=64)
    unit = models.CharField(max_length=64)
    dem = models.CharField(max_length=32)
    rep = models.CharField(max_length=32)
    source = models.CharField(max_length=200)
    sizestr = models.CharField(max_length=64,null=True)
    size = models.IntegerField(null=True)
    demcnt = models.FloatField()
    repcnt = models.FloatField()
    spreadstr = models.CharField(max_length=64,null=True)
    spread = models.FloatField(null=True)
    moe = models.FloatField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    pub_date = models.DateTimeField()
    #unique_together = (("pub_date","source"),("pub_date","race"),("race","source"),("rep","dem"))
    unique_together = (("source","pub_date","race","dem","rep"))
    
    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.source, self.pub_date, self.race, self.dem, self.rep)
