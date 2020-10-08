def ask(prompt, data_type=int):
    while True:
        try:
            a = data_type(input(prompt))
            return a
        except ValueError:
            print(f"Please give a input string convertible in {data_type.__name__} ")
