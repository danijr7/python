tiempo_crudo_actual = 3.5
tiempo_actual = 1.5
tiempo_crudo_promedio = 5
tiempo_promedio = 4

material_inservible_actual = int(100 - (tiempo_actual * 100) / tiempo_crudo_actual)
material_inservible_promedio = int(100 - (tiempo_promedio * 100) / tiempo_crudo_promedio)

print(f'El material inservible de este curso es de {material_inservible_actual}%')
print(f'El material inservible de los cursos promedio es de {material_inservible_promedio}%')