from django.db import migrations

def crear_estados_roles(apps, schema_editor):
    EstadoCita = apps.get_model('core', 'EstadoCita')
    RolUsuario = apps.get_model('core', 'RolUsuario')

    # Crear estados de cita
    estados = [
        ('PENDIENTE', 'Pendiente'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]
    for nombre, desc in estados:
        EstadoCita.objects.create(nombre=nombre, descripcion=desc)

    # Crear roles de usuario
    roles = [
        ('admin', 'Administrativo'),
        ('medico', 'Médico'), 
        ('paciente', 'Paciente'),
    ]
    for nombre, desc in roles:
        RolUsuario.objects.create(nombre=nombre, descripcion=desc)

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_estados_roles),
    ]
