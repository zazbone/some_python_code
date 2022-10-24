q = lambda x: x if len(x) <= 1 else q([i for i in x if i < x[0]]) + [i for i in x if i == x[0]] + q([i for i in x if i > x[0]])
# ([int(i) for i in input("Give a list of int: ").split(",")])
print(q([1, 5, 12, 90, 4, 54, 23, 81, 2, 1]))
print(q([2, 2]))
