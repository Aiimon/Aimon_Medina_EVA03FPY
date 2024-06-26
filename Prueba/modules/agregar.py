from pathlib import Path
import json
ruta = Path('D:/carpeta.json')
def agregar_pintura():
    if not Path(ruta).exists():
        Path(ruta).touch()
    elif Path(ruta).exists():
        Path(ruta).unlink()
        Path(ruta).touch()
        