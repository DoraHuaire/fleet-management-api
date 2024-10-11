from flask import Blueprint, request, jsonify
from src.services.taxis_services import get_filtered_taxis

taxis_bp = Blueprint('taxis', __name__) 

# Definimos el endpoint /taxis
@taxis_bp.route('/taxis', methods=['GET'])
def get_taxis():
    
# Obtenemos los parámetros de la solicitud
    plate = request.args.get('plate', '') 
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)  
    limit = request.args.get('limit', per_page, type=int)  
    
# Llamamos a la función del servicio
    taxis_list = get_filtered_taxis(plate, page, per_page, limit)
    
# Devolver los taxis en formato JSON
    return jsonify(taxis_list)