from socialAD.forward_pro import *

x = forwardAD_pro(3.0)

f = 3*x**2 + x**3

print(f.func.val, f.dera.val, f.dera.der)

x = forwardAD_pro(3.0)

f = x**e()*x**2

print(f.func.val, f.dera.val, f.dera.der)

x = forwardAD_pro(3.0)

f = log(x)**2

print(f.func.val, f.dera.val, f.dera.der)

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


