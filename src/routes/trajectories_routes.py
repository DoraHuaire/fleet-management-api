from flask import Blueprint, request, jsonify
from src.services.trajectories_services import get_filtered_trajectories

trajectories_bp = Blueprint('trajectories', __name__)  

# Define el endpoint /trayectoias
@trajectories_bp.route('/trajectories', methods=['GET'])
def get_trajectories():
    # Obtener los parámetros de la solicitud
    taxiId = request.args.get('taxiId')
    date = request.args.get('date')
    
    if not taxiId or not date:
        return jsonify({"error": "taxiId y date son obligatorios"}), 400
    
    trajectories_list = get_filtered_trajectories(taxiId, date)
    
    return jsonify(trajectories_list)

