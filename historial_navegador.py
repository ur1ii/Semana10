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
        
    print(f"✓ Visitando: {pagina_actual['dato']}")