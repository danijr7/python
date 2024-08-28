nombre = 'dani'

with open('archivos\\miNombre.txt','w',encoding='UTF-8') as file:
    file.write(f'my name is {nombre}')

file.close()