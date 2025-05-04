from django.db import models

class Pup(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pup_images/')
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name

class AvailablePuppy(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank= True)
    image = models.ImageField(upload_to='available_pups/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.image.name