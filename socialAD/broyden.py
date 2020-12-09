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
		variables = np.array(variables)
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
		while abs(AD_function.val) > 1e-7:

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
			print('function value:', AD_function.val)

			#Evaluate finite difference
			finite_difference = (AD_function.val - previous_function_val) / (new_values - previous_values)

			#Store function value
			previous_function_val = AD_function.val

			#Store domain values
			previous_values = new_values

			#Next estiamte
			new_values = previous_values - (AD_function.val / finite_difference)

		return new_values, AD_function.val

	#Case of vector function
	else:

		#List to store functions
		vector = []

		#If just one string, convert to list
		if isinstance(variables,str):

			variables = [variables]

		#Convert to numpy arrays
		variables = np.array(variables)
		init_values = np.array(init_values)

		#Loop through functions
		for func in function:

			#Loop through variable names
			for index, variable in enumerate(variables):

				#Store to variable name
				name = variable

				#Save as forwardAD object
				exec(name + " = forwardAD(np.array([init_values[index]]), numvar = len(variables), idx = index)")

			#Stores full function in vector of functions as forwardAD object
			vector.append(eval(func))

		#Store as a vector function
		AD_vector = vector_func(*vector)

		#Store values
		previous_values = init_values
		previous_values = previous_values.reshape(len(previous_values),1)

		#Store jacobian
		previous_jacobian = AD_vector.jacobian()

		#Store function values
		previous_function_val = AD_vector.values()

		new_values = previous_values - np.matmul(np.linalg.pinv(AD_vector.jacobian()),AD_vector.values())
		new_values = new_values.reshape(1,-1)[0]

		#Loop counter
		loop = 0

		#Iterate using finite differences until find good enough root
		while np.linalg.norm(AD_vector.values()) > 1e-7:

			#List to store functions
			vector = []

			#Loop through functions
			for func in function:

				#Loop through variable names
				for index, variable in enumerate(variables):

					#Store to variable name
					name = variable

					#Save as forwardAD object
					exec(name + " = forwardAD(np.array([new_values[index]]), numvar = len(variables), idx = index)")

				#Stores full function in vector of functions as forwardAD object
				vector.append(eval(func))

			#Store as a vector function
			AD_vector = vector_func(*vector)

			#differences
			previous_values = previous_values.reshape(1,-1)[0]
			delta_f = AD_vector.values() - previous_function_val
			delta_x = new_values - previous_values
			# print(previous_values)
			delta_x = delta_x.reshape(len(delta_x),1)

			#Evaluate finite jacobian
			finite_jacobian = previous_jacobian + np.matmul((delta_f - np.matmul(previous_jacobian, delta_x)) / np.linalg.norm(delta_x),delta_x.T)

			#Store function value
			previous_function_val = AD_vector.values()

			#Store domain values
			previous_values = new_values
			previous_values = previous_values.reshape(len(previous_values),1)
			# print(previous_values)

			#Next estiamte
			new_values = previous_values - np.matmul(np.linalg.pinv(finite_jacobian),AD_vector.values())
			new_values = new_values.reshape(1,-1)[0]
			# print(new_values)

			# print(np.linalg.norm(AD_vector.values()))
			# print(AD_vector.values())
			# print(new_values)

			if loop > 10000:

				raise ValueError('Too many iterations - could not converge')

			loop += 1

		return new_values, AD_vector.values()


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

print(broyden(functions,"x",[50]))

# functions = ["y + x**2 - 25", "2*y + x - 5"]

# print(broyden(functions,["x","y"],[0,0]))


functions = ["x**3 + y**3 - 2", "x**3 - y**3"]

print(broyden(functions,["x","y"],[4,4]))