# -*- coding: utf-8 -*-

def cargar_datos(ruta):
    '''
    Lee el archivo CSV y devuelve una lista de registros.

    Parametros:
        - ruta: ruta del archivo.

    Retorna:
        - list: lista de diccionarios con los registros del sistema.
    '''
    datos = []

    # ● la ruta existe, el archivo se puede abrir y no está vacío
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(
            "[ERROR CRÍTICO] Tipo de error encontrado: la ruta no existe o el archivo no se puede abrir | Ubicación: cargar_datos")

    # ● la línea no está vacía y tiene la cantidad correcta de columnas
    if  len(lineas) == 0:
       raise ValueError("[ERROR CRÍTICO] Tipo de error encontrado: el archivo está vacío | Ubicación: cargar_datos")
    

    numero_linea = 1
    for linea in lineas:
        if linea.strip() == "":
            raise ValueError("[ERROR CRÍTICO] Tipo de error encontrado: línea vacía | Ubicación: cargar_datos")

        partes = linea.strip().split(",")

        if len(partes) != 5:
            raise ValueError(f"[ERROR CRÍTICO] Tipo de error encontrado: cantidad incorrecta de columnas en la línea {numero_linea} | Ubicación: cargar_datos")
        
        registro = {
          "id_participante": partes[0],
          "fecha": partes[1],
          "app": partes[2],
          "cantidad_uso": partes[3],
          "tiempo_uso": partes[4]
      }

    datos.append(registro)
    numero_linea += 1
    
    return datos

