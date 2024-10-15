from flask import request, jsonify
from models.trajectories_models import get_filtered_trajectories
from datetime import datetime

def init_routes_trajectories(app):
# Define el endpoint /trayectoias
    @app.route('/trajectories', methods=['GET'])
    def get_trajectories():
        # Obtener los parámetros de la solicitud
        taxiId = request.args.get('taxiId')
        date = request.args.get('date')
        
        if not taxiId:
           return jsonify({"error": "El ID del taxi es obligatorio"}), 400

        if not date:
           return jsonify({"error": "La fecha es obligatoria"}), 400
         
        try:
            date = datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            return jsonify({"error": "Fecha invalida, por favor usa el formato DD-MM-YYYY"}), 400
    
        
        trajectories_list = get_filtered_trajectories(taxiId, date)
        
        return jsonify(trajectories_list)

