from math import sqrt


def sigma_heron1(AB, BD, DC, CA, BC, AD):
    delta_l = 0.0007
    delta_a = 0.000009
    l_1 = 0.5 * (AB + BC + CA)
    l_2 = 0.5 * (DC + BC + BD)
    A = (l_1-AB)*(l_1-BC)*(l_1-CA)
    B = (l_2 - DC)*(l_2 - BC)*(l_2 - BD)
    A += l_1 * ((l_1-AB)*(l_1-BC) + (l_1-BC)*(l_1-CA) + (l_1-AB)*(l_1-CA))
    B += l_2 * ((l_2 - DC)*(l_2 - BC) + (l_1 - BC)*(l_1 - BD) + (l_1 - DC)*(l_1 - BD))
    A = A ** 2
    B = B ** 2
    A *= delta_l ** 2
    B *= delta_l ** 2
    A += -l_1 * ((l_1-BC)*(l_1-CA) + (l_1-AB)*(l_1-CA) + (l_1-BC)*(l_1-AB)) * delta_a ** 2
    B += -l_2 * ((l_1 - BC)*(l_1 - BD) + (l_1 - DC)*(l_1 - BD) + (l_1 - BC)*(l_1 - DC)) * delta_a ** 2
    return A + B


def sigma_bretschneider(AB, BD, DC, CA, BC, AD):
    delta_a = 0.000009
    sigma_aire = (AB*AB + BD*BD + DC*DC + CA*CA)
    sigma_aire *= (-AB*AB + BD*BD - DC*DC + CA*CA) ** 2
    sigma_aire += 4 * (BC*BC*AD + AD*AD*BC) ** 2
    sigma_aire /= 4 * (4*BC*BC*AD*AD -(-AB*AB + BD*BD - DC*DC + CA*CA) ** 2)
    return sigma_aire * delta_a


def sigma(values):
    average = sum(values) / len(values)
    quad_average = sum((x - average)**2 for x in values) / (len(values) - 1)
    sigma = 1.84 * sqrt(quad_average)
    return sigma / sqrt(2)


def area_bretschneider(AB, BD, DC, CA, BC, AD):
    area = -((BD*BD + CA*CA - AB*AB - DC*DC) ** 2)
    area += 4 * BC*BC * AD*AD
    area = sqrt(area)
    area /= 4
    return area


def area_heron(AB, BD, DC, CA, BC, AD):
    l_1 = 0.5 * (AB + BC + CA)
    l_2 = 0.5 * (DC + BC + BD)
    aire_1 = sqrt(l_1 * (l_1 - AB) * (l_1 - BC) * (l_1 - CA))
    aire_2 = sqrt(l_2 * (l_2 - DC) * (l_2 - BC) * (l_2 - BD))
    return aire_1 + aire_2


AB = 1.978
AC = 4.477
AD = 3.619
BC = 5.628
BD = 2.225
CD = 5.364

BA = 1.998
CA = 4.474
DA = 3.618
CB = 5.678
DB = 2.224
DC = 5.396

mAB = (AB + BA) / 2
mAC = (AC + CA) / 2
mAD = (AD + DA) / 2
mBC = (BC + CB) / 2
mBD = (BD + DB) / 2
mCD = (CD + DC) / 2

sigma_mAB = sigma((AB, BA))
sigma_mAC = sigma((AC, CA))
sigma_mAD = sigma((AD, DA))
sigma_mBC = sigma((BC, CB))
sigma_mBD = sigma((BD, DB))
sigma_mCD = sigma((CD, DC))

print(mAB)
print(sigma_mAB)
print(area_bretschneider(AB, BD, DC, CA, BC, AD), "bretschneider")
print(area_heron(AB, BD, CD, CA, BC, AD), "heron")
print(area_bretschneider(mAB, mBD, mCD, mAC, mBC, mAD), "Mbretschneider")
print(area_heron(mAB, mBD, mCD, mAC, mBC, mAD), "Mheron")
print(sigma_heron1(AB, BD, DC, CA, BC, AD))
print(sigma_bretschneider(AB, BD, DC, CA, BC, AD))