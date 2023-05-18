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

lista_goles = []
puntosA = 0
puntosB = 0

for i in range(4):
    gol = jugada(("River", 79), ("Boca", 48))
    print(gol)
    if gol == "A":
        puntosA = puntosA +1
    if gol == "B":
        puntosA = puntosB +1
    lista_goles.append(gol)
    
print("River: " + str(puntosA) + " Boca: " + str(puntosB))


