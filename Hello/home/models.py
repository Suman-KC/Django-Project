from django.db import models
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField( max_length=50)
    email=models.CharField(max_length=12)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    

 
    def __str__(self):
     return self.name

    



# Create your models here.
