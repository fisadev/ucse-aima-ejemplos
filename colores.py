from csp import CSP, backtracking_search

#  +-----+-------+-------+---+
#  |  A  |       |       | G |
#  |     |     D |       +---+
#  |  +--+----+  |   E       |
#  |  |   C   |  |           |
#  |--+----+  +--+-----------+
#  |       +--+  |           |
#  |   B   |     +--+    F   |  +---+
#  |       |        |        |  | H |
#  +-------+        +--------+  +---+

# variables del problema
variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# dominio de cada variable
dominios = dict((variable, ['ROJO', 'VERDE', 'AZUL'])
                for variable in variables)

# vecinos de vada variable
vecinos = {'A': ['B', 'C', 'D'],
           'B': ['A', 'C'],
           'C': ['A', 'B', 'D'],
           'D': ['A', 'C', 'E'],
           'E': ['D', 'F', 'G'],
           'F': ['E'],
           'G': ['E'],
           'H': []}

# restricciones - nos llaman preguntando:
# "La variable A con valor a, anda bien con la variable B con valor b?"
# (OJO! en A recibimos un string con el nombre de la variable, o sea que
# en A puede venir 'A', 'B', 'C', ... etc. Y lo mismo para B)
def restricciones(A, a, B, b):
    if B in vecinos[A]:
        if a == b:
            return False
    if A in vecinos[B]:
        if a == b:
            return False
    return True

problema_colores = CSP(variables, dominios, vecinos, restricciones)

print backtracking_search(problema_colores)
