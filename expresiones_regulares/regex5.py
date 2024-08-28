import re

text = 'este es un ejemplo de una pagina web: http://www.example.com'

pattern = 'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

result = re.findall(pattern,text)

print(result)