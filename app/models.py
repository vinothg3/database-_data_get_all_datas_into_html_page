from django.db import models

# Create your models here.

class Topic(models.Model):
    Topic_name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Topic_name
    
class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Email=models.EmailField()

    def __str__(self):
        return self.Name
    
class Detail(models.Model):
    Name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    Place=models.CharField(max_length=100)
    Date=models.DateField()