
cabeza = []
def crear_nodo(dato):
    return {"dato": dato, "siguiente": None}

def insertar_inicio(cabeza, dato):
    nuevo = crear_nodo(dato)
    nuevo["siguiente"] = cabeza
    return nuevo

def insertar_final(cabeza, dato):
    nuevo = crear_nodo(dato)
    if cabeza is None:
        return nuevo
    actual = cabeza
    while actual["siguiente"] is not None:
        actual = actual["siguiente"]
    actual["siguiente"] = nuevo
    return cabeza

cabeza = print(crear_nodo("Marcelo"))
cabeza = print(insertar_inicio("Marcelo", "Jose"))
print(insertar_final(cabeza, "Manuel"))

def mostrar(cabeza):
    actual = cabeza
    while actual is not None:
        print(actual["dato"], end=" → ")
        actual = actual["siguiente"]
    print("None")