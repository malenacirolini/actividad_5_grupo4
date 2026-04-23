Actividad 5 - Grupo 4

Integrantes
- Sofia Moreno
- Malena Cirolini
- Carmin Bausili
- Justina Franzini

**Descripción:** Este proyecto implementa un sistema de carga y validación de datos desde archivos CSV con manejo de errores.

------------------------------------------------------------------------------------------------------------------------------------------------
**Ejecución**
1. Colocar el archivo CSV dentro de la carpeta `datos/`
2. Ejecutar el programa con el siguiente comando: python main.py

Manejo de errores: El sistema valida los datos durante la carga y procesamiento del archivo.
Ante la detección de un error, la ejecución se detiene inmediatamente y se muestra un mensaje en consola con el siguiente formato:
[ERROR CRÍTICO] Tipo de error encontrado: <descripción> | Ubicación: <función>

------------------------------------------------------------------------------------------------------------------------------------------------
Entre las validaciones realizadas se incluyen:
- Verificación de existencia y contenido del archivo
- Validación de tipos de datos
- Control de valores negativos o fuera de rango
- Validación de campos obligatorios
- Control de categorías válidas
- Verificación de orden en la variable tiempo

------------------------------------------------------------------------------------------------------------------------------------------------
**Modelado del Sistema con Objetos**
Para una futura implementación utilizando Programación Orientada a Objetos, el sistema podría modelarse mediante las siguientes clases:

**Clase Participante**
- Representa a cada participante del sistema.
- *Atributos:*
    - id: int --> identificador único del participante
    - nombre: str --> nombre del participante
 - *Métodos:*
   - validar_id(): verifica que el ID sea positivo y válido
   
------------------------------------------------------------------------------------------------------------------------------------------------
**Clase Registro**
- Representa cada fila de datos del archivo CSV.
- *Atributos:* 
    - tiempo: float --> instante de tiempo del registro
    - coordenada_x: float --> posición en eje X
    - coordenada_y: float --> posición en eje Yc
    - app: str --> categoría o aplicación utilizada
- *Métodos:*
    - validar_datos(): verifica que los datos sean correctos
    - validar_rango(): controla que los valores estén dentro de los límites permitidos
    - es_valido(): indica si el registro puede ser utilizado para cálculos

------------------------------------------------------------------------------------------------------------------------------------------------
**Clase Sistema**
- Encargada de la lógica principal del programa.
- *Atributos:*
    - datos: list --> lista de registros cargados desde el CSV
    - participantes: list --> lista de participantes detectados
- *Métodos:*
    - cargar_datos(ruta): carga el archivo CSV
    - validar_datos(): ejecuta todas las validaciones necesarias
    - procesar_datos(): prepara la información para su análisis
 
