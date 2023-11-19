from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=50)
    variant = models.CharField(max_length=50)
    engine = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    mat = [ 
        ('yes','INSURED '),
        ('no','NOT INSURED '),
    ]
    insured = models.CharField(max_length=3 , choices=mat )
    pic = models.ImageField(null = True)
    addpic = models.ImageField(null= True, blank= True)
    price = models.PositiveBigIntegerField(null = True , blank= True)
    Mileage = models.PositiveIntegerField(help_text= "In KMs", null = True, blank = True)
    
    contact  = models.EmailField(null = True)


    def save(self, *args, **kwargs):
        print(f"Data Updated for {self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

            