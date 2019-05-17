def evalRPN(tokens):
	"""
	:type tokens: List[str]
	:rtype: int
	"""
	import math
	driverStack = []

	for token in tokens:
		if token not in ['+', '-', '/', '*']:
			driverStack.append(token)
		else:
			first = driverStack.pop()
			second = driverStack.pop()

			if token == '+':
				driverStack.append(int(float(first) + float(second)))
			elif token == '-':
				driverStack.append(int(float(first) - float(second)))
			elif token == '*':
				driverStack.append(int(float(first) * float(second)))
			elif token == '/':
				driverStack.append(math.trunc(float(first) / float(second)))



	print(driverStack)
			






tokens = ["4", "13", "5", "/", "+"]
print(evalRPN(tokens))

import math

print(math.trunc(-0.5))