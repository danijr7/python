curso_actual = 1.5
curso_rapido = 2.5
curso_promedio = 4
curso_lento = 7

diferencia_porcentual_rapido = int(((curso_rapido - curso_actual) / curso_actual) * 100)
diferencia_porcentual_promedio = int(((curso_promedio - curso_actual) / curso_actual) * 100)
diferencia_porcentual_lento = int(((curso_lento - curso_actual) / curso_actual) * 100)

print(f'El curso minimo dura un {diferencia_porcentual_rapido}% mas que el actual.')
print(f'El curso promedio dura un {diferencia_porcentual_promedio}% mas que el actual.')
print(f'El curso maximo dura un {diferencia_porcentual_lento}% mas que el actual.')