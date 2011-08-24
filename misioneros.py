# importamos las cosas que vamos a usar de aima
from search import Problem, breadth_first_tree_search

class ProblemaMisioneros(Problem):
    ''' Clase problema (formalizacion de nuestro problema) siguiendo la
        estructura que aima espera que tengan los problemas.'''
    def __init__(self, initial, goal=None):
        '''Inicializacion de nuestro problema.'''
        Problem.__init__(self, initial, goal)
        # cada accion tiene un texto "lindo", y despues una tupla con la
        # cantidad de misioneros y canibales que se mueven en la canoa
        self._actions = [('1c', (0,1)), ('1m', (1, 0)), ('2c', (0, 2)), ('2m', (2, 0)), ('1m1c', (1, 1))]

    def actions(self, s):
        '''Devuelve las acciones validas para un estado.'''
        # las acciones validas para un estado son aquellas que al aplicarse
        # nos dejan en otro estado valido
        return [a for a in self._actions if self._is_valid(self.result(s, a))]

    def _is_valid(self, s):
        '''Determina si un estado es valido o no.'''
        # un estado es valido si no hay mas canibales que misioneros en ninguna
        # orilla, y si las cantidades estan entre 0 y 3
        return (s[0] >= s[1] or s[0] == 0) and ((3 - s[0]) >= (3 - s[1]) or s[0] == 3) and (0 <= s[0] <= 3) and (0 <= s[1] <= 3)

    def result(self, s, a):
        '''Devuelve el estado resultante de aplicar una accion a un estado
           determinado.'''
        # el estado resultante tiene la canoa en el lado opuesto, y con las
        # cantidades de misioneros y canibales actualizadas segun la cantidad
        # que viajaron en la canoa
        if s[2] == 0:
            return (s[0] - a[1][0], s[1] - a[1][1], 1)
        else:
            return (s[0] + a[1][0], s[1] + a[1][1], 0)

# creamos un problema a partir de nuestra formalizacion de ProblemaMisioneros
# como parametros le pasamos el estado inicial, y el estado meta que esperamos
p1 = ProblemaMisioneros((3, 3, 0), (0, 0, 1))

# le decimos a aima que resuelva nuestro problema con el metodo de busqueda en
# amplitud
r = breadth_first_tree_search(p1)
# esto nos devuelve el nodo meta del arbol. Podemos recorrer sus padres para
# tener todo el camino de acciones
camino_acciones = []
while r:
    if r.action:
        camino_acciones.append(r.action[0])
    r = r.parent

print ' '.join(reversed(camino_acciones))
