import os
import shutil

def _get_db_path() -> str:
    flet_storage = os.environ.get("FLET_APP_STORAGE_DATA")
    if flet_storage:
        os.makedirs(flet_storage, exist_ok=True)
        new_path = os.path.join(flet_storage, "kakebo.db")
        old_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kakebo.db")
        if os.path.exists(old_path) and not os.path.exists(new_path):
            shutil.move(old_path, new_path)
        return new_path
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "kakebo.db")

DB_NAME = _get_db_path()