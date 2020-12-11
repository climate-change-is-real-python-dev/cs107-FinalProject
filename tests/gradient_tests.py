import socialAD.gradient as gd
import numpy as np
import time

def generate_timer(function):
    def with_timer():
        t_start = time.monotonic()
        function
        t_stop = time.monotonic()
        print( f'Time elapsed: {t_stop - t_start} seconds ')  
        print('--------------------------------------------')
    return with_timer
variables = ["x"]
f = "(x+5)**2 "
cur_x = [3]
rate = 0.01
precision = 0.000001
previous_step_size = 1
max_iters = 10000
iters = 0

print('============================================')
print('GRADIENT DESCENT')
print('============================================')

a = generate_timer(gd.gradient_descent(variables, f, cur_x, rate, precision, previous_step_size, max_iters))
a()

print('============================================')
print('GD WITH BACKTRACK LINE SEARCH')
print('============================================')

a = generate_timer(gd.gd_backtrack(variables, f, cur_x, precision, previous_step_size, max_iters))
a()

print('============================================')
print('BFGS')
print('============================================')
a  = generate_timer(gd.BFGS(variables, f, cur_x, precision, max_iters))
a()
print('============================================')
print('BFGS WITH BACKTRACK LINE SEARCH')
print('============================================')
a = generate_timer(gd.BFGS_backtrack(variables, f, cur_x, precision, max_iters))
a()



variables = ["x","y"]
f = "(x+5)**2 + y**2"
cur_x = [3, 1]

print('============================================')
print('GRADIENT DESCENT')
print('============================================')

a = generate_timer(gd.gradient_descent(variables, f, cur_x, rate, precision, previous_step_size, max_iters))
a()

print('============================================')
print('GD WITH BACKTRACK LINE SEARCH')
print('============================================')

a = generate_timer(gd.gd_backtrack(variables, f, cur_x, precision, previous_step_size, max_iters))
a()

print('============================================')
print('BFGS')
print('============================================')
a  = generate_timer(gd.BFGS(variables, f, cur_x, precision, max_iters))
a()
print('============================================')
print('BFGS WITH BACKTRACK LINE SEARCH')
print('============================================')
a = generate_timer(gd.BFGS_backtrack(variables, f, cur_x, precision, max_iters))
a()
