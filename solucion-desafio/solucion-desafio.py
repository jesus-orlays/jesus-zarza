# Solicita al usuario que ingrese 5 calificaciones
calificaciones = []
for i in range(5):
            calificacion = float(input(f'Ingrese la calificación {i + 1}: '))
            calificaciones.append(calificacion)

# Calcula el promedio de las calificaciones
promedio = sum(calificaciones) / len(calificaciones)

# Determina el estado según el promedio
if promedio >= 60:
    estado = "Aprobado"
elif 40 <= promedio < 60:
    estado = "En recuperación"
else:
    estado = "Reprobado"

# Imprime el resultado
print(f'El promedio es: {promedio}')
print(f'El estado es: {estado}')
