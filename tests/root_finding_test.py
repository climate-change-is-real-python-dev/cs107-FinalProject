from root_finding import *



'''
Adding function tests
'''
# a = np.array([3]) # Value of x to be evaluated 
# x = forwardAD(a, numvar = 2, idx = 0)

# b = np.array([2]) # Value of y to be evaluated 
# y = forwardAD(b, numvar = 2, idx = 1)

# f1 = x*y
# f2 = x**2 + y**2

# print(f1.val) 
# print(f2.val) 

# print('---------')

# print(f1.der) 
# print(f2.der) 


# a = vector_func(f1, f2)
# jacobian_a = a.jacobian()
# print(jacobian_a)
# values_a = a.values()


##Tests
# a = 3.00 # Value to evaluate at
# x = forwardAD(a)

# print('Should be: 0.401265 0.820037')
# cc = (4*e())**(sin(7 - log(5 + 3** x)))
# print(type(cc.val), cc.der)








# print(broyden("y + x**3 + 3*x**2 - 21",["x","y"],[3, 7])[0][1])

# functions = ["x**3 + 3*x**2 - 21", "x + 25"]

# print(broyden(functions,"x",[5]))


functions = ["x**2 - 25", "x - 5"]

print("Broyden's Method: ")
print(broyden(functions,"x",[50]))

print("Newton's Method: ")
print(newton(functions,"x",[50]))

# functions = ["y + x**2 - 25", "2*y + x - 5"]

# print(broyden(functions,["x","y"],[0,0]))


functions = ["x**3 + y**3 - 2", "x**3 - y**3"]

print("Broyden's Method: ")
print(broyden(functions,["x","y"],[4,4]))
print("Newton's Method: ")
print(newton(functions,["x","y"],[4,4]))

