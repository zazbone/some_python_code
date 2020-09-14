print(
*(lambda a, b: (i for i, j in __import__("itertools").chain(a, b) if (object.__eq__,object.__ne__)[j](i % 2, 1) ))
(*([(int(i), j) for i in input("Give a list of int: ").split(',')] for j in range(2)))
)
