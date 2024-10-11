from src.models.taxi_models import Taxis

def get_filtered_taxis(plate, page, per_page, limit):
    query = Taxis.query
    
# Filtrar por plate, si se especifica
    if plate:
        query = query.filter(Taxis.plate.ilike(f"%{plate}%"))
    
# ajustamos los límites
    if limit < 1 or limit > 10:
        limit = per_page

# aplicamos la paginación y definimos límites
    taxis = query.offset((page - 1) * per_page).limit(limit).all()

# convertimos taxis a disccionarios
    return [taxi.convert_to_dictionary() for taxi in taxis]
