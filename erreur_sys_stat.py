from math import sqrt
from numpy import power

def aire(a, b, c, d, e, f):
    Aire = 0.25 * sqrt(4 * e*e * f*f - power(-a*a + b*b - c*c + d*d, 2))
    return Aire


def incert(a, b, c, d, e, f):
    fear       = -a*a + b*b - c*c + d*d
    Delta_Aire = 0.0002 * (fear*fear * (a*a + b*b + c*c + d*d) + 4 * (e * f*f + f * e*e) ** 2)
    return Delta_Aire /(4 * (4 * e*e * f*f - fear * fear))

a = 1.988
b = 2.2245
c = 4.475 
d = 5.380
e = 3.6185
f = 5.653 
print(4 * e*e * f*f - power(-a*a - b*b + c*c + d*d, 2))
print(aire(a, b, c, d, e, f), "Metre carre")
print(incert(a, b, c, d, e, f), "Metre carre")
