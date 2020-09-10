class Foo:
    def __str__(self):
        return "Hello world!"


a = locals()["Foo"]()
print(a)
