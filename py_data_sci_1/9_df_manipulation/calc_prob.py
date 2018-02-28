import numpy as np
import math

xv = -10.6513 + .0055*1936.6

def calc_log(x):
    return math.exp(x) / (1 + math.exp(x))

print(calc_log(xv))