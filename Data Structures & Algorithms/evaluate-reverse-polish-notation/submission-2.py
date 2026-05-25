class Solution:
	def evalRPN(self, tokens: list[str]) -> int:
		evaluation = 0
		operators = ['+','-','*','/']
		stack = list()
		for num, token in enumerate(tokens):
			if token in operators:
				opp2 = stack.pop()
				opp1 = stack.pop()
				if token == '-':
					stack.append(opp1 - opp2)
				elif token == '+':
					stack.append(opp1 + opp2)
				elif token == '*':
					stack.append(opp1 * opp2)
				elif token == '/':
					stack.append(int(opp1 / opp2))
			else:
				stack.append(int(token))

		return stack.pop()