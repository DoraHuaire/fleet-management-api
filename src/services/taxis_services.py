from src.models.taxi_models import Taxis

def get_filtered_taxis(plate, page, limit):
    query = Taxis.query
    # Filtrar por plate
    if plate:
        query = query.filter(Taxis.plate.ilike(f"%{plate}%"))
    
    taxis = query.paginate(page=page, per_page=limit).items
    return [taxi.convert_to_dictionary() for taxi in taxis]
