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

def menu():
    while True:
        print("\n" + "="*30)
        print("      MENÚ DEL NAVEGADOR")
        print("="*30)
        print("1. Visitar nueva página")
        print("2. Retroceder")
        print("3. Avanzar")
        print("4. Mostrar página actual")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        print("-" * 30)

        if opcion == "1":
            url = input("Ingresa la URL o nombre de la página: ")
            if url:
                visitar_pagina(url)
            else:
                print("x La URL no puede estar vacía.")
        elif opcion == "2":
            retroceder()
        elif opcion == "3":
            avanzar()
        elif opcion == "4":
            mostrar_pagina_actual()
        elif opcion == "5":
            print("Saliendo del navegador...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()