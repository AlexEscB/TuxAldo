import os
import shutil

def _get_db_path() -> str:
    # Lee las variables de entorno del sistema. En Android, Flet inyecta
    # FLET_APP_STORAGE_DATA con la ruta de almacenamiento persistente de la app.
    # En desktop no existe, así que retorna None.
    flet_storage = os.environ.get("FLET_APP_STORAGE_DATA")

    if flet_storage:
        # Crea el directorio si no existe. Si ya existe, no hace nada.
        os.makedirs(flet_storage, exist_ok=True)

        # Ruta nueva donde vivirá la DB en Android (sobrevive actualizaciones del APK)
        new_path = os.path.join(flet_storage, "kakebo.db")

        # Si hay una DB en la ruta vieja y aún no existe en la nueva, la mueve.
        # Solo ocurre una vez, en la primera actualización.
        old_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kakebo.db")
        if os.path.exists(old_path) and not os.path.exists(new_path):
            shutil.move(old_path, new_path)

        return new_path

    # Fallback para desktop: construye la ruta a partir de la ubicación
    # de este archivo (config.py) y le agrega el nombre de la DB al final.
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "kakebo.db")

DB_NAME = _get_db_path()

needs_refresh = False