from django.db import models

# Create your models here.
class Projects(models.Model):

    def __str__(self):
        return self.title


    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    url = models.URLField()
    image = models.ImageField(default='')