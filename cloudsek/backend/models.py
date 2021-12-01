from enum import unique
from django.db import models

# Create your models here.

class calculate(models.Model):
    instance_url = models.URLField()
    token_id = models.URLField()
    access_token = models.CharField(max_length=200, blank=True)
    token_type = models.CharField(max_length=200, blank=True)
    signature = models.CharField(max_length=200, blank=True)
    issued_at = models.BigIntegerField()