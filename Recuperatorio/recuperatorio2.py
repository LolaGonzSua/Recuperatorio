#Función para inicializar la matriz de la ppt
def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

#1.Cargar votos
def cargar_votos(matriz: list) -> None:
    for i in range(5):
        nro_lista = int(input(f"Ingrese el número de la lista {i + 1} (tres cifras): "))
        while nro_lista < 100 or nro_lista > 999:  # Validación de número de lista de 3 cifras
            print("El número de lista debe ser de tres cifras. Intente nuevamente.")
            nro_lista = int(input(f"Ingrese el número de la lista {i + 1} (tres cifras): "))
        
        turno_mañana = int(input(f"Ingrese la cantidad de votos en el turno mañana para la lista {nro_lista}: "))
        while turno_mañana < 0:
            print("La cantidad de votos no puede ser negativa. Intente nuevamente.")
            turno_mañana = int(input(f"Ingrese la cantidad de votos en el turno mañana para la lista {nro_lista}: "))
        
        turno_tarde = int(input(f"Ingrese la cantidad de votos en el turno tarde para la lista {nro_lista}: "))
        while turno_tarde < 0:
            print("La cantidad de votos no puede ser negativa. Intente nuevamente.")
            turno_tarde = int(input(f"Ingrese la cantidad de votos en el turno tarde para la lista {nro_lista}: "))
        
        turno_noche = int(input(f"Ingrese la cantidad de votos en el turno noche para la lista {nro_lista}: "))
        while turno_noche < 0:
            print("La cantidad de votos no puede ser negativa. Intente nuevamente.")
            turno_noche = int(input(f"Ingrese la cantidad de votos en el turno noche para la lista {nro_lista}: "))
        
        matriz[i] = [nro_lista, turno_mañana, turno_tarde, turno_noche]

#2. Mostrar votos
def mostrar_votos(matriz: list) -> None:
    total_votos = 0
    for i in range(5):
        total_votos += matriz[i][1] + matriz[i][2] + matriz[i][3]
    
    print("\nVotos de cada lista:")
    print(f"{'Nro Lista':<10}{'Mañana':<15}{'Tarde':<15}{'Noche':<15}{'Porcentaje':<15}")
    for i in range(5):
        lista = matriz[i][0]
        votos_mañana = matriz[i][1]
        votos_tarde = matriz[i][2]
        votos_noche = matriz[i][3]
        total = votos_mañana + votos_tarde + votos_noche
        porcentaje = (total / total_votos) * 100 if total_votos > 0 else 0
        print(f"{lista:<10}{votos_mañana:<15}{votos_tarde:<15}{votos_noche:<15}{porcentaje:>14}%")

#3. Ordenar votos Turno Mañana
def ordenar_por_votos_mañana(matriz: list) -> None:
    print("La lista del Turno Mañana ANTES de ordenar:")
    for fila in matriz:
        print(fila)  

    for i in range(4): 
        for j in range(4 - i):  
            if matriz[j][1] < matriz[j + 1][1]:  
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]  

    print("La lista del Turno Mañana DESPUES de ordenar:")
    for fila in matriz:
        print(fila)  



#4. Listas que tengan el 5% o menos
def no_te_voto_nadie(matriz: list) -> None:
    total_votos = 0
    for i in range(5):
        total_votos += matriz[i][1] + matriz[i][2] + matriz[i][3]
    
    print("\nListas con menos del 5% de los votos:")
    for i in range(5):
        total_lista = matriz[i][1] + matriz[i][2] + matriz[i][3]
        porcentaje = (total_lista / total_votos) * 100 if total_votos > 0 else 0
        if porcentaje < 5:
            print(f"Lista {matriz[i][0]} con {total_lista} votos ({porcentaje: }%)")
    
    print(f"No hubo otra lista con menos del 5%")

#5. Turno que más fue a votar
def turno_mas_votado(matriz: list) -> None:
    total_mañana = 0
    total_tarde = 0
    total_noche = 0
    for i in range(5):
        total_mañana += matriz[i][1]
        total_tarde += matriz[i][2]
        total_noche += matriz[i][3]
    
    
    if total_mañana > total_tarde and total_mañana > total_noche:
        print("\nEl turno con más participación fue el turno mañana.")
    if total_tarde > total_mañana and total_tarde > total_noche:
        print("\nEl turno con más participación fue el turno tarde.")
    if total_noche > total_mañana and total_noche > total_tarde:
        print("\nEl turno con más participación fue el turno noche.")
    if total_mañana == total_tarde and total_mañana > total_noche:
        print("\nLos turnos con más participación fueron el turno mañana y tarde.")
    if total_mañana == total_noche and total_mañana > total_tarde:
        print("\nLos turnos con más participación fueron el turno mañana y noche.")
    if total_tarde == total_noche and total_tarde > total_mañana:
        print("\nLos turnos con más participación fueron el turno tarde y noche.")

#6. Ballotage 
def verificar_segunda_vuelta(matriz: list) -> bool:
    total_votos = 0
    for i in range(5):
        total_votos += matriz[i][1] + matriz[i][2] + matriz[i][3]
    
    mayor_voto = 0
    mayor_lista = -1
    
    for i in range(5):
        total_lista = matriz[i][1] + matriz[i][2] + matriz[i][3]
        if total_lista > mayor_voto:
            mayor_voto = total_lista
            mayor_lista = i
    
    if mayor_voto / total_votos > 0.5:
        return False  #no hay segunda vuelta
    return True

#7. Realizar segunda vuelta
def segunda_vuelta(matriz: list) -> None:
    
    print("\nRealizando segunda vuelta...")
    
    lista_1 = 0
    lista_2 = 0
    max_voto_1 = 0
    max_voto_2 = 0
    
    for i in range(5):
        total_votos_lista = matriz[i][1] + matriz[i][2] + matriz[i][3]
        if total_votos_lista > max_voto_1:
            max_voto_2 = max_voto_1
            lista_2 = lista_1
            max_voto_1 = total_votos_lista
            lista_1 = i
        elif total_votos_lista > max_voto_2:
            max_voto_2 = total_votos_lista
            lista_2 = i
    
    total_votos_segunda_vuelta = 0
    for i in range(3):
        total_votos_segunda_vuelta += int(input(f"Ingrese la cantidad de votos en el turno mañana (segunda vuelta): "))
        total_votos_segunda_vuelta += int(input(f"Ingrese la cantidad de votos en el turno tarde (segunda vuelta): "))
        total_votos_segunda_vuelta += int(input(f"Ingrese la cantidad de votos en el turno noche (segunda vuelta): "))
    
    votos_candidato_1 = 0
    votos_candidato_2 = 0
    for i in range(total_votos_segunda_vuelta):
        if i % 2 == 0:
            votos_candidato_1 += 1
        else:
            votos_candidato_2 += 1
    
    print(f"\nVotos en segunda vuelta:")
    print(f"Lista {matriz[lista_1][0]}: {votos_candidato_1}")
    print(f"Lista {matriz[lista_2][0]}: {votos_candidato_2}")
    
    if votos_candidato_1 > votos_candidato_2:
        print(f"Ganador de la segunda vuelta: Lista {matriz[lista_1][0]}")
    else:
        print(f"Ganador de la segunda vuelta: Lista {matriz[lista_2][0]}")



#menú principal
def menu():
    matriz = inicializar_matriz(5, 4, 0)  #inicializamos la matriz con 5 listas y 4 columnas
    while True:
        print("\n--- MENU DE ELECCIONES ---")
        print("1. Cargar votos")
        print("2. Mostrar votos")
        print("3. Ordenar votos por turno mañana")
        print("4. Listas con menos del 5% de los votos")
        print("5. Turno con más participación")
        print("6. Verificar si hay segunda vuelta")
        print("7. Realizar segunda vuelta")
        print("8. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            cargar_votos(matriz)
        elif opcion == 2:
            mostrar_votos(matriz)
        elif opcion == 3:
            ordenar_por_votos_mañana(matriz)
            
        elif opcion == 4:
            no_te_voto_nadie(matriz)
        elif opcion == 5:
            turno_mas_votado(matriz)
        elif opcion == 6:
            if verificar_segunda_vuelta(matriz):
                print("\nHubo segunda vuelta.")
            else:
                print("\nNo hubo segunda vuelta.")
        elif opcion == 7:
            segunda_vuelta(matriz)
        elif opcion == 8:
            print("Saliendo. . .")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

#llamamos al menú
menu()
