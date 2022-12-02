import math

a, b, c = map(float, input("Введите коэффиценты a, b и с уравнения ax^2+bx+c=0:").split())
D = (b**2)-(4*a*c)
if a == 0 and b == 0 and c == 0: print("x - любое значение")
elif a == 0 and b == 0: print("утверждение неверно")
elif (a == 0 or b == 0) and c == 0: print("x=0")
elif a == 0: print(f"x={-1*(c/b)}")
elif b == 0:
    e = -1*(c/a)
    if e < 0: print(f"нет решений")
    elif e == 0: print("x=0")
    else: print(f"x={-1*(math.sqrt(e))}, {math.sqrt(e)}")
elif c == 0: print(f"x=0, {(-1*b)/(a**2)}")
else:
    if D > 0: print(f"x={(-1*b+math.sqrt(D))/(2*a)}, {(-1*b-math.sqrt(D))/(2*a)}")
    elif D == 0: print(f"x={(-1*b)/2*a}")
    else: print("решений нет")