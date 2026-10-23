# Universidad CENFOTEC
# Curso: Principios de Programación 1
# Tarea 2
# Estudiante: Rachid Josué Angulo Rodríguez
# Problema 2: Registro de notas de un curso


# Constantes del programa
MAX_ESTUDIANTES = 30
NOTA_MINIMA = 0
NOTA_MAXIMA = 100
NOTA_APROBACION = 70


# Contadores y acumulador
cantidad_notas = 0
cantidad_aprobados = 0
cantidad_reprobados = 0
suma_notas = 0.0


# Encabezado del programa
print("=" * 45)
print("REGISTRO DE NOTAS DEL CURSO")
print("=" * 45)


# Solicitud inicial al usuario
respuesta_usuario = input(
    "¿Desea ingresar una nota? (s/n): "
).strip().lower()


# Validación de la respuesta inicial
while respuesta_usuario != "s" and respuesta_usuario != "n":
    print("Error: debe ingresar únicamente 's' o 'n'.")

    respuesta_usuario = input(
        "¿Desea ingresar una nota? (s/n): "
    ).strip().lower()


# Ciclo principal para registrar las notas
while respuesta_usuario == "s" and cantidad_notas < MAX_ESTUDIANTES:
    nota_estudiante = float(
        input(
            f"Ingrese la nota del estudiante "
            f"{cantidad_notas + 1} (0 a 100): "
        )
    )

    # Validación del rango permitido
    if NOTA_MINIMA <= nota_estudiante <= NOTA_MAXIMA:
        suma_notas += nota_estudiante
        cantidad_notas += 1

        # Clasificación de la nota
        if nota_estudiante >= NOTA_APROBACION:
            cantidad_aprobados += 1
            print("Resultado: estudiante aprobado.")
        else:
            cantidad_reprobados += 1
            print("Resultado: estudiante reprobado.")

        print(f"Notas válidas registradas: {cantidad_notas}")

    else:
        print(
            f"Error: la nota debe estar entre "
            f"{NOTA_MINIMA} y {NOTA_MAXIMA}."
        )

    # Verificación del límite máximo
    if cantidad_notas < MAX_ESTUDIANTES:
        respuesta_usuario = input(
            "¿Desea ingresar otra nota? (s/n): "
        ).strip().lower()

        # Validación de la respuesta para continuar
        while respuesta_usuario != "s" and respuesta_usuario != "n":
            print("Error: debe ingresar únicamente 's' o 'n'.")

            respuesta_usuario = input(
                "¿Desea ingresar otra nota? (s/n): "
            ).strip().lower()


# Presentación del resumen final
print()
print("=" * 45)
print("RESUMEN DEL CURSO")
print("=" * 45)
print(f"Notas válidas ingresadas: {cantidad_notas}")
print(f"Estudiantes aprobados: {cantidad_aprobados}")
print(f"Estudiantes reprobados: {cantidad_reprobados}")


# Cálculo seguro del promedio
if cantidad_notas > 0:
    promedio_notas = suma_notas / cantidad_notas
    print(f"Promedio general del grupo: {promedio_notas:.2f}")
else:
    print("Advertencia: no se ingresaron notas válidas.")


# Mensaje correspondiente al límite de estudiantes
if cantidad_notas == MAX_ESTUDIANTES:
    print("Se alcanzó el máximo permitido de estudiantes.")


print("=" * 45)
print("Programa finalizado.")