from flask import request, jsonify
from models.users_models import get_filtered_users,  connection_db_create_user

def init_routes_users(app):
    @app.route('/users', methods=['GET'])  # Asegúrate de que esta ruta está registrada
    def get_users():
    # Obtenemos los parámetros de la solicitud
        page = request.args.get('page', "1")
        per_page = request.args.get('per_page', "5")
        limit = request.args.get('limit', 10)
        
        try:
            # Convertimos los parámetros a enteros
            page = int(page)
            per_page = int(per_page)
            limit = int(limit) if limit is not None else 10
        # Validamos que page, per_page y limit sean números positivos
            if page <= 0 or per_page <= 0 or limit <= 0:
                return jsonify({'error': 'Error, parámetros deben ser positivos'}), 400
        except ValueError:
        # Si alguno de los parámetros no es un número válido, devolvemos un error 400
            return jsonify({'error': 'Error, página y límite inválidos'}), 400  
        
        # Llamamos a la función get_filtered_users y devolvemos código 200
        users_list = get_filtered_users(page, per_page, limit)
        
        return jsonify(users_list), 200
    
    
    @app.route('/users', methods=['POST'])
    def create_new_user():
        """
        Crea un nuevo usuario en la base de datos a partir de los datos proporcionados en la solicitud.

        Este endpoint recibe un cuerpo JSON con los datos del usuario, como nombre, correo, etc., 
        y los utiliza para crear un nuevo usuario en la base de datos.
        """
        # Obtener datos del usuario de la solicitud
        user_data = request.get_json()
        # Llama a la función para crear un usuario y devolver la respuesta
        db_response = connection_db_create_user(user_data)
        return db_response






    