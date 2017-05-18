class DivideError(Exception): pass

def divideFunction( dividend, divisor):
	if divisor == 0:
		errorMessage = "Divisor = " + str(divisor) + " which cannot be zero"
		raise DivideError, errorMessage
	answer = float(dividend) / float(divisor)
	print "The answer = ", answer
	return answer
