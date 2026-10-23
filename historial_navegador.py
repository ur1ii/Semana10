cabeza = None
cola = None
pagina_actual = None

def crear_nodo(dato):
    return {"dato": dato, "anterior": None, "siguiente": None}

def visitar_pagina(url):
    global cabeza, cola, pagina_actual
    nuevo = crear_nodo(url)
    
    if pagina_actual is None:
        cabeza = cola = pagina_actual = nuevo
    else:
        pagina_actual["siguiente"] = None
        cola = pagina_actual
        nuevo["anterior"] = pagina_actual
        pagina_actual["siguiente"] = nuevo
        pagina_actual = nuevo
        cola = nuevo
        
    print(f"Visitando: {pagina_actual['dato']}")

def retroceder():
    global pagina_actual
    if pagina_actual and pagina_actual["anterior"] is not None:
        pagina_actual = pagina_actual["anterior"]
        print(f"Retrocediste a: {pagina_actual['dato']}")
    else:
        print("No hay páginas anteriores en el historial.")

def avanzar():
    global pagina_actual
    if pagina_actual and pagina_actual["siguiente"] is not None:
        pagina_actual = pagina_actual["siguiente"]
        print(f"Avanzaste a: {pagina_actual['dato']}")
    else:
        print("No hay páginas siguientes en el historial.")

def mostrar_pagina_actual():
    if pagina_actual:
        print(f"Página actual: {pagina_actual['dato']}")
    else:
        print("No hay ninguna página abierta.")