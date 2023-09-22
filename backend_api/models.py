from django.db import models
from django.conf import settings

class DataSource(models.Model):
    Name = models.CharField(max_length=100)
    SourceId = models.IntegerField(default=1)

class DataBranch(models.Model):
    EventDT = models.DateTimeField(auto_now_add=True)
    BranchId = models.IntegerField()