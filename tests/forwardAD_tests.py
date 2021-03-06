from socialAD.forward import *


###For Documentation###
#Always show multiplication explicitly with a '*'. You cannot just put a number next to x
#Use e() for the natural number (Euler's number): e
#For log, use class log(). Defaults to natural log. See implementation above.

##Tests
a = 3.00 # Value to evaluate at
x = forwardAD(a)
alpha = 2.00
beta = 5.00


print('Should be: 0.401265 0.820037')
cc = (4*e())**(sin(7 - log(5 + 3** x)))
print(cc.val, cc.der)
print('\n')\


print('Should be: 0.110286 -0.0933502')
cc = (4*e())**(cos(7 - log(5 + 3** x)))
print(cc.val, cc.der)
print('\n')\


print('Should be: 2.68682 -6.96274')
cc = (4*e())**(tan(7 - log(5 + 3** x)))
print(cc.val, cc.der)
print('\n')\


print('Should be: 5.52971e17 -2.09766e19')
cc = (4*e())**(sinh(7 - log(5 + 3** x)))
print(cc.val, cc.der)
print('\n')\

print('Should be: 5.92848e17 -2.24511e19')
cc = (4*e())**(cosh(7 - log(5 + 3** x)))
print(cc.val, cc.der)
print('\n')\

print('Should be: 1.4097 -0.348387')
cc = (4*e())**(x**(-2)*arctan(7 - log(5 + 3** x)))
print(cc.val, cc.der)
print('\n')\


'''
Adding more tests
'''

cc = x + (2 + 7*x)
print(cc.val, cc.der)
print('\n')\

cc = x - (2 - 6*x - 2*x)
print(cc.val, cc.der)
print('\n')\

cc = x - (2 - 6*x -3*x)
print(cc.val, cc.der)
print('\n')\



cc = sin( sin(10) + sin(x))
print(cc.val, cc.der)
print('\n')\

cc = arctan( arctan(0.5) + arctan(x))
print(cc.val, cc.der)
print('\n')\



cc = tanh(0.5)
print(cc.val, cc.der)
print('\n')\


cc = tanh(x) + 2
print(cc.val, cc.der)
print('\n')\


cc = x.__rsub__(tanh(0.5))
print(cc.val, cc.der)
print('\n')\


cc = x.__rtruediv__(tanh(0.5))
print(cc.val, cc.der)
print('\n')\

cc = x.__truediv__(tanh(0.5))
print(cc.val, cc.der)
print('\n')\

cc = x.__rtruediv__(tanh(x))
print(cc.val, cc.der)
print('\n')\

cc = x.__truediv__(0.5)
print(cc.val, cc.der)
print('\n')\

cc = x.__rtruediv__(0.5)
print(cc.val, cc.der)
print('\n')\

cc = x.__truediv__(tanh(x))
print(cc.val, cc.der)
print('\n')\



cc = x.__rpow__(tanh(0.5)) 
print(cc.val, cc.der)
print('\n')\


cc = x*log(5.0)
print(cc.val, cc.der)
print('\n')\

cc = x*cos(5.0)
print(cc.val, cc.der)
print('\n')\

cc = x*tan(5.0)
print(cc.val, cc.der)
print('\n')\

cc = x*sinh(0.5)
print(cc.val, cc.der)
print('\n')\

cc = x*cosh(0.5) - 3
print(cc.val, cc.der)
print('\n')\



cc = x*arccos(0.5) - 3*arccos(0.2)
print(cc.val, cc.der)
print('\n')\


cc = x*arcsin(0.5) - 3*arcsin(0.2)
print(cc.val, cc.der)
print('\n')\

cc = sigmoid(0.5) - 3*sigmoid(x)
print(cc.val, cc.der)
print('\n')\


'''
Adding function tests
'''
a = np.array([3]) # Value of x to be evaluated 
x = forwardAD(a, numvar = 2, idx = 0)

b = np.array([2]) # Value of y to be evaluated 
y = forwardAD(b, numvar = 2, idx = 1)

f1 = x*y
f2 = x**2 + y**2

print(f1.val) 
print(f2.val) 

print('---------')

print(f1.der) 
print(f2.der) 


a = vector_func(f1, f2)
jacobian_a = a.jacobian
print(jacobian_a)
values_a = a.values
print(values_a)

print("\n")
print("Tests for comparison operators")

'''
Comparison operators
'''

# Scalar inputs
ob1 = forwardAD(4)
ob2 = forwardAD(7)
f1 = 4*ob1 + 3*ob2
f2 = 3*ob1 + 4*ob2
print("value of f1:", f1.val)
print("value of f2:", f2.val)
print("der of f1:", f1.der)
print("der of f2:", f2.der)

# True only if both val and der are true
print("eq: ", f1 == f2) # expected: val false, der true, therefore false
print("neq: ", f1 != f2) # expected: val true, der false, therefore false
print("less than: ", f1 < f2) # expected: val true, der false, therefore false
print("leq: ", f1 <= f2) # expected: val true, der true, therefore true
print("greater than: ", f1 > f2) # expected: val false, der false, therefore false
print("geq: ", f1 >= f2) # expected: val false, der true, therefore false

# Reverse
print("eq: ", f2 == f1) # expected: val false, der true, therefore false
print("neq: ", f2 != f1) # expected: val true, der false, therefore false
print("less than: ", f2 < f1) # expected: val false, der false, therefore false
print("leq: ", f2 <= f1) # expected: val false, der true, therefore false
print("greater than: ", f2 > f1) # expected: val false, der false, therefore false
print("geq: ", f2 >= f1) # expected: val true, der true, therefore true

# Compare with a single number
print("eq: ", f1 == 1) # expected: false
print("neq: ", f1 != 1) # expected: true
print("less than: ", f1 < 1) # expected: false
print("leq: ", f1 <= 1) # expected: false
print("greater than: ", f1 > 1) # expected: true
print("geq: ", f1 >= 1) # expected: true

# Reverse
print("eq: ", 1 == f1) # expected: false
print("neq: ", 1 != f1) # expected: true
print("less than: ", 1 < f1) # expected: true
print("leq: ", 1 <= f1) # expected: true
print("greater than: ", f1 > f1) # expected: false
print("geq: ", 1 >= f1) # expected: false

# Vector inputs
a = np.array([3])
x = forwardAD(a, numvar=2, idx=0)

b = np.array([2])
y = forwardAD(b, numvar=2, idx=1)

f1 = x*y
f2 = x**2 + y**2

# True only if both val and der are true
print("eq: ", f1 == f2) # expected: val false, der false, therefore false
print("neq: ", f1 != f2) # expected: val true, der [true true], therefore true
print("less than: ", f1 < f2) # expected: val true, der [true true], therefore [true true]
print("leq: ", f1 <= f2) # expected: val true, der [true true], therefore [true true]
print("greater than: ", f1 > f2) # expected: val false, der [false false], therefore false
print("geq: ", f1 >= f2) # expected: val false, der [false false], therefore false

# Reverse
print("eq: ", f2 == f1) # expected: val false, der false, therefore false
print("neq: ", f2 != f1) # expected: val true, der [true true], therefore true
print("less than: ", f2 < f1) # expected: val false, der [false false], therefore false
print("leq: ", f2 <= f1) # expected: val false, der [false false], therefore false
print("greater than: ", f2 > f1) # expected: val true, der [true true], therefore [true true]
print("geq: ", f2 >= f1) # expected: val true, der [true true], therefore [true 

# Compare with a single number
print("eq: ", f1 == 1) # expected: false
print("neq: ", f1 != 1) # expected: true
print("less than: ", f1 < 1) # expected: false
print("leq: ", f1 <= 1) # expected: false
print("greater than: ", f1 > 1) # expected: true
print("geq: ", f1 >= 1) # expected: true

# Reverse
print("eq: ", 1 == f1) # expected: false
print("neq: ", 1 != f1) # expected: true
print("less than: ", 1 < f1) # expected: true
print("leq: ", 1 <= f1) # expected: true
print("greater than: ", f1 > f1) # expected: false
print("geq: ", 1 >= f1) # expected: false

'''
print('Should be: -4.3333 -0.222222')
fa = alpha / x - beta
print(fa.val, fa.der)
print('\n')

print('Should be: -3.5 0.5')
fb = x / alpha - beta
print(fb.val, fb.der)
print('\n')

print('Should be: -1.0 -2.0')
fc = beta - alpha * x
print(fc.val, fc.der)
print('\n')

print('Should be: 11.0 2.0')
fd = beta + x * alpha
print(fd.val, fd.der)
print('\n')

print('Should be: 6.6666 -6.88888')
fe = fd - fc * fa
print(fe.val,fe.der)
print('\n')

print('Should be: -0.39393939 0.0514')
ff = fa/fd
print(ff.val,ff.der)
print('\n')

print('Should be: 243.0 405.0')
aa = x ** beta
print(aa.val, aa.der)
print('\n')

print('Should be: 14348907.0 150563962.795')
ac = x**(5.0 * x)
print(ac.val, ac.der)
print('\n')

print('Should be: 18.5202 21.988')
ad = (x+4.0)**(x/2.0)
print(ad.val, ad.der)
print('\n')

print('Should be: 0.125 0.08664')
ae = (4.0)**(x/2.0 - 3)
print(ae.val, ae.der)
print('\n')

print('Should be: 0.002984 -0.00374')
ab = (5 * x ** x / (7 + x /8 ))** (x - 5.0 * x / x)
print(ab.val, ab.der)
print('\n')

print('Should be: 1.967989 0.163999')
af = (5 * x) ** (1/4)
print(af.val, af.der)
print('\n')

print('Should be: 1.68987 0.14082')
ag = (e() * x) ** (1/4)
print(ag.val, ag.der)
print('\n')

print('Should be: 20.0855 20.08555')
ba = e() ** x
print(ba.val, ba.der)
print('\n')

print('Should be: -0.100809 0.0132')
bb = (e() ** x) ** (1/4) / (3 - 8 * x )
print(bb.val, bb.der)
print('\n')

print('Should be: 0.1411 -0.9899')
triga = sin(x)
print(triga.val,triga.der)
print('\n')

print('Should be: -0.536 0')
trigb = sin(12)
print(trigb.val,trigb.der)
print('\n')

print('Should be: 2.243 1.8715')
trigc = x + sin(12/x)
print(trigc.val,trigc.der)
print('\n')

print('Should be: 2.07944 0.125')
ca = log(5 + x)
print(ca.val, ca.der)
print('\n')

print('Should be: 3.295 1.0986')
foo = log(3 ** x)
print(foo.val, foo.der)
print('\n')

print('Should be: 3.67 0.6051')
cb = 8 * x / 4**x + log(x ** 3)
print(cb.val, cb.der)
print('\n')

print('Should be: -1.683 -1.0')
cb = log(5 / x ** 3)
print(cb.val, cb.der)
print('\n')
'''
