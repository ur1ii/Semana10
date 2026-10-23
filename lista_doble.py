cabeza = None
cola = None

def crear_nodo(dato):
    return {"dato": dato, "anterior": None, "siguiente": None}

def agregar_final(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)
    if cabeza is None:
        cabeza = nuevo
        cola = nuevo
    else:
        nuevo["anterior"] = cola
        cola["siguiente"] = nuevo
        cola = nuevo

agregar_final("Inicio")
agregar_final("Catálogo")
agregar_final("Contacto")

def mostrar_adelante():
    actual = cabeza
    while actual is not None:
        print(actual["dato"], end=" ↔ " if actual["siguiente"] else "\n")
        actual = actual["siguiente"]

def mostrar_atras():
    actual = cola
    while actual is not None:
        print(actual["dato"], end=" ↔ " if actual["anterior"] else "\n")
        actual = actual["anterior"]

mostrar_adelante()
mostrar_atras()

def agregar_inicio(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)
    if cabeza is None:
        cabeza = cola = nuevo
    else:
        nuevo["siguiente"] = cabeza
        cabeza["anterior"] = nuevo
        cabeza = nuevo

agregar_inicio("Bienvenida")
mostrar_adelante()
mostrar_atras()

def eliminar(dato):
    global cabeza, cola
    actual = cabeza
    while actual is not None and actual["dato"] != dato:
        actual = actual["siguiente"]
    if actual is None:
        return False

    anterior = actual["anterior"]
    siguiente = actual["siguiente"]
    if anterior is None:
        cabeza = siguiente
    else:
        anterior["siguiente"] = siguiente
    if siguiente is None:
        cola = anterior
    else:
        siguiente["anterior"] = anterior
    return True

print("Eliminado:", eliminar("Catálogo"))
mostrar_adelante()
mostrar_atras()

def buscar(dato):
    pasos_cabeza = 0
    encontrado_cabeza = False
    actual_cabeza = cabeza
    while actual_cabeza is not None:
        pasos_cabeza += 1
        if actual_cabeza["dato"] == dato:
            encontrado_cabeza = True
            break
        actual_cabeza = actual_cabeza["siguiente"]

    pasos_cola = 0
    encontrado_cola = False
    actual_cola = cola
    
    while actual_cola is not None:
        pasos_cola += 1
        if actual_cola["dato"] == dato:
            encontrado_cola = True
            break
        actual_cola = actual_cola["anterior"]

    print(f"--- Búsqueda de '{dato}' ---")
    print(f" • Desde cabeza : {'Encontrado' if encontrado_cabeza else 'No encontrado'} ({pasos_cabeza} iteraciones)")
    print(f" • Desde cola   : {'Encontrado' if encontrado_cola else 'No encontrado'} ({pasos_cola} iteraciones)")

    return encontrado_cabeza

print("Resultado:", buscar("Bienvenida")) 
print("Resultado:", buscar("Contacto"))   
print("Resultado:", buscar("Productos"))

def insertar_despues(referencia, dato):
    global cabeza, cola
    actual = cabeza
    while actual is not None:
        actual = actual["siguiente"]

    if actual is None:
        return False
    nuevo = crear_nodo(dato)
    siguiente_nodo = actual["siguiente"]

    nuevo["anterior"] = actual
    nuevo["siguiente"] = siguiente_nodo
    actual["siguiente"] = nuevo

    if siguiente_nodo is None:
        cola = nuevo
    else:
        siguiente_nodo["anterior"] = nuevo
    return True

print("Insertado:", insertar_despues("Inicio", "Ofertas"))  
print("Insertado:", insertar_despues("Blog", "Novedades"))   
mostrar_adelante()