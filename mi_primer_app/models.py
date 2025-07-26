from django.db import models



# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default="apellido desconocido")
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    parentesco = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    
    

    def __str__(self):
        return f"{self.nombre} ({self.parentesco}) - {self.edad} años"
