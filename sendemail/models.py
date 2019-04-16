from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    message = models.TextField(null = True, max_length=50)

    def __str__(self):
        return self.name
