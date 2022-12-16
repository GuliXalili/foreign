from django.db import models

class Rang(models.Model):
    nomi = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nomi
    
class Car(models.Model):
    nomi = models.CharField(max_length=20)
    rangi = models.ForeignKey(Rang, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomi
    
class Carr(models.Model):
    nomi = models.CharField(max_length=20)
    rangi = models.ForeignKey(Rang, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nomi
        
