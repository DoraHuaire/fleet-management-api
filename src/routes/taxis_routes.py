from flask import Blueprint, request, jsonify
from src.services.taxis_services import get_filtered_taxis

taxis_bp = Blueprint('taxis', __name__) 

# Define el endpoint /taxis
@taxis_bp.route('/taxis', methods=['GET'])
def get_taxis():
    # Obtener los parámetros de la solicitud
    plate = request.args.get('plate')
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    # Llamar a la función del servicio
    taxis_list = get_filtered_taxis(plate, page, limit)
    
    return jsonify(taxis_list)