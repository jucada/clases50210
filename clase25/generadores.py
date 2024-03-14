def generador():
    yield 10


for x in generador():
    print(x)
