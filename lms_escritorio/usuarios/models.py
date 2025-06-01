# usuarios/models.py
from mongoengine import Document, StringField,  ReferenceField,  FileField, DateTimeField
from mongoengine import Document, StringField, ValidationError
from datetime import datetime


class Usuario_admin(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)


# ESTUDIANTE
class Estudiante(Document):
    nombre = StringField(required=True)
    apellido = StringField(required=True)
    ci = StringField(required=True, unique=True)
    telefono = StringField()
    carrera = StringField()


# DOCENTE
class Docente(Document):
    nombre = StringField(required=True)
    apellido = StringField(required=True)
    ci = StringField(required=True, unique=True)
    telefono = StringField()
    profesion = StringField()

#MATERIA
class Materia(Document):
    nombre = StringField(required=True, unique=True)
    codigo = StringField(required=True, unique=True)

#TAREA
class Tarea(Document):
    titulo = StringField(required=True)
    descripcion = StringField(required=True)
    docente = ReferenceField(Docente) 
    nombre_docente = StringField()   


#SUBIR TAREA DE LA APP MOVIL ESTUDIANTE
class Entrega(Document):
    tarea = ReferenceField(Tarea, required=True)
    estudiante = ReferenceField(Estudiante, required=True)
    archivo = FileField()  # si quieres guardar archivo
    descripcion = StringField()  # o texto de entrega
    fecha_entrega = DateTimeField(default=datetime.utcnow)

