print((lambda x, y: x * y if x * y < 1000 else x + y)(*(int(input(f"Give {i + 1} number: ")) for i in range(2))))

# Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum
# From: https://pynative.com/python-basic-exercise-for-beginners/
