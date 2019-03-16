from django.db import models

# Create your models here.
class fibResult(models.Model):

    #num = models.CharField(max_length = 50)
    number = models.IntegerField()
    nthFib = models.IntegerField()
    timeTaken = models.CharField(max_length=50)

    class Meta:
        db_table = "nthfib"

    def __str__(self):
        return self.number
