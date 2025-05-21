from django.db import migrations

def crear_datos_iniciales(apps, schema_editor):
    Rol = apps.get_model('core', 'Rol')
    EstadoCita = apps.get_model('core', 'EstadoCita')

    # Crear roles
    roles = [
        ('admin', 'Administrativo'),
        ('medico', 'Médico'),
        ('paciente', 'Paciente'),
    ]
    for nombre, descripcion in roles:
        Rol.objects.create(nombre=nombre, descripcion=descripcion)

    # Crear estados de cita
    estados = [
        ('PENDIENTE', 'Pendiente'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]
    for nombre, descripcion in estados:
        EstadoCita.objects.create(nombre=nombre, descripcion=descripcion)

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_datos_iniciales),
    ]
