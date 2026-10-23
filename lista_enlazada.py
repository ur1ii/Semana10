def crear_nodo(dato):
    return {"dato": dato, "siguiente": None}

def apilar(tope, dato):
    nuevo = crear_nodo(dato)
    nuevo["siguiente"] = tope
    return nuevo

def desapilar(tope):
    if not tope:
        print("Error: La pila está vacía.")
        return None, None
    dato_retirado = tope["dato"]
    nuevo_tope = tope["siguiente"]
    return nuevo_tope, f"Dato desapilado: {dato_retirado}"

def ver_tope(tope):
    if not tope:
        return None
    return tope["dato"]

def mostrar(tope):
    actual = tope
    print("Tope -> ", end="")
    while actual is not None:
        print(f"[{actual['dato']}]", end=" -> ")
        actual = actual["siguiente"]
    print("None")
    
pila = []
pila = crear_nodo("Hola")
pila = apilar(pila, "Messi")
pila = apilar(pila, "20")
pila, "20" == desapilar(pila)

print(pila)
print(ver_tope(pila))
print(desapilar(pila))
print(ver_tope(pila))

