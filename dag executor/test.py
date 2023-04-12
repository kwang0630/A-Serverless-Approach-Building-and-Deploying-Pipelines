print(10)
def myfuc():
    input = 0
    def test():
        nonlocal input
        input += 1
    test()

myfuc()
print(input)