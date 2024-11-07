from flask import Blueprint

# Inicializa el blueprint sin importar `create_app`
api = Blueprint('api', __name__)

# Importa rutas después de definir el blueprint
from . import routes
