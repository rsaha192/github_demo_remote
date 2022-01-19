#Add
def add(x,y):
	return x+y
#Subtract
def subtrac(x,y):
	return x-y
#Multiply
def multiply(x,y):
	return x*y
#Divide
def divide(x,y):
	if y==0:
        return DIVIDE_BY_0_ERROR
    else:
        return x/y
#NewFunction
def square (x):
    return x*x