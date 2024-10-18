from flask import request, jsonify
from models.taxi_models import get_filtered_taxis

def init_routes_taxis(app):
# Definimos el endpoint /taxis
    @app.route('/taxis', methods=['GET'])
    def get_taxis():
    # Obtenemos los parámetros de la solicitud
        id = request.args.get('id', type=int)
        plate = request.args.get('plate', '') 
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)  
        limit = request.args.get('limit', 10, type=int)  
        
    # Llamamos a la función del servicio
        taxis_list = get_filtered_taxis(id, plate, page, per_page, limit)
        
    # Devolver los taxis en formato JSON
        return jsonify(taxis_list)