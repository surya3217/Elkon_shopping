from django.db import models

# Create your models here.
class Value(models.Model):
    value = models.IntegerField(null=False)
    timestamp = models.DateTimeField()
    class Meta:
        unique_together = ('value', 'timestamp')

