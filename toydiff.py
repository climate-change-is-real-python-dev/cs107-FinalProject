import numpy as np

#Forward mode, automatic differentiation class
class AutoDiffToy:
	def __init__(self, val, der=1.0):
		self.val = val
		self.der = der

	#Overloaded addition
	def __add__(self, other):

		#For adding of the same class, add derivatives
		try:
			out_val = self.val + other.val
			out_der = self.der + other.der

		#For adding a float, keep derivative
		except AttributeError:
			out_val = self.val + other
			out_der = self.der

		return AutoDiffToy(out_val, out_der)

	#Overloaded subtraction
	def __sub__(self, other):

		#For subtracting of the same class, subtract derivatives
		try:
			out_val = self.val - other.val
			out_der = self.der - other.der

		#For subtracting a float, keep derivative
		except AttributeError:
			out_val = self.val - other
			out_der = self.der

		return AutoDiffToy(out_val, out_der)

	#Overloaded multiplication
	def __mul__(self, other):

		#For multiplying the same class, use product rule
		try:
			out_val = self.val * other.val
			out_der = self.der * other.val + self.val * other.der

		#For multiplying a float, multiply the value
		except AttributeError:
			out_val = self.val * other
			out_der = self.der * other

		return AutoDiffToy(out_val, out_der)


	#Overloaded division
	def __truediv__(self, other):

		#For dividing the same class, use quotient rule
		try:
			out_val = self.val / other.val
			out_der = (self.der * other.val - self.val * other.der)/(other.val ** 2.0)

		#For dividing a float, divide the value
		except AttributeError:
			out_val = self.val / other
			out_der = self.der / other

		return AutoDiffToy(out_val, out_der)

	#Overloaded power
	def __pow__(self, other):

		#For power to same class, use logarithmic differentiation
		try:
			out_val = self.val ** other.val
			out_der = (other.der * np.log(self.val) + other.val * (self.der / self.val)) * (self.val ** other.val)

		#For raising to a float, do power rule
		except AttributeError:
			out_val = self.val ** other
			out_der = self.der * other * self.val **(other - 1.0)

		return AutoDiffToy(out_val, out_der)

	### Reversed Operations ###

	# Addition is commutative
	def __radd__(self, other):
		return self.__add__(other)

	# Reverse subtraction
	def __rsub__(self, other):

		#If another of same type, then reverse order of subtraction
		try:
			out_val = other.val - self.val
			out_der = other.der - self.der

		#If a float, then reverse order subtract
		except AttributeError:
			out_val = other - self.val
			out_der = -1.0 * self.der

		return AutoDiffToy(out_val, out_der)

	#Multiplication is commutative
	def __rmul__(self, other):
		return self.__mul__(other)

	#Reverse division
	def __rtruediv__(self, other):
		#For dividing the same class, use reversed quotient rule
		try:
			out_val = other.val / self.val
			out_der = (other.der * self.val - other.val * self.der)/(self.val ** 2.0)

		#For dividing a float, take derivative of f**(-1) using power rule
		except AttributeError:
			out_val = other / self.val
			out_der = (-1.0) * other * self.der / (self.val**2.0)
		
		return AutoDiffToy(out_val, out_der)

	#Reverse power
	def __rpow__(self, other):

		#If base is same class, do logarithmic differentiation
		try:
			out_val = other.val ** self.val
			out_der = (self.der * np.log(other.val) + self.val * (other.der / other.val)) * (other.val ** self.val)

		#If base is a float, then b^x derivative rule
		except AttributeError:
			out_val = other ** self.val
			out_der = other ** self.val * self.der * np.log(other)

		return AutoDiffToy(out_val, out_der)

#For getting an 'e'
class e(AutoDiffToy):
	def __init__(self, val=np.exp(1), der=0.0):
		self.val = val
		self.der = der

#For getting a log, defaults to natural log
class log(AutoDiffToy):
	def __init__(self, inputs, base = np.exp(1)):

		#For getting log of variable expression, log is derivative/val
		try:
			self.val = np.log(inputs.val)/np.log(base)
			self.der = inputs.der / inputs.val

		#For log of float, use numpy.log
		except AttributeError:
			self.val = np.log(inputs) / np.log(base)
			self.der = 0.0

#For getting a sine
class sin(AutoDiffToy):
	def __init__(self, inputs):

		#For getting log of variable expression, log is derivative/val
		try:
			self.val = np.sin(inputs.val)
			self.der = inputs.der * np.cos(inputs.val)

		#For sine of float, use numpy.sin
		except AttributeError:
			self.val = np.sin(inputs)
			self.der = 0.0


###For Documentation###
#Always show multiplication explicitly with a '*'. You cannot just put a number next to x
#Use e() for the natural number (Euler's number): e
#For log, use class log(). Defaults to natural log. See implementation above.

##Tests
a = 3.00 # Value to evaluate at
x = AutoDiffToy(a)
alpha = 2.00
beta = 5.00


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

print('Should be: 4599.92 -10174.9588')
cc = (4*e())**(7 - log(5 + 3** x))
print(cc.val, cc.der)
print('\n')