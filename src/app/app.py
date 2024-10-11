from flask import Flask
from src.database.db import db  # Importa db desde el nuevo archivo
from src.database.config import Config

# Inicializar Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos con la app
db.init_app(app)

# Importar y registrar los blueprints
from src.routes.taxis_routes import taxis_bp
from src.routes.trajectories_routes import trajectories_bp

app.register_blueprint(taxis_bp)
app.register_blueprint(trajectories_bp)

if __name__ == '__main__':
    app.run(debug=True)