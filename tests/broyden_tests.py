from socialAD.forward import *
from socialAD.broyden import *
import numpy as np 

### Tests of broyden ###

print('Case: non-vector function, multiple variables')
print('Should get roots of 2.53 and -14.29')
print(broyden("y + x**3 + 3*x**2 - 21",["x","y"],[3, 7]))
print('\n')

print('Case: vector function, single variable')
print('Should get root of 5')
functions = ["x**2 - 25", "x - 5"]
print(broyden(functions,"x",[50]))
print('\n')

print('Case: vector function, multple variables')
print('Should get roots of 1 and 1')
functions = ["x + y - 2", "x - y"]
print(broyden(functions,["x","y"],[4,4]))
print('\n')

# #Error test
# print('Should get convergence error')
# functions = ["y + x**2 - 25", "2*y + x - 5"]
# print(broyden(functions,["x","y"],[0,0]))