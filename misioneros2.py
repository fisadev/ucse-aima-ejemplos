from search import Problem, breadth_first_tree_search, depth_first_tree_search, uniform_cost

ACTIONS = [(m, c)
           for m in (0, 1, 2)
           for c in (0, 1, 2)
           if 0 < m + c < 3]


class ProblemaMisioneros(Problem):
    def actions(self, state):
        return [a for a in ACTIONS if self.is_valid(self.result(state, a))]

    def is_valid(self, state):
        otro_lado = tuple([3 - x for x in state[:2]])
        este_lado = state[:2]
        no_se_comen = [not (lado[0] > 0 and lado[1] > lado[0])
                       for lado in (este_lado, otro_lado)]

        cantidades_bien = [0 <= valor <= 3 for valor in state[:2]]

        return all(no_se_comen + cantidades_bien)

    def result(self, state, action):
        if state[2] == 'I':
            resultado = (state[0] - action[0], state[1] - action[1], 'D')
        else:
            resultado = (state[0] + action[0], state[1] + action[1], 'I')
        return resultado

    def goal_test(self, state):
        return state[:2] == (0, 0)

if __name__ == '__main__':
    p1 = ProblemaMisioneros((3, 3, 'I'))

    # r = breadth_first_tree_search(p1)
    # r = depth_first_tree_search(p1)
    r = uniform_cost(p1)

    while r:
        print 'Estado', r.state
        print 'Accion', r.action

        r = r.parent

