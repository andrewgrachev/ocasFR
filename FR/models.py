from django.db import models


class wtpersons(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    folder = models.TextField()
    class Meta:
        db_table = 'wtpersons'


class wtpersonenters(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    person_id = models.IntegerField()
    class Meta:
        db_table = 'wtpersonenters'

class wtpersonimages(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    image_name = models.TextField()
    person_id = models.TextField()
    class Meta:
        db_table = 'wtpersonimages'