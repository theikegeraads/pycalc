import math
n1 = int(input('Getal 1: '))
operator = input('+, -, *, /, sq, pow: ')

wort = math.sqrt(n1)
if operator == 'sq':
    print(wort)
    exit()
else:
    pass

kwad = pow(n1, 2)
if operator == 'pow':
    print(kwad)
    exit()
else:
    pass

n2 = int(input('Getal 2: '))

plus = n1 + n2
min = n1 - n2
keer = n1 * n2
deel = n1 / n2

if operator == '+':
    print(plus)
else:
    pass

if operator == '-':
    print(min)
else:
    pass

if operator == '*':
    print(keer)
else:
    pass

if operator == '/':
    print(deel)
else:
    pass