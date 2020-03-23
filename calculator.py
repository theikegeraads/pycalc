import math
n1 = float(input('Number 1: '))
operator = input('+, -, *, /, sq, pow: ')
if operator == 'sq':
    print(math.sqrt(n1))
    exit()

n2 = float(input('Number 2: '))
if operator == "pow":
    print(pow(n1, n2))
elif operator == '+':
    print(n1 + n2)
elif operator == '-':
    print(n1 - n2)
elif operator == '*':
    print(n1 * n2)
elif operator == '/':
    print(n1 / n2)
else:
    print(operator + " is not an operator")