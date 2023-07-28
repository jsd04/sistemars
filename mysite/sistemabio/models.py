
# Create your models here.
import datetime

from django.db import models
from django.utils import timezone


from django.contrib import admin
# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    ap_paterno = models.CharField(max_length=15)
    ap_materno = models.CharField(max_length=15)
    #   user = models.ForeignKey(User)
    curp = models.CharField(max_length=30)
     # domicilio
    piso = models.IntegerField()
     # type: Number,
    departamento = models.IntegerField()
     # type: Number,
    telefono = models.CharField(max_length=15)
     # type: String, models.IntegerField()
    correo = models.EmailField()
    #  type: String,
    fecha_nac = models.DateField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    # Campos con opciones
    CATALOGO_PERFIL = [
        ('1', 'Administrador'),
        ('2', 'Usuario Inquilino'),
        ('3', 'Usuario Visitante'),
        ('4', 'Usuario Trabajador'),
    ]
    id_perfil = models.CharField(max_length=2, choices=CATALOGO_PERFIL, default='2')
    # Campos con opciones
    CATALOGO_STATUS = [
        ('1', 'ALTA/COMPLETO'),
        ('2', 'BAJA'),
        ('3', 'PENDIENTE'),
        ('4', 'ALTA/COMPLETO'),
    ]
    id_status = models.CharField(max_length=2, choices=CATALOGO_STATUS, default='3')

    def __str__(self):
        return self.nombre


# class Usuario_Sesion(models.Model):
#     id_sesion = models.AutoField(primary_key=True)
#     id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     CATALOGO_TIPO_SESION = [
#         ('1', 'FACIAL'),
#         ('2', 'VOZ'),
#         ('3', 'HUELLA'),
#         ('4', 'NORMAL'),
#     ]
#     id_tipo_sesion = models.CharField(max_length=2, choices=CATALOGO_TIPO_SESION, default='4')
#     CATALOGO_STATUS_SESION = [
#         ('0', 'NO REGISTRADO'),
#         ('1', 'REGISTRADO'),
#     ]
#     id_status_sesion = models.CharField(max_length=2, choices=CATALOGO_STATUS_SESION, default='0')


# class Usuario_Tipo_Sesion(models.Model):
#     id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     id_tipo_sesion = models.ForeignKey(Usuario_Sesion, on_delete=models.CASCADE)
#     image = models.BinaryField()



