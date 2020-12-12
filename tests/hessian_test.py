from forward_pro import *
# from forward import *


# x = forwardAD_pro(3.0)

# f = 3*x**2 + x**3

# print(f.func.val, f.dera.val, f.dera.der)


# x = forwardAD_pro(3.0)

# f = x**e()*x**2

# print(f.func.val, f.dera.val, f.dera.der)


# x = forwardAD_pro(3.0)

# f = log(x)**2

# print(f.func.val, f.dera.val, f.dera.der)

# x = forwardAD(3.0)

# f = log(x)**2

# print(f.val, f.val, f.der)


x = forwardAD_pro(0.387)

f = log(1/(tan(x)*x**2))

print(f.func.val, f.dera, f.dera.der)

x = forwardAD_pro(0.387)

f = log(1/(arcsin(x)*x**2))

print(f.func.val, f.dera.val, f.dera.der)

x = forwardAD_pro(0.387)

f = log(1/(arccos(x)*x**2))

print(f.func.val, f.dera.val, f.dera.der)

x = forwardAD_pro(0.387)

f = log(1/(arctan(x)*x**2))

print(f.func.val, f.dera.val, f.dera.der)

x = forwardAD_pro(0.387)

f = log(1/(sinh(x)*x**2))

print(f.func.val, f.dera.val, f.dera.der)

x = forwardAD_pro(0.387)

f = log(1/(cosh(x)*x**2))

print(f.func.val, f.dera.val, f.dera.der)

x = forwardAD_pro(0.387)

f = log(1/(tanh(x)*x**2))

print(f.func.val, f.dera.val, f.dera.der)


'''
Adding function tests
# '''

# a = np.array([3]) # Value of x to be evaluated 
# x = forwardAD_pro(a, numvar = 2, idx = 0)

# b = np.array([2]) # Value of y to be evaluated 
# y = forwardAD_pro(b, numvar = 2, idx = 1)

# b = np.array([2]) # Value of z to be evaluated 
# y = forwardAD_pro(b, numvar = 2, idx = 1)


# f1 = x*y
# f2 = x**2.0 + y**2.0


# a = vector_func(f1, f2)
# print(a.values())
# print(a.jacobian())
# print(a.hessian())


# print("\n")
# print("Tests for comparison operators")




