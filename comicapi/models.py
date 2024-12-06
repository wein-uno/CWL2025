from django.db import models

# Create your models here.

class Comics(models.Model):
       title = models.CharField(max_length=50)
       number = models.IntegerField(default=1)
       grade = models.CharField(max_length=4, choices=[('9.8', '9.8'), ('9.6', '9.6')])
       #grade = models.CharField(choices=[('9.8', '9.8'), ('9.6', '9.6'), (9.4, 9.4), (9.2, 9.2),(9.0, 9.0),(8.5, 8.5),(8.0, 8.0),(7.5, 7.5),(7.0, 7.0),(6.5, 6.5)(6.0, 6.0),(5.5, 5.5),(5.0, 5.0),(4.5, 4.5),(4.0, 4.0),(3.5, 3.5),(3.0, 3.0),(2.5, 2.5),(2.0, 2.0),(1.5, 1.5),(1.0, 1.0),(0.5, 0.5),(0.1, 0.1)])
       price = models.DecimalField(max_digits=10, decimal_places=2)

def __str__(self):
       return f"{self.title} - Issue #{self.number}"


