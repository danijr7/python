#cuantos cursos equivalen 10h del curso actual
horas_promedio = 4
horas_min = 2.5
horas_max = 7

equivalente_con_promedio = 10 / 4
equivalente_con_min = int(10 / 2.5)
equivalente_con_max = (((10 / 7) * 100) // 1) / 100
print(f'En 10hs del curso actual equivalen a {equivalente_con_promedio} cursos del promedio.')
print(f'En 10hs del curso actual equivalen a {equivalente_con_min} cursos del minimo.')
print(f'En 10hs del curso actual equivalen a {equivalente_con_max} cursos del maximo.')
print('----------------------------------------------------------------')

#10hs de otros cursos equivalen a los de este curso actual
equivalente_con_actual = (((10 / 1.5) * 100) // 1) / 100
print(f'En 10hs de otros cursos equivalen a {equivalente_con_actual} cursos del actual.')