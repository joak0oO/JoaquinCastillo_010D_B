def leer_opcion()
    while true:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe  seleccionar una opcion valida")
        except ValueError:
            print("Debe seleccionar una opcion valida")
def cupos_genero (genero, peliculas, cartelera):
    total_cupos = 0
    genero_buscado = genero_strip().lower()
    for cod, datos in peliculas_items():
        if datos[1].strip().lower() == genero_buscado:
            if cod in cartelera:
                total_cupos += cartelera[cod][1]
    print(f"El total de cupos disponibles es: {total_cupos}")
def busqueda_precio(p_min, p_max, peliculas, cartelera):
    encontradas = []
    for cod, datos in cartelera.items():
        precio_datos = [0]
        cupos = datos[1]
        if p_min <= precio <= p_max and cupos > 0:
            if cod in peliculas:
                titulo = peliculas[cod][0]
                encontradas.append(f"{titulo}--{cod}")

    if encontradas:
        encontradas.sort()
        print(f"Las películas encontradas son: {encontradas}")
    else:
        print("No hay películas en ese rango de precios.")

def buscar_codigo(codigo, cartelera):
    return codigo.upper() in cartelera

def actualizar_precio(codigo, nuevo_precio, cartelera):
    cod_upper = codigo.upper()
    if buscar_codigo(cod_upper, cartelera):
        cartelera[cod_upper][0] = nuevo_precio
        return True
    return False