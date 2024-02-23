from django.db import models

class Staff(models.Model):
    sId = models.AutoField(primary_key=True)
    sName = models.CharField(max_length=50)
    sProfile = models.CharField(max_length=20)
    sAge = models.IntegerField()
    sContact = models.CharField(max_length=10)
    sEmail = models.EmailField()
    sAddress = models.CharField(max_length=255)
    Types = [("M","Male"), ("F","Female"), ("O","Other"),]
    sGender = models.CharField(max_length=1, choices=Types)

    def __str__(self) -> str:
        return f'{self.sName}'

