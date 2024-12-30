from django.db import models

class Students(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    roll_number=models.IntegerField()

    def __str__(self):
        return self.first_name+""+self.last_name