from django.db import models

# Create your models here.


class studentdata(models.Model):

	rollno = models.IntergerField()
	name = models.CharField(max_length=30)
	branch = models.CharField(max_length=10)
