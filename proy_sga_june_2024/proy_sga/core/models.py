from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from proy_sga.utils import valida_cedula

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)

class BaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    objects = models.Manager()
    active_objects = ActiveManager()

    def delete(self):
        self.state = False
        self.save()

    class Meta:
        abstract = True

class Periodo(BaseModel):
    periodo = models.CharField(max_length=50)

    def __str__(self):
        return self.periodo

class Asignatura(BaseModel):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Profesor(BaseModel):
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Estudiante(BaseModel):
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Nota(BaseModel):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    def __str__(self):
        return f'Nota de {self.profesor} en {self.asignatura}'

class DetalleNota(BaseModel):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    nota = models.ForeignKey(Nota, on_delete=models.CASCADE)
    nota1 = models.FloatField()
    nota2 = models.FloatField()
    recuperacion = models.FloatField(null=True, blank=True)
    observacion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Detalle de {self.estudiante} - Nota: {self.nota.id}'
