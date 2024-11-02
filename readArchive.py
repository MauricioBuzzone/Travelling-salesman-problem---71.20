import pandas as pd
import folium
from geopy.geocoders import Nominatim
import time
import os
import webbrowser

# Leer el archivo CSV
csv_file_path = 'routes/lugares_buenos_aires.csv'  # Reemplaza con la ruta de tu archivo CSV
df = pd.read_csv(csv_file_path)

# Crear un mapa centrado en Buenos Aires
mapa = folium.Map(location=[-34.603722, -58.381592], zoom_start=12)

# Inicializar el geocodificador
geolocator = Nominatim(user_agent="geoapiExercises")

# Lista para almacenar las coordenadas
coordinates = []

# Iterar sobre cada fila del CSV para crear marcadores y obtener coordenadas
for index, row in df.iterrows():
    # Intentar convertir la dirección a coordenadas
    try:
        location = geolocator.geocode(row['Ubicación'])
        if location:
            lat, lon = location.latitude, location.longitude
            folium.Marker(
                location=[lat, lon],
                popup=f"{row['Nombre']} - Cierre: {row['Horario de Cierre']}",
                tooltip=row['Nombre']
            ).add_to(mapa)
            
            # Agregar las coordenadas a la lista
            coordinates.append([lat, lon])
        else:
            print(f"No se encontraron coordenadas para: {row['Ubicación']}")
    except Exception as e:
        print(f"Error al geocodificar {row['Ubicación']}: {e}")
    
    # Añadir una pausa para evitar que la API bloquee las solicitudes por exceso de uso
    time.sleep(1)

# Dibujar un camino (línea) entre las ubicaciones obtenidas
if len(coordinates) > 1:
    for i in range(len(coordinates) - 1):
        start = coordinates[i]
        end = coordinates[i + 1]
        
        # Dibujar la línea
        folium.PolyLine(locations=[start, end], color="blue", weight=2.5, opacity=1).add_to(mapa)

        # Calcular la posición de la flecha
        mid_point = [(start[0] + end[0]) / 2, (start[1] + end[1]) / 2]
        
        # Usar una imagen de flecha
        folium.Marker(
            location=mid_point,
            icon=folium.CustomIcon(icon_image="https://example.com/arrow.png", icon_size=(20, 20)),  # Cambia esta URL
            popup="Flecha"
        ).add_to(mapa)
# Guardar el mapa como un archivo HTML
mapa.save('mapa_lugares_buenos_aires.html')

print("Mapa guardado como 'mapa_lugares_buenos_aires.html'")


# Obtener la ruta completa del archivo HTML
file_path = os.path.abspath('mapa_lugares_buenos_aires.html')

# Abrir el archivo en el navegador
webbrowser.open(f'file://{file_path}')
