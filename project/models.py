from django.db import models

# Create your models here.
# Represents the file structure in our database

class Speech_Analysis(models.Model):
    name = models.CharField(max_length=100, null=True)
    date_created =  models.DateTimeField(auto_now_add=True, null=True)
    speech_to_be_analyzed = models.CharField(max_length=20000, null=True)

    def __str__(self):
        return self.name


class nlp(models.Model):
    STATUS = (
        ('PENDING', 'Pending'),
        ('ANALYZED', 'Analyzed')
    )
    name = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # category = models.CharField(max_length=100, null=True, )
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.name