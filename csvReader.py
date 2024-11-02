import csv

NAME=0
LOCATION=1
CLOSEAT = 2

def read(path):
    i = 0
    places = {}
    try:
        with open(path, mode='r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo)

            for row in reader:
                if len(row) < 3:
                    print("Advertencia: Fila con menos de 3 columnas, saltando...")
                    continue
                places[i] = {
                    "name": row[NAME],
                    "location": row[LOCATION],
                    "closeAt": row[CLOSEAT]
                }
                i+=1

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{path}'.")  
    return places