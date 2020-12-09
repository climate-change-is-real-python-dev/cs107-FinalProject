from forward import *
import numpy as np


### Implementation of Broyden's Optimization Method ###
# More computationally efficient than Newton's method #

#Broyden function
def broyden(function, variables, init_values):

	#Check user input types (string or list of strings)
	if not isinstance(function,str):

		#Vector function case
		if not isinstance(function,list):
			raise TypeError('function input must be either string or list of strings')

		if not isinstance(function[0],str):
			raise TypeError('function input must be either string or list of strings')

	#Check user input types (string or list of strings)
	if not isinstance(variables,str):

		#Vector function case
		if not isinstance(variables,list):
			raise TypeError('Each input must be either string or list of strings')

		if not isinstance(variables[0],str):
			raise TypeError('Each input must be either string or list of strings')

	#Check inital values is a list
	if not isinstance(init_values,list):
		
		raise TypeError('initial values must be a list')

	#Check that initial values and variables match in length
	if not len(variables) == len(init_values):

		raise Error('number of initial values must match number of variables')

	#Broyden's method for non-vector function
	if isinstance(function,str):

		#If just one string, convert to list
		if isinstance(variables,str):

			variables = [variables]

		#Convert to numpy arrays
		variables = np.array(varibles)
		init_values = np.array(init_values)

		#Loop through variable names
		for index, variable in enumerate(variables):

			#Store to variable name
			name = variable

			#Save as forwardAD object
			exec(name + " = forwardAD(np.array([init_values[index]]), numvar = len(variables), idx = index)")

		#Stores full function as a forwardAD object
		AD_function = eval(function)

		#First iteration is Newton's method
		new_values = init_values - (AD_function.val / AD_function.der)

		#Store init as last values
		previous_values = init_values

		#Stores function value as previoust function value
		previous_function_val = AD_function.val

		#Iterate using finite differences until find good enough root
		while max(AD_function.val) > 1e-20:

			#Loop through variable names
			for index, variable in enumerate(variables):

				#Store to variable name
				name = variable

				#Save as forwardAD object
				exec(name + " = forwardAD(np.array([new_values[index]]), numvar = len(variables), idx = index)")

			#Stores full function as a forwardAD object
			AD_function = eval(function)

			print('new run')
			print('new values: ', new_values)
			print('previous values: ', previous_values)

			#Evaluate finite difference
			finite_difference = (AD_function.val - previous_function_val) / (new_values - previous_values)

			#Next estiamte
			new_values = previous_values - (AD_function.val / finite_difference)

			#Store function value
			previous_function_val = AD_function.val

			#Store domain values
			previous_values = new_values

		return new_values, AD_function.val






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
jacobian_a = a.jacobian()
print(jacobian_a)
# values_a = a.values()
# print(values_a)

print(np.transpose(jacobian_a))

print(type(f1))

print(type(a))

print(type("hellow wjklfd fdasl;"))

exec('j = 27')

print(j)

print(type([2]))


example = "hello"
example = [example]
print(example)
print(type(example))

##Tests
a = 3.00 # Value to evaluate at
x = forwardAD(a)

print('Should be: 0.401265 0.820037')
cc = (4*e())**(sin(7 - log(5 + 3** x)))
print(type(cc.val), cc.der)








broyden("(4*e())**(sin(7 - log(5 + 3** x)))","x",[3])