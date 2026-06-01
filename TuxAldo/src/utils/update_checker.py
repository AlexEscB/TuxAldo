import urllib.request
import json
from version import APP_VERSION

def check_for_update():
    """
    Consulta la API de GitHub y compara la versión actual con la última publicada.
    Devuelve (hay_actualizacion, version_nueva, url_descarga) o None si falla.
    """
    try:
        url = "https://api.github.com/repos/AlexEscB/TuxAldo/releases/latest"
        req = urllib.request.Request(url, headers={"User-Agent": "TuxAldo"})
        
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read())
        
        latest_version = data["tag_name"].lstrip("v")  # "v0.1.1" → "0.1.1"
        download_url = data["html_url"]
        
        hay_actualizacion = latest_version != APP_VERSION
        
        return hay_actualizacion, latest_version, download_url
    
    except Exception:
        return None