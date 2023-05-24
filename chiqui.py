#Importo la librería random como rnd
import random as rnd

# Función Auxiliar 1
# Esta función la usa goles
# Toma dos equipos, que son una lista o tupla de dos elementos: el primero es el nombre del equipo y el segundo es la efectividad.
# Devuelve una tupla de tres elementos: el primero es la probabilidad de que meta gol el equipo A, el segundo la probabilidad de que no haya goles y el tercero la probabilidad de que meta gol el equipo B.
def probabilidades_de_gol(equipoA, equipoB):
    _,probabilidadA = equipoA
    _,probabilidadB = equipoB
    # Pa * (1 - Pb)
    golA = probabilidadA/100 * (1-probabilidadB/100)
    # Pb * (1 - Pa)
    golB = probabilidadB/100 * (1-probabilidadA/100)
    # 1 - PgolA - PgolB
    empate = 1 - golA - golB
    return golA, empate, golB

#Función Auxiliar 1
# Toma dos equipos, que son una lista o tupla de dos elementos: el primero es el nombre del equipo y el segundo es la efectividad.
# Devuelve A si mete gol A, B si mete gol B, E si no mete gol ninguno.
#EquipoA = [equipo, efect]
def jugada(equipoA,equipoB):
    victoriaA, empate, victoriaB = probabilidades_de_gol(equipoA, equipoB)
    resultado = rnd.choices(["A", "E", "B"], [victoriaA, empate, victoriaB])[0]
    return(resultado)

#Funcion Auxiliar 2
#Esta función se usa en ordenar_tabla, ignorar
def orden_en_tabla(equipo):
    _,puntos,GF,GC = equipo
    return puntos, GF-GC, GF

#Esta es la función que van a usar: Toma una tabla de posiciones y la ordena de mayor a menor según los criterios de desempate.
#La tabla de posiciones es una lista de listas, donde cada lista interna tiene cuatro elementos: el primero es el nombre del equipo, el segundo es la cantidad de puntos, el tercero es la cantidad de goles a favor y el cuarto es la cantidad de goles en contra.
def ordenar_tabla(tabla):
    return sorted(tabla, key=orden_en_tabla, reverse=True)

def simular_jugadas(a, b, cantidad_jugadas):
    lista_goles = []
    puntosA = 0
    puntosB = 0

    for i in range(cantidad_jugadas):
        gol = jugada(a, b)
        if gol == "A":
            puntosA = puntosA +1
        if gol == "B":
            puntosB = puntosB +1
        lista_goles.append(gol)
    return puntosA, puntosB

def simular_jugadas_Laves(a, b):
    lista_goles = []
    puntosA = 0
    puntosB = 0

    for i in range(4):
        gol = jugada(a, b)
        if gol == "A":
            puntosA = puntosA +1
        if gol == "B":
            puntosB = puntosB +1
        lista_goles.append(gol)

    if puntosA==puntosB: #Si al cabo de las 4 jugadas de arriba, estan empatados ambos equipos,
        for i in range(2): #Se hacen 2 jugadas mas
            gol = jugada(a, b)
            if gol == "A":
                puntosA = puntosA +1
            if gol == "B":
                puntosB = puntosB +1
            lista_goles.append(gol)

    #Si al cabo de esas 6 jugadas, ambos equipos siguen teniendo igual cantidad de goles, se hacen jugadas hasta que un equipo mete gol
    return puntosA, puntosB
lista_equipos = [("River", 78),("Boca", 37),("Independiente", 40),("Racing", 55),("San Lorenzo", 64),("Banfield", 17),("Velez", 47),("Huracán", 21)]

def correr_lista(lista_elegida):
    
    lista_ganadores =[]
    for i in range(0, len(lista_elegida), 2):
        
        a= lista_elegida[i]
        b = lista_elegida [i+1] 
        #ganador 
        puntosA,puntosB = simular_jugadas(a, b, 4)
        print(f"Inicial {a[0]}:{puntosA} | {b[0]}:{puntosB}")
        if puntosA == puntosB:
            dpuntosA, dpuntosB = simular_jugadas(a, b, 2)
            puntosA = puntosA + dpuntosA
            puntosB = puntosB + dpuntosB
            print(f"Tiempo extra {a[0]}:{puntosA} | {b[0]}:{puntosB}")
        while puntosA == puntosB:
            #gol de oro
            dpuntosA, dpuntosB = simular_jugadas(a, b, 1)
            puntosA = puntosA + dpuntosA
            puntosB = puntosB + dpuntosB
            print(f"Gol de oro {a[0]}:{puntosA} | {b[0]}:{puntosB}")
        if puntosA>puntosB: 
            #ganador = a
            print(f"El ganador es {a[0]}")
            lista_ganadores.append(a)
        elif puntosB>puntosA:
            #ganador = b 
            print(f"El ganador es {b [0]}")
            lista_ganadores.append(b)

    return lista_ganadores


def sacar_estadistica(lista_elec):
    equipos_solonombres = []
    for tuplas in lista_elec:
        equipos_solonombres.append(tuplas[0])
    return equipos_solonombres

ganadores1 = correr_lista(lista_equipos)
print(f"los ganadores de la primera ronda son {sacar_estadistica(ganadores1)}")

ganadores2 = correr_lista(ganadores1)

print(f"Los ganadores de la ronda 2 son {sacar_estadistica(ganadores2)}")
ganadores3= correr_lista(ganadores2)
print(f"El ganador es {sacar_estadistica(ganadores3)}")


def campeonato(lista_elegida):
    marcador = []
    for i in lista_elegida:
        marcador.append([i[0],0,0,0])
    for a in range(len(lista_elegida)):
        for b in range(a+1, len(lista_elegida), 1):
            puntosA, puntosB = simular_jugadas(lista_elegida[a], lista_elegida[b], 4) 
            a[2] = puntosA + a[2]
            b[2] = puntosB + b[2]
            if puntosA>puntosB: 
                a[1] = a[1] + 3
                #a[2] = a[2] + (puntosA - puntosB)
            elif puntosB>puntosA:
                b[1] = b[1] + 3
                #b[2] = b[2] + (puntosB - puntosA)
            elif puntosA == puntosB:
                b[1] = b[1] + 1
                a[1] = a[1] + 1
            

            
