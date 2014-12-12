from django.db import models

# Create your models here.

class Student(models.Model):
    # st_id = models.ForeignKey("self", related_name="referral", null=True, blank=True)
    name = models.CharField(max_length=120, default='ABC', unique=True)
    group = models.CharField(max_length=120, default='ABC')


    def __unicode__(self):
        return "%s %s" %(self.name, self.group)
