class DatabaseRouter:
    """
    Router para manejar las operaciones de lectura/escritura en diferentes bases de datos
    """
    def db_for_read(self, model, **hints):
        """
        Todas las operaciones de lectura van a la base de datos de lectura
        """
        return 'lectura'

    def db_for_write(self, model, **hints):
        """
        Todas las operaciones de escritura van a la base de datos de escritura
        """
        return 'escritura'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Permitir relaciones entre objetos
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Asegurar que las migraciones solo se ejecuten en la base de datos default
        """
        return db == 'default'
