from django.db import models

# Create your models here.

class AccountModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True)
    email = models.TextField(blank=True)
    password = models.CharField(max_length=200)

    class Meta:
        db_table="account_api"
