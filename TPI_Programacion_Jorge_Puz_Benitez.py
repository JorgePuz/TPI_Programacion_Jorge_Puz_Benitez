import csv  # Modulo para que python pueda leer archivos CSV

ARCHIVO_CSV = "paises.csv"  # archivo donde guardamos los datos de los paises

# MÓDULO DE DATOS - Lectura y escritura del CSV

def cargar_paises():
    "Lee el archivo CSV y devuelve una lista de diccionarios."
    paises = []  # lista vacía

    try:
        with open(ARCHIVO_CSV, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)
                except (ValueError, KeyError):
                    print(f"  Fila inválida ignorada: {fila}")

    except FileNotFoundError:
        print(f"  Archivo '{ARCHIVO_CSV}' no encontrado. Se creará al agregar países.")

    return paises


def guardar_paises(paises):
    "Guarda la lista de países en el archivo CSV."
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises)
    print("  Datos guardados correctamente.")

# Validaciones

def pedir_entero(mensaje, minimo=0):
    "Pide un número entero al usuario y valida que sea válido."
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit() and int(valor) >= minimo:
            return int(valor)
        print(f"  Por favor ingrese un número entero válido (mínimo {minimo}).")

# Datos - Mostrar países

def listar_paises(paises):
    "Muestra todos los países en formato de tabla."
    if not paises:
        print("\n  No hay países cargados.")
        return

    print(f"\n  {'NOMBRE':<20} {'POBLACIÓN':>15} {'SUPERFICIE':>12} {'CONTINENTE':<12}")
    print("  " + "-"*62)
    for p in paises:
        print(f"  {p['nombre']:<20} {p['poblacion']:>15,} {p['superficie']:>12,} {p['continente']:<12}")
    print(f"\n  Total: {len(paises)} país/es.")

# MÓDULO DE DATOS - Agregar y actualizar

def agregar_pais(paises):
    "Agrega un nuevo país a la lista."
    print("\n--- AGREGAR PAÍS ---")

    while True:
        nombre = input("  Nombre del país: ").strip()
        if not nombre:
            print("  El nombre no puede estar vacío.")
            continue

        # Verificamos que no exista un país con ese nombre
        existe = False
        for p in paises:
            if p["nombre"].lower() == nombre.lower():
                existe = True
                break

        if existe:
            print(f"  '{nombre}' ya existe en el sistema.")
        else:
            break

    poblacion = pedir_entero("  Población: ", minimo=1)
    superficie = pedir_entero("  Superficie en km²: ", minimo=1)

    while True:
        continente = input("  Continente: ").strip()
        if continente:
            break
        print("  El continente no puede estar vacío.")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    print(f"  '{nombre}' agregado correctamente.")


def actualizar_pais(paises):
    "Actualiza población y superficie de un país existente."
    print("\n--- ACTUALIZAR PAÍS ---")

    nombre = input("  Nombre del país a actualizar: ").strip()

    pais_encontrado = None
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            pais_encontrado = p
            break

    if not pais_encontrado:
        print(f"  No se encontró '{nombre}'.")
        return

    print(f"\n  Datos actuales de {pais_encontrado['nombre']}:")
    print(f"    Población:  {pais_encontrado['poblacion']:,}")
    print(f"    Superficie: {pais_encontrado['superficie']:,} km²")

    pais_encontrado["poblacion"] = pedir_entero("  Nueva población: ", minimo=1)
    pais_encontrado["superficie"] = pedir_entero("  Nueva superficie en km²: ", minimo=1)

    print(f"  '{pais_encontrado['nombre']}' actualizado correctamente.")

# BÚSQUEDAS

def buscar_pais(paises):
    "Busca países por nombre, coincidencia parcial o exacta."
    print("\n--- BUSCAR PAÍS ---")

    termino = input("  Ingresá el nombre o parte del nombre: ").strip()

    if not termino:
        print("  Ingresá al menos un caracter para buscar.")
        return

    resultados = []
    for p in paises:
        if termino.lower() in p["nombre"].lower():
            resultados.append(p)

    if not resultados:
        print(f"  No se encontraron países con '{termino}'.")
    else:
        print(f"\n  Se encontraron {len(resultados)} resultado/s:")
        listar_paises(resultados)

# FILTROS

def filtrar_por_continente(paises):
    "Filtra por continente."
    continente = input("  Ingresá el continente: ").strip()

    if not continente:
        print("  El continente no puede estar vacío.")
        return

    resultados = []
    for p in paises:
        if p["continente"].lower() == continente.lower():
            resultados.append(p)

    if not resultados:
        print(f"  No se encontraron países en '{continente}'.")
    else:
        print(f"\n  Países en {continente}:")
        listar_paises(resultados)

def filtrar_por_poblacion(paises):
    "Filtra países por rango de población."
    print("  Ingresá el rango de población:")
    minimo = pedir_entero("    Mínimo: ", minimo=0)
    maximo = pedir_entero("    Máximo: ", minimo=0)

    if minimo > maximo:
        print("  El mínimo no puede ser mayor que el máximo.")
        return

    resultados = []
    for p in paises:
        if minimo <= p["poblacion"] <= maximo:
            resultados.append(p)

    if not resultados:
        print(f"  No hay países con población entre {minimo:,} y {maximo:,}.")
    else:
        print(f"\n  Países con población entre {minimo:,} y {maximo:,}:")
        listar_paises(resultados)

def filtrar_por_superficie(paises):
    "Filtra países por rango de superficie."
    print("  Ingresá el rango de superficie en km²:")
    minimo = pedir_entero("    Mínimo: ", minimo=0)
    maximo = pedir_entero("    Máximo: ", minimo=0)

    if minimo > maximo:
        print("  El mínimo no puede ser mayor que el máximo.")
        return

    resultados = []
    for p in paises:
        if minimo <= p["superficie"] <= maximo:
            resultados.append(p)

    if not resultados:
        print(f"  No hay países con superficie entre {minimo:,} y {maximo:,} km².")
    else:
        print(f"\n  Países con superficie entre {minimo:,} y {maximo:,} km²:")
        listar_paises(resultados)

def menu_filtros(paises):
    "Submenú de filtros."
    print("\n--- FILTRAR PAÍSES ---")
    print("  1. Por continente")
    print("  2. Por rango de población")
    print("  3. Por rango de superficie")

    opcion = input("  Elegí una opción: ").strip()

    if opcion == "1":
        filtrar_por_continente(paises)
    elif opcion == "2":
        filtrar_por_poblacion(paises)
    elif opcion == "3":
        filtrar_por_superficie(paises)
    else:
        print("  Opción inválida.")

# MÓDULO DE ORDENAMIENTO

def ordenar_burbuja(paises, clave, descendente=False):
    "Ordena la lista usando el algoritmo de burbuja."
    lista = paises[:]  # Copia para no modificar la original
    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if clave == "nombre":
                valor_a = lista[j]["nombre"].lower()
                valor_b = lista[j + 1]["nombre"].lower()
            elif clave == "poblacion":
                valor_a = lista[j]["poblacion"]
                valor_b = lista[j + 1]["poblacion"]
            else:
                valor_a = lista[j]["superficie"]
                valor_b = lista[j + 1]["superficie"]

            if descendente:
                if valor_a < valor_b:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                if valor_a > valor_b:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def menu_ordenamiento(paises):
    "Submenú de ordenamiento."
    print("\n--- ORDENAR PAÍSES ---")
    print("  1. Por nombre")
    print("  2. Por población")
    print("  3. Por superficie")

    opcion = input("  Elegí criterio: ").strip()

    if opcion not in ("1", "2", "3"):
        print("  Opción inválida.")
        return

    if opcion in ("2", "3"):
        orden = input("  ¿Orden? (a=ascendente / d=descendente): ").strip().lower()
        descendente = orden == "d"
    else:
        descendente = False

    if opcion == "1":
        resultado = ordenar_burbuja(paises, "nombre", descendente)
    elif opcion == "2":
        resultado = ordenar_burbuja(paises, "poblacion", descendente)
    else:
        resultado = ordenar_burbuja(paises, "superficie", descendente)

    listar_paises(resultado)

# ESTADÍSTICAS

def mostrar_estadisticas(paises):
    "Muestra estadísticas generales del dataset."
    print("\n--- ESTADÍSTICAS ---")

    if not paises:
        print("  No hay países cargados.")
        return

    mayor_pob = paises[0]
    menor_pob = paises[0]
    mayor_sup = paises[0]
    menor_sup = paises[0]
    total_pob = 0
    total_sup = 0

    for p in paises:
        total_pob += p["poblacion"]
        total_sup += p["superficie"]

        if p["poblacion"] > mayor_pob["poblacion"]:
            mayor_pob = p
        if p["poblacion"] < menor_pob["poblacion"]:
            menor_pob = p
        if p["superficie"] > mayor_sup["superficie"]:
            mayor_sup = p
        if p["superficie"] < menor_sup["superficie"]:
            menor_sup = p

    promedio_pob = total_pob // len(paises)
    promedio_sup = total_sup // len(paises)

    continentes = {}
    for p in paises:
        c = p["continente"]
        if c in continentes:
            continentes[c] += 1
        else:
            continentes[c] = 1

    print(f"\n  Población:")
    print(f"    Mayor:    {mayor_pob['nombre']} ({mayor_pob['poblacion']:,} hab.)")
    print(f"    Menor:    {menor_pob['nombre']} ({menor_pob['poblacion']:,} hab.)")
    print(f"    Promedio: {promedio_pob:,} hab.")

    print(f"\n  Superficie:")
    print(f"    Mayor:    {mayor_sup['nombre']} ({mayor_sup['superficie']:,} km²)")
    print(f"    Menor:    {menor_sup['nombre']} ({menor_sup['superficie']:,} km²)")
    print(f"    Promedio: {promedio_sup:,} km²")

    print(f"\n  Países por continente:")
    for continente, cantidad in continentes.items():
        print(f"    {continente:<15} {cantidad} país/es")

# MENÚ PRINCIPAL

def mostrar_menu():
    "Muestra las opciones disponibles en pantalla."
    print("\n" + "="*45)
    print("   GESTIÓN DE DATOS DE PAÍSES")
    print("="*45)
    print("  1. Agregar un país")
    print("  2. Actualizar población y superficie")
    print("  3. Buscar país por nombre")
    print("  4. Filtrar países")
    print("  5. Ordenar países")
    print("  6. Mostrar estadísticas")
    print("  7. Listar todos los países")
    print("  0. Salir")
    print("="*45)

def main():
    "Función principal que arranca el programa."
    print("Cargando datos...")
    paises = cargar_paises()
    print(f"  {len(paises)} países cargados correctamente.")

    while True:
        mostrar_menu()
        opcion = input("  Ingresá una opción: ").strip()

        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            menu_filtros(paises)
        elif opcion == "5":
            menu_ordenamiento(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            listar_paises(paises)
        elif opcion == "0":
            guardar_paises(paises)
            print("\n  Hasta luego!\n")
            break
        else:
            print("  Opción inválida. Ingresá un número del 0 al 7.")

# ENTRADA DEL PROGRAMA

if __name__ == "__main__":
    main()