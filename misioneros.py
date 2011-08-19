from search import Problem

class ProblemaMisioneros(Problem):
    def __init__(self, initial, goal=None):
        Problem.__init__(self, initial, goal)
        self._actions = [('1c', (0,1)), ('1m', (1, 0)), ('2c', (0, 2)), ('2m', (2, 0)), ('1m1c', (1, 1))]

    def actions(self, s):
        return [a for a in self._actions if self._is_valid(self._result(s, a))]

    def is_valid(self, s):
        return s[0] >= s[1] and (3 - s[0]) >= (3 - s[1]) and (0 <= s[0] <= 3) and (0 <= s[1] <= 3)

    def result(self, s, a):
        if s[2] == 0:
            return (s[0] - a[0][1], s[1] - a[1][1], 1)
        else:
            return (s[0] + a[0][1], s[1] + a[1][1], 0)

