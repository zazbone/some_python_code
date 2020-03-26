import matplotlib.pyplot as plt


def is_premier(nombre, prim_liste):
    for i in prim_liste:
        if not nombre % i:
            return False
    return True


x = [i for i in range(3, 1000000)]
prim_liste = [2]
y = []
for i in x:
    if is_premier(i, prim_liste):
        prim_liste.append(i)
    y.append(len(prim_liste))
    if not i % 200:
        print(f"{i / 10000}%")
print(prim_liste)
plt.plot(x, y)
plt.show()
