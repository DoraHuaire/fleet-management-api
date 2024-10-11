from flask import Blueprint, request, jsonify
from src.services.trajectories_services import get_filtered_trajectories
from datetime import datetime

trajectories_bp = Blueprint('trajectories', __name__)  

# Define el endpoint /trayectoias
@trajectories_bp.route('/trajectories', methods=['GET'])
def get_trajectories():
    # Obtener los parámetros de la solicitud
    taxiId = request.args.get('taxiId')
    date = request.args.get('date')
    
    if taxiId:
        try:
            taxiId = int(taxiId)
        except ValueError:
            return jsonify({"error": "taxiId debe ser un número"}), 400
        
    if date:
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "La fecha debe estar en formato YYYY-MM-DD"}), 400
    
    trajectories_list = get_filtered_trajectories(taxiId, date)
    
    return jsonify(trajectories_list)

