from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(null=True , blank=True , default='09000000000', max_length=11)
    address = models.CharField(max_length=256 , null=True , blank=True)
    

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"