from flask import request, jsonify
from app import app
from services import get_filtered_taxis

# Define el endpoint /taxis
@app.route('/taxis', methods=['GET'])
def get_taxis():
    # Obtener los parámetros de la solicitud
    plate = request.args.get('plate')
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    # Llamar a la función del servicio
    taxis_list = get_filtered_taxis(plate=plate, page=page, limit=limit)
    
    return jsonify(taxis_list)