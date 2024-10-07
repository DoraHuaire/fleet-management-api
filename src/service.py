from models import Taxis

def get_filtered_taxis(plate=None, page=1, limit=10):
    query = Taxis.query
    if plate:
        query = query.filter(Taxis.plate.ilike(f"%{plate}%"))
    
    taxis = query.paginate(page=page, per_page=limit).items
    return [taxi.convert_to_dictionary() for taxi in taxis]