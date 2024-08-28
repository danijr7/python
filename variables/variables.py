numero = 5 #True/False, 5.35
string = "palabra"

#camelCase
primerNombre = "Daniel"
#snake_case (recomendado)
segundo_nombre = "Enrique"

#concatenar con f-strings
dice = f"Tu variable es {numero}." #convierte a texto cualquier variable

#concatenar con +
dice = "Tu variable es " + string + "."

del numero #"del" es un operador para borrar datos de la variable

print(dice)

#operadores de pertenencia
print("Tu" in dice) #mira si "String" esta en esa variable y responde con un True/False
print("Tu" not in dice) #mira si "String" no esta en esa variable y responde con un True/False\