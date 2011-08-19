from search import Problem

class ProblemaMisioneros(Problem):
    def __init__(self, initial, goal=None):
        Problem.__init__(self, initial, goal)
        self._actions = [('1c', (0,1)), ('1m', (1, 0)), ('2c', (0, 2)), ('2m', (2, 0)), ('1m1c', (1, 1))]


