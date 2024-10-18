from flask import request, jsonify
from models.trajectories_models import get_filtered_trajectories
from datetime import datetime
#from models.trajectories_models import taxi_exists

def init_routes_trajectories(app):
# Define el endpoint /trayectoias
    @app.route('/trajectories', methods=['GET'])
    def get_trajectories():
        # Obtenemos los parámetros de la solicitud
        taxi_id = request.args.get('taxiId')
        date = request.args.get('date')
        
        # Validamos de entrada
        if not taxi_id:
           return jsonify({"error": "El ID del taxi es obligatorio"}), 400
        
        if not date:
           return jsonify({"error": "La fecha es obligatoria"}), 400
        
    
        trajectories_list, error_message = get_filtered_trajectories(taxi_id, date)
        
        
        if error_message:
           return jsonify({"error": error_message}), 400
        
        if not trajectories_list:
           return jsonify({"error": "No se encontraron trayectorias para el taxi y fecha proporcionados"}), 404
        
        return jsonify(trajectories_list), 200
    
        