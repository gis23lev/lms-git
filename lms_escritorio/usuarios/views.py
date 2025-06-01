# usuarios/views.py
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm, LoginForm
from .models import Usuario_admin
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from bson import ObjectId  # Asegúrate de importar esto si estás usando MongoDB
from .models import Estudiante

from .models import Docente

from .models import Materia

from .forms import DocenteLoginForm
from .models import Docente, Tarea
from .models import Entrega # O ajusta según tu estructura

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            if Usuario_admin.objects(username=form.cleaned_data['username']).first():
                messages.error(request, 'El nombre de usuario ya existe.')
            else:
                Usuario_admin(
                    username=form.cleaned_data['username'],
                    password=make_password(form.cleaned_data['password'])  # ← ahora se encripta
                ).save()
                messages.success(request, 'Usuario registrado correctamente.')
                return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = Usuario_admin.objects(username=form.cleaned_data['username']).first()
            if user and check_password(form.cleaned_data['password'], user.password):
                request.session['usuario_id'] = str(user.id)
                return redirect('dashboard')
            else:
                messages.error(request, 'Credenciales incorrectas.')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    request.session.flush()
    return redirect('login')

def dashboard_view(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    
    usuario = Usuario_admin.objects(id=ObjectId(usuario_id)).first()
    return render(request, 'usuarios/dashboard.html', {'usuario': usuario})


# VISTAS ESTUDIANTES
def estudiantes_view(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')

    estudiantes = Estudiante.objects()  # Todos los estudiantes
    return render(request, 'usuarios/estudiantes.html', {'estudiantes': estudiantes})

@csrf_exempt
def crear_estudiante_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            ci = data.get('ci')
            telefono = data.get('telefono')
            carrera = data.get('carrera')

            if not all([nombre, apellido, ci, telefono, carrera]):
                return JsonResponse({'success': False, 'message': 'Faltan campos requeridos.'}, status=400)

            # Validar que el CI contenga solo números
            if not str(ci).isdigit():
                return JsonResponse({'success': False, 'message': 'El campo CI debe contener solo números.'}, status=400)

            # Verificar si ya existe el estudiante con esa cédula
            if Estudiante.objects(ci=ci).first():
                return JsonResponse({'success': False, 'message': f'Ya existe un estudiante con la cédula {ci}.'}, status=400)

            estudiante = Estudiante(
                nombre=nombre,
                apellido=apellido,
                ci=ci,
                telefono=telefono,
                carrera=carrera
            )
            estudiante.save()

            return JsonResponse({
                'success': True,
                'message': 'Estudiante creado correctamente.',
                'estudiante': {
                    'id': str(estudiante.id),
                    'nombre': estudiante.nombre,
                    'apellido': estudiante.apellido,
                    'ci': estudiante.ci,
                    'telefono': estudiante.telefono,
                    'carrera': estudiante.carrera,
                }
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'JSON inválido.'}, status=400)

    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)

def crear_estudiante_view(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        ci = request.POST.get('ci')
        telefono = request.POST.get('telefono')
        carrera = request.POST.get('carrera')

        # Verificar si la cédula ya existe
        if Estudiante.objects(ci=ci).first():
            error = f'Ya existe un estudiante con la cédula {ci}.'
            return render(request, 'usuarios/crear_estudiante.html', {
                'error': error,
                'nombre': nombre,
                'apellido': apellido,
                'ci': ci,
                'telefono': telefono,
                'carrera': carrera
            })

        estudiante = Estudiante(
            nombre=nombre,
            apellido=apellido,
            ci=ci,
            telefono=telefono,
            carrera=carrera
        )
        estudiante.save()
        return redirect('estudiantes')  # redirige a la lista o donde quieras

    return render(request, 'usuarios/crear_estudiante.html')


def editar_estudiante_view(request, estudiante_id):
    estudiante = Estudiante.objects(id=ObjectId(estudiante_id)).first()

    if request.method == 'POST':
        estudiante.nombre = request.POST.get('nombre')
        estudiante.apellido = request.POST.get('apellido')
        estudiante.ci = request.POST.get('ci')
        estudiante.telefono = request.POST.get('telefono')
        estudiante.carrera = request.POST.get('carrera')
        estudiante.save()
        return redirect('estudiantes')

    return render(request, 'usuarios/editar_estudiante.html', {'estudiante': estudiante})


def eliminar_estudiante_view(request, estudiante_id):
    Estudiante.objects(id=ObjectId(estudiante_id)).delete()
    return redirect('estudiantes')

@csrf_exempt
def login_estudiante_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data.get('nombre')
        password = data.get('password')

        estudiante = Estudiante.objects(nombre=nombre).first()  # Buscar por nombre en vez de ci
        if estudiante and password == estudiante.ci:  # contraseña igual al ci
            return JsonResponse({
                'success': True,
                'estudiante': {
                    'nombre': estudiante.nombre,
                    'ci': estudiante.ci
                }
            })
        else:
            return JsonResponse({'success': False, 'message': 'Nombre o contraseña incorrectos'})

    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)



# VISTAS DOCENTES

def docentes_view(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')

    docentes = Docente.objects()  # Todos los docentes
    return render(request, 'usuarios/docentes.html', {'docentes': docentes})

@csrf_exempt
def crear_docente_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            ci = data.get('ci')
            telefono = data.get('telefono')
            profesion = data.get('profesion')

            if not all([nombre, apellido, ci]):
                return JsonResponse({'success': False, 'message': 'Faltan campos requeridos.'}, status=400)

            # Verificar si ya existe el docente con esa cédula
            if Docente.objects(ci=ci).first():
                return JsonResponse({'success': False, 'message': f'Ya existe un docente con la cédula {ci}.'}, status=400)

            docente = Docente(
                nombre=nombre,
                apellido=apellido,
                ci=ci,
                telefono=telefono,
                profesion=profesion
            )
            docente.save()

            return JsonResponse({
                'success': True,
                'message': 'Docente creado correctamente.',
                'docente': {
                    'id': str(docente.id),
                    'nombre': docente.nombre,
                    'apellido': docente.apellido,
                    'ci': docente.ci,
                    'telefono': docente.telefono,
                    'profesion': docente.profesion,
                }
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'JSON inválido.'}, status=400)

    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)

def crear_docente_view(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        ci = request.POST.get('ci')
        telefono = request.POST.get('telefono')
        profesion = request.POST.get('profesion')

        # Verificar si la cédula ya existe
        if Docente.objects(ci=ci).first():
            error = f'Ya existe un docente con la cédula {ci}.'
            return render(request, 'usuarios/crear_docente.html', {
                'error': error,
                'nombre': nombre,
                'apellido': apellido,
                'ci': ci,
                'telefono': telefono,
                'profesion': profesion
            })

        docente = Docente(
            nombre=nombre,
            apellido=apellido,
            ci=ci,
            telefono=telefono,
            profesion=profesion
        )
        docente.save()
        return redirect('docentes')  # redirige a la lista o donde quieras

    return render(request, 'usuarios/crear_docente.html')


def editar_docente_view(request, docente_id):
    docente = Docente.objects(id=ObjectId(docente_id)).first()

    if request.method == 'POST':
        docente.nombre = request.POST.get('nombre')
        docente.apellido = request.POST.get('apellido')
        docente.ci = request.POST.get('ci')
        docente.telefono = request.POST.get('telefono')
        docente.profesion = request.POST.get('profesion')
        docente.save()
        return redirect('docentes')

    return render(request, 'usuarios/editar_docente.html', {'docente': docente})


def eliminar_docente_view(request, docente_id):
    Docente.objects(id=ObjectId(docente_id)).delete()
    return redirect('docentes')



# MATERIAS
def materias_view(request):
    materias = Materia.objects.all()
    return render(request, 'usuarios/materias.html', {'materias': materias})

def crear_materia(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        codigo = request.POST['codigo']
        Materia(nombre=nombre, codigo=codigo).save()
        return redirect('materias')
    return render(request, 'usuarios/crear_materia.html')

def eliminar_materia(request, materia_id):
    Materia.objects(id=ObjectId(materia_id)).delete()
    return redirect('materias')



# LOGIN DOCENTE
def login_docente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ci = request.POST.get('ci')

        try:
            docente = Docente.objects.get(nombre=nombre, ci=ci)
            # Puedes guardar en sesión si quieres:
            request.session['docente_id'] = str(docente.id)
            request.session['docente_nombre'] = docente.nombre
            return redirect('dashboard_docente')  # Reemplaza por tu vista principal
        except Docente.DoesNotExist:
            return render(request, 'usuarios/login_docente.html', {
                'error': 'Nombre o CI incorrectos'
            })

    return render(request, 'usuarios/login_docente.html')


def dashboard_docente(request):
    if 'docente_id' not in request.session:
        return redirect('login_docente')

    docente_id = request.session['docente_id']
    docente = Docente.objects(id=docente_id).first()

    mensaje = None

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')

        if titulo and descripcion:
            Tarea(
                titulo=titulo,
                descripcion=descripcion,
                docente=docente,
                nombre_docente=docente.nombre  # <-- esto faltaba
            ).save()
            mensaje = "Tarea creada correctamente."
        else:
            mensaje = "Por favor, completa todos los campos."

    tareas = Tarea.objects(docente=docente)

    return render(request, 'usuarios/dashboard_docente.html', {
        'nombre': docente.nombre,
        'tareas': tareas,
        'mensaje': mensaje
    })
def eliminar_tarea(request, tarea_id):
    if 'docente_id' not in request.session:
        return redirect('login_docente')
    
    tarea = Tarea.objects(id=tarea_id).first()
    if tarea:
        tarea.delete()
    
    return redirect('dashboard_docente')

def logout_docente(request):
    request.session.flush()
    return redirect('login_docente')




def dashboard_estudiante(request):
    if 'estudiante_id' not in request.session:
        return redirect('login_estudiante')

    estudiante_id = request.session['estudiante_id']
    estudiante = Estudiante.objects(id=estudiante_id).first()

    # Mostrar todas las tareas de todos los docentes
    tareas = Tarea.objects()

    return render(request, 'usuarios/dashboard_estudiante.html', {
        'nombre': estudiante.nombre,
        'tareas': tareas
    })



#SUBIR TAREA DE LA APP MOVIL ESTUDIANTE
import datetime





def lista_tareas(request):
    tareas = Tarea.objects()
    data = []
    for tarea in tareas:
        data.append({
            'id': str(tarea.id),
            'titulo': tarea.titulo,
            'descripcion': tarea.descripcion,
            'nombre_docente': tarea.nombre_docente,
        })
    return JsonResponse(data, safe=False)


@csrf_exempt
def crear_entrega(request):
    if request.method == 'POST':
        tarea_id = request.POST.get('tarea_id')
        estudiante_id = request.POST.get('estudiante_id')
        descripcion = request.POST.get('descripcion', '')
        archivo = request.FILES.get('archivo')

        if not tarea_id or not estudiante_id:
            return JsonResponse({'error': 'Se requiere tarea_id y estudiante_id'}, status=400)

        try:
            tarea = Tarea.objects.get(id=tarea_id)
            estudiante = Estudiante.objects.get(id=estudiante_id)
        except:
            return JsonResponse({'error': 'Tarea o estudiante no encontrado'}, status=404)

        entrega = Entrega(
            tarea=tarea,
            estudiante=estudiante,
            descripcion=descripcion,
            fecha_entrega=datetime.utcnow()
        )

        if archivo:
            entrega.archivo.put(archivo, content_type=archivo.content_type, filename=archivo.name)

        entrega.save()
        return JsonResponse({'mensaje': 'Entrega registrada correctamente'}, status=201)

    return JsonResponse({'error': 'Método no permitido'}, status=405)