import re

# Leer el archivo de países
with open('ejercicios_txt/un_members.txt', 'r', encoding='UTF-8') as lista_paises:
    contenido = lista_paises.read()
    paises = contenido.split('\n')

lista_paises_dict = []

# Procesar cada país en la lista
for pais in paises:
    if not pais.strip():  # Ignorar líneas en blanco
        continue
    try:
        codigo, info = re.split(':', pais, 1)
        detalles = info.split(',')
        pais_dict = {
            'codigo': codigo.strip(),
            'pais': detalles[0].strip(),
            'capital': detalles[1].strip(),
            'dominio': detalles[2].strip(),
            'poblacion': int(detalles[3].strip())
        }
        lista_paises_dict.append(pais_dict)
    except ValueError:
        print(f"Línea con formato incorrecto: {pais}")

# Ordenar la lista de países por población en orden descendente
lista_paises_ordenada = sorted(lista_paises_dict, key=lambda x: x['poblacion'], reverse=True)

# Mostrar los países ordenados
for pais in lista_paises_ordenada:
    print(f"{pais['pais']}: {pais['poblacion']}")

# Si quieres escribir los países ordenados a un archivo
with open('ejercicios_txt/paises_ordenados_por_poblacion.txt', 'w', encoding='UTF-8') as archivo:
    for pais in lista_paises_ordenada:
        archivo.write(f"{pais['codigo']}: {pais['pais']},{pais['capital']},{pais['dominio']},{pais['poblacion']}\n")
