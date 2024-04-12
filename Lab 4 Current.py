import math

from manim import *
import numpy as np
from scipy.optimize import fsolve


def func(x):
    return [x[0] - x[1] - x[2],
            2 - 51 * x[0] - 51 * x[1],
            51 * x[1] - 68 * x[2] - 68 * x[2]]


root = fsolve(func, [1, 1, 1])

print("I total: ", root[0])
print("I 2: ", root[1])
print("I 3: ", root[2])
