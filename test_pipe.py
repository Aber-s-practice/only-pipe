import pipe
import functools

pipe.set_global(pipe.F, pipe.FF, functools.reduce)

assert range(10) | F(filter, lambda x: x % 2) | F(sum) == 25
assert (1, 2, 3) | F(sum) == 6

assert (1, 2) | FF(lambda x, y: x + y) == 3

assert range(10) | F(reduce, lambda x, y: x + y) == 45
