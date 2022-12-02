import math
import cmath

a, b, c = map(complex, input("Введите через пробел коэффиценты a, b и с уравнения ax^2+bx+c=0 (Пример1:2+3j 1 3-2j;Пример2:1 2 3):").split())
D = (b**2)-(4*a*c)
if a == 0 and b == 0 and c == 0: print("x - любое значение")
elif a == 0 and b == 0: print("утверждение неверно")
elif (a == 0 or b == 0) and c == 0: print("x=0")
elif a == 0:
    f = -1*(c/b)
    print(f"x={f.real}") if f.imag == 0 else print(f"x={f}")
elif b == 0:
    e = -1*(c/a)
    if e == 0: print("x=0")
    elif e.imag == 0 and e.real > 0: print(f"x={-1*(math.sqrt(e.real))}, {math.sqrt(e.real)}")
    else: print(f"x={-1*(cmath.sqrt(e))}, {cmath.sqrt(e)}")
# elif c == 0: # можно и без этого(обрабатывается далее)
#     if a.imag == 0 and b.imag == 0: print(f"x=0, {(-1*b.real)/(a.real**2)}")
#     else: print(f"x=0, {(-1*b)/pow(a, 2)}")
else:
    if a.imag == 0 and b.imag == 0 and c.imag == 0 and D.real >= 0:
        if D.real > 0: print(f"x={((-1*b+math.sqrt(D.real))/(2*a)).real}, {((-1*b-math.sqrt(D.real))/(2*a)).real}")
        elif D.real == 0: print(f"x={((-1*b)/2*a).real}")
    else: print(f"x={(-b+cmath.sqrt(D))/(2*a)}, {(-b-cmath.sqrt(D))/(2*a)}")