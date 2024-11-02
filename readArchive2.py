import os
import csv
import folium
import requests
import webbrowser

# Reemplaza 'YOUR_GOOGLE_API_KEY' con tu clave de API de Google
GOOGLE_API_KEY = 'AIzaSyBDaeWicvigtP9xPv919E-RNoxfvC-Hqik'
GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

# Función para obtener la latitud y longitud de una ubicación
def get_lat_long(location):
    params = {
        'address': location,
        'key': GOOGLE_API_KEY
    }
    response = requests.get(GEOCODE_URL, params=params)
    print(response)
    if response.status_code == 200:
        result = response.json()
        print(result)
        
        if result['status'] == 'OK':
            lat = result['results'][0]['geometry']['location']['lat']
            lng = result['results'][0]['geometry']['location']['lng']
            return lat, lng
    return None, None

# Leer el CSV y obtener coordenadas
places = []
with open('lugares.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['Nombre']
        location = row['Ubicación']
        lat, lng = get_lat_long(location)
        if lat and lng:
            places.append((name, lat, lng))

print(places)
# Crear un mapa con los lugares
map_center = [sum(place[1] for place in places) / len(places), sum(place[2] for place in places) / len(places)]
m = folium.Map(location=map_center, zoom_start=12)

for name, lat, lng in places:
    folium.Marker([lat, lng], popup=name).add_to(m)

# Guardar el mapa en un archivo HTML
m.save('mapa_lugares.html')


file_path = os.path.abspath('mapa_lugares.html')

# Abrir el archivo en el navegador
webbrowser.open(f'file://{file_path}')