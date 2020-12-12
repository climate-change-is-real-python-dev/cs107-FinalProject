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

f = log(1/(sin(x)*x**2))

print(f.func.val, f.dera, f.dera.der)


x = forwardAD_pro(0.387)

f = log(1/(cos(x)*x**2))

print(f.func.val, f.dera, f.dera.der)


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


cc = x.__rtruediv__(tanh(0.5))

cc = x.__truediv__(tanh(0.5))

cc = x.__rtruediv__(tanh(x))

cc = x.__truediv__(0.5)

cc = x.__rtruediv__(0.5)

cc = x.__truediv__(tanh(x))

cc = x.__rpow__(tanh(0.5)) 

cc = x*log(5.0)

cc = x*cos(5.0)

cc = x*tan(5.0)

cc = x*sinh(0.5)

cc = x*cosh(0.5) - 3

cc = x*arccos(0.5) - 3*arccos(0.2)

cc = x*arcsin(0.5) - 3*arcsin(0.2)

