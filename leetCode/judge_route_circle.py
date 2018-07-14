import functools
import operator

def judgeCircle(self, moves):
    directions = {'U': (1, 0),
                  'R': (0, 1),
                  'D': (-1, 0),
                  'L': (0, -1)}

    return (0, 0) == functools.reduce(
        lambda accumlator, move: tuple(map(operator.add, directions[move], accumlator)), moves, (0, 0))
