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
def validar_codigo(codigo, cartelera):
    return len(codigo.strip()) > 0 and not buscar_codigo (codigo, cartelera )
def validar_titulo(titulo):
    return len(titulo.strip()) > 0

def validar_genero(genero):
    return len(genero.strip()) > 0

def validar_duracion(duracion):
    return duracion > 0

def validar_clasificacion(clasificacion):
    return clasificacion in ['A', 'B', 'C']

def validar_idioma(idioma):
    return len(idioma.strip()) > 0

def validar_es_3d(es_3d):
    return es_3d.lower() in ['s', 'n']

def validar_precio(precio):
    return precio > 0

def validar_cupos(cupos):
    return cupos >= 0
def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
    cod_upper = codigo.upper()
    if buscar_codigo(cod_upper, cartelera):
        return False
    valor_3d = True if es_3d.lower() == 's' else False
    peliculas[cod_upper] = [titulo, genero, duracion, clasificacion, idioma, valor_3d]
    cartelera[cod_upper] = [precio, cupos]
    return True
def eliminar_pelicula(codigo, peliculas, cartelera):
    cod_upper = codigo.upper()
    if buscar_codigo(cod_upper, cartelera):
        del peliculas[cod_upper]
        del cartelera[cod_upper]
        return True
    return False
def mostrar_menu():
    print("\n ================== MENU PRINCIPAL ====================")
    print("1. cupos por genero ")
    print("2. busqueda de peliculas por rango de precio ")
    print("3. actualizar precio de pelicula")
    print("4. agregar pelicula")
    print("5. eliminar pelicula")
    print("6. salir")
    print("=========================================================")
    