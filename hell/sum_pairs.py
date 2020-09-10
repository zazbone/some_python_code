print(*(lambda a: [f"Current Number {x} Previous Number {y} Sum: {x + y}" for x, y in zip(a[1:], a[:-1])])(list(int(input(f"Element number {i + 1}: ")) for i in range(10))), sep='\n')


# Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number
# From: https://pynative.com/python-basic-exercise-for-beginners/
