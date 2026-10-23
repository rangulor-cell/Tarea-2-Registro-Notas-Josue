# Tarea 2: Registro de notas de un curso

## Información general

- **Universidad:** CENFOTEC
- **Curso:** Principios de Programación 1
- **Trabajo:** Tarea 2
- **Estudiante:** Rachid Josué Angulo Rodríguez
- **Problema seleccionado:** Registro de notas de un curso

## Descripción

Este programa permite registrar las notas de un grupo de estudiantes.

Cada nota debe encontrarse entre 0 y 100. El programa clasifica a cada estudiante como aprobado o reprobado, calcula el promedio general del grupo y permite registrar un máximo de 30 estudiantes.

## Reglas del programa

- La nota mínima permitida es 0.
- La nota máxima permitida es 100.
- La nota mínima de aprobación es 70.
- La cantidad máxima de estudiantes es 30.
- Las notas inválidas no se cuentan ni se agregan al promedio.
- Si no se ingresan notas válidas, el programa muestra una advertencia.
- El programa finaliza cuando el usuario decide no continuar o cuando se alcanza el máximo de estudiantes.

## Conceptos utilizados

- Variables
- Constantes
- Condicionales
- Ciclos `while`
- Contadores
- Acumuladores
- Validación de datos
- Cálculo de promedio

## Archivo principal

El código fuente se encuentra en el archivo:

```text
registro_notas.py
```

## Ejecución

Para ejecutar el programa desde PowerShell:

```powershell
python registro_notas.py
```

## Casos de prueba

Se realizaron los siguientes casos de prueba:

1. Caso normal con tres notas.
2. Caso con cero iteraciones.
3. Caso con una sola iteración.
4. Caso límite con 30 estudiantes.

## Evidencias

Las capturas de las pruebas se encuentran dentro de la carpeta `evidencias`:

- `01_caso_normal.png`
- `02_cero_iteraciones.png`
- `03_una_iteracion.png`
- `04_caso_limite_30_estudiantes.png`

## Repositorio

- **Rama principal:** `main`
- **Archivo principal:** `registro_notas.py`