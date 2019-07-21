from django.db import models

# Create your models here.


class banks(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'banks'


class branches(models.Model):
      ifsc = models.CharField(max_length=11)
      bank_id = models.IntegerField()
      branch = models.CharField(max_length=74)
      address = models.CharField(max_length=195)
      city = models.CharField(max_length=50)
      district = models.CharField(max_length=50)
      state = models.CharField(max_length=26)
	  

      class Meta:
          db_table = 'branches'
