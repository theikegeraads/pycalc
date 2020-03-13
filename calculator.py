import math
n1 = int(input("Getal 1: "))
module = input("+, -, *, /, sq: ")
n2 = int(input("Getal 2: "))
plus = n1 + n2
min = n1 - n2
keer = n1 * n2
deel = n1 / n2
kwad = math.pow(n1, n2)

if module == "+":
    print(plus)
else:
    pass

if module == "-":
    print(min)
else:
    pass
    
if module == "*":
    print(keer)
else:
    pass

if module == "/":
    print(deel)
else:
    pass
if module == "sq":
    print(kwad)
