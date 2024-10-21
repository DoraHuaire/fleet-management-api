from flask import jsonify
from models.latest_models import get_latest_trajectories

def init_routes_trajectories_latest(app):
# Define el endpoint /trayectoias/latest    
    @app.route('/trajectories/latest', methods=['GET'])
    def get_latest_trajectories_route():
        # Obtiene las trayectorias más recientes
        latest_trajectories_result = get_latest_trajectories()
        return jsonify(latest_trajectories_result)
        