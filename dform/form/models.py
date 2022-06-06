from django.db import models

# Create your models here.

class Snippet(models.Model):
    ROLE_CHOICES =(
    ("Mgr", "Manager"),
    ("Emp", "Employee"),
    ("Admin", "Administrator"),
    ("Sup", "Supervisor"),
    )
      
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    spirit_animal = models.CharField(max_length=100)
    roles = models.CharField(max_length=100, choices = ROLE_CHOICES)
    date_created=models.DateField()
    
    
    def __str__(self):
        return self.name
      
