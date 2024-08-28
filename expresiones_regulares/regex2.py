import re

text = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

#el patron a buscar
pattern = r'\d{2}/\d{2}/\d{4}'
replacement = '*Fecha oculta*'
new_text = re.sub(pattern,replacement,text)

print(text)
print('*Texto modificado: ',new_text)