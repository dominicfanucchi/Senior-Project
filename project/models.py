from django.db import models

# Create your models here.
# Represents the file structure in our database

class Speech_Analysis(models.Model):
    date_created =  models.DateTimeField(auto_now_add=True, null=True)
    speech_to_be_analyzed = models.CharField(max_length=20000, null=True)