#detectanto un numero CABA y ocultandolo

import re

texto = 'mi numero es: +54 11 4321-4321'
patron = r'\+54\s11\s\d{4}-\d{4}'

reemplazo = re.sub(patron,'*numero oculto*',texto)

print(reemplazo)