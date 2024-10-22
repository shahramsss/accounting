from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)
    phone = models.IntegerField()
    address = models.CharField(max_length=256)
    

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"