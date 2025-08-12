import re
from geopy.geocoders import Nominatim

def get_coordinates_from_text(text):
    pattern_web = r'https://waze\.com/ul\?ll=([0-9.]+),([0-9.]+)'
    pattern_app = r'waze://\?ll=([0-9.]+),([0-9.]+)'

    match_web = re.search(pattern_web, text)
    match_app = re.search(pattern_app, text)

    if match_web:
        latitude = match_web.group(1)
        longitude = match_web.group(2)
        return float(latitude), float(longitude)

    if match_app:
        latitude = match_app.group(1)
        longitude = match_app.group(2)
        return float(latitude), float(longitude)

    return None

def get_location_data_from_coordinates(latitude, longitude):
    geolocator = Nominatim(user_agent='MyGeoAPI/1.0 (your_email@example.com)')
    location = geolocator.reverse((latitude, longitude), exactly_one=True)

    if location:
        address = location.raw.get('address', {})
        data = {
            'full_address': location.address,
            'house_number': address.get('house_number', 'Null'),
            'road': address.get('road', 'Null'),
            'neighborhood': address.get('neighborhood', 'Null'),
            'suburb': address.get('suburb', 'Null'),
            'city': address.get('city', 'Null'),
            'town': address.get('town', 'Null'),
            'village': address.get('village', 'Null'),
            'county': address.get('county', 'Null'),
            'state': address.get('state', 'Null'),
            'postcode': address.get('postcode', 'Null'),
            'country': address.get('country', 'Null'),
            'latitude': location.latitude,
            'longitude': location.longitude,
            'osm_type': location.raw.get('osm_type', 'Null'),
            'osm_id': location.raw.get('osm_id', 'Null'),
            'importance': location.raw.get('importance', 'Null'),
        }
        return data
    return None

def get_geo(line):
    coordinates = get_coordinates_from_text(line)
    if coordinates:
        latitude, longitude = coordinates
        location_data = get_location_data_from_coordinates(latitude, longitude)
        if location_data['village'] != 'Null':
            return location_data['village']
        elif location_data['town'] != 'Null':
            return location_data['town']
        elif location_data['city'] != 'Null':
            return location_data['city']
        else:
            return location_data['full_address']
    else:
        return None