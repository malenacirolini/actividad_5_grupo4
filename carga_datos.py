# -*- coding: utf-8 -*-

def parsear_linea (linea: str)-> dict:
    """
  Recibe una línea del archivo CSV, la separa en campos y devuelve
  un diccionario con los datos del registro.

  Parámetros:
      linea (str): línea del archivo CSV.

  Retorna:
      dict: registro con los datos de una fila.
  """ 
    partes = linea.strip().split(",")
    
    # tiene la cantidad correcta de columnas
    if len(partes) != 5:
        raise ValueError("[ERROR CRÍTICO] Tipo de error encontrado: cantidad incorrecta de columnas | Ubicación: parsear_linea")
    
    registro = {
      "id_participante": partes[0],
      "fecha": partes[1],
      "app": partes[2],
      "cantidad_uso": partes[3],
      "tiempo_uso": partes[4]
      }

    return registro



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

    if  len(lineas) == 0:
       raise ValueError("[ERROR CRÍTICO] Tipo de error encontrado: el archivo está vacío | Ubicación: cargar_datos")
    
    # ● la línea no está vacía
    
    for linea in lineas:
        if linea.strip() == "":
            raise ValueError("[ERROR CRÍTICO] Tipo de error encontrado: línea vacía | Ubicación: cargar_datos")
        registro = parsear_linea(linea)
        id_participante = registro["id_participante"]
        
        if id_participante not in datos:
            datos[id_participante] = []
        
        datos[id_participante].append(registro)
        
    return datos
    
    
            


