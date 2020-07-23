from django.db import models

# Create your models here.
class Memo(models.Model):
    content = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
