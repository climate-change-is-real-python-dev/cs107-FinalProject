from socialAD.forwardAD import *


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

cc = arccos(0.5)
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
