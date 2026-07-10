def leer_opcion():
    while True:
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
    genero_buscado = genero.strip().lower()
    for cod, datos in peliculas.items():
        if datos[1].strip().lower() == genero_buscado:
            if cod in cartelera:
                total_cupos += cartelera[cod][1]
    print(f"El total de cupos disponibles es: {total_cupos}")
def busqueda_precio(p_min, p_max, peliculas, cartelera):
    encontradas = []
    for cod, datos in cartelera.items():
        precio = datos = [0]
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
    print("1. Cupos por genero ")
    print("2. Busqueda de peliculas por rango de precio ")
    print("3. Actualizar precio de pelicula")
    print("4. Agregar pelicula")
    print("5. Eliminar pelicula")
    print("6. Salir")
    print("=========================================================")
    def main():
      peliculas = {
        'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
        'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
        'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
        'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
        'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
        'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False]
      }
    
      cartelera = {
        'P101': [5990, 40],
        'P102': [7990, 0],
        'P103': [4990, 25],
        'P104': [6990, 12],
        'P105': [8990, 8],
        'P106': [7490, 3]
      }
      while True:
          mostrar_menu()
          opcion = leer_opcion()

          if opcion == 1:
            genero = input("Ingrese género a consultar: ")
            cupos_genero(genero, peliculas, cartelera)

          elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        break
                    else:
                        print("Rango inválido. Intente nuevamente.")
                except ValueError:
                    print("Debe ingresar valores enteros")
                busqueda_precio(p_min, p_max, peliculas, cartelera)
          elif opcion == 3:
             continuar = 's'
             while continuar.lower() == 's':
                codigo = input("Ingrese código de película: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio > 0:
                        if actualizar_precio(codigo, nuevo_precio, cartelera):
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                    else:
                        print("El precio debe ser mayor a cero.")
                except ValueError:
                    print("Debe ingresar un valor entero para el precio.")
                
                continuar = input("¿Desea actualizar otro precio (s/n)?: ")
          elif opcion == 4:
             codigo = input("Ingrese código de película: ")
             if not validar_codigo(codigo, cartelera):
                print("Error: Código inválido o ya existe.")
                continue
            
             titulo = input("Ingrese título: ")
             if not validar_titulo(titulo):
                print("Error: Título inválido.")
                continue
                
             genero = input("Ingrese género: ")
             if not validar_genero(genero):
                print("Error: Género inválido.")
                continue
                
             try:
                duracion = int(input("Ingrese duración (minutos): "))
                if not validar_duracion(duracion):
                    print("Error: Duración inválida.")
                    continue
             except ValueError:
                print("Error: Duración debe ser un número entero.")
                continue
                
             clasificacion = input("Ingrese clasificación: ")
             if not validar_clasificacion(clasificacion):
                print("Error: Clasificación inválida.")
                continue
             idioma = input("Ingrese idioma: ")
             if not validar_idioma(idioma):
                 print("Error: Idioma inválido.")
                 continue
             es_3d = input("¿Es 3D? (s/n): ")
             if not validar_es_3d(es_3d):
                print("Error: Opción 3D inválida.")
                continue
             try:
                precio = int(input("Ingrese precio: "))
                if not validar_precio(precio):
                    print("Error: Precio inválido.")
                    continue
             except ValueError:
                print("Error: Precio debe ser un número entero.")
                continue
                
