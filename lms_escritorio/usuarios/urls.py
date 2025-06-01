from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),  # Redirige la raíz a login
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

    path('estudiantes/', views.estudiantes_view, name='estudiantes'),
    path('estudiantes/crear/', views.crear_estudiante_view, name='crear_estudiante'),
    path('estudiantes/editar/<str:estudiante_id>/', views.editar_estudiante_view, name='editar_estudiante'),
    path('estudiantes/eliminar/<str:estudiante_id>/', views.eliminar_estudiante_view, name='eliminar_estudiante'),
    path('api/estudiante/login/', views.login_estudiante_api, name='login_estudiante_api'),
    path('api/estudiante/crear/', views.crear_estudiante_api, name='crear_estudiante_api'),


    path('docentes/', views.docentes_view, name='docentes'),
    path('docentes/crear/', views.crear_docente_view, name='crear_docente'),
    path('docentes/editar/<str:docente_id>/', views.editar_docente_view, name='editar_docente'),
    path('docentes/eliminar/<str:docente_id>/', views.eliminar_docente_view, name='eliminar_docente'),

    # Opcionalmente API para crear con JSON
    path('api/docentes/crear/', views.crear_docente_api, name='crear_docente_api'),


    path('materias/', views.materias_view, name='materias'),
    path('materias/crear/', views.crear_materia, name='crear_materia'),
    path('materias/eliminar/<str:materia_id>/', views.eliminar_materia, name='eliminar_materia'),


    path('docente/login/', views.login_docente, name='login_docente'),
    path('docente/dashboard/', views.dashboard_docente, name='dashboard_docente'),
    
    
    path('dashboard/eliminar_tarea/<str:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('logout_docente/', views.logout_docente, name='logout_docente'),



    path('api/tareas/', views.lista_tareas, name='lista_tareas'),
    path('api/entrega/', views.crear_entrega, name='crear_entrega'),
    ]
