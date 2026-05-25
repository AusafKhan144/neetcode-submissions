class Solution:
	def evalRPN(self, tokens: list[str]) -> int:
		evaluation = 0
		operators = ['+','-','*','/']
		stack = list()
		for num, token in enumerate(tokens):
			if token in operators:
				b = stack.pop()
				a = stack.pop()
				if token == '-':
					stack.append(a - b)
				elif token == '+':
					stack.append(a + b)
				elif token == '*':
					stack.append(a * b)
				elif token == '/':
					stack.append(int(a / b))
			else:
				stack.append(int(token))

		return stack.pop()