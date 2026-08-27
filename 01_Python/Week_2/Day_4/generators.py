def get_numbers():
    yield 1
    yield 2
    yield 3

numbers = get_numbers()
print(next(numbers))
print(next(numbers))







# generator expressions


squares=(x**2 for x in range(2,11) if x%2==0)

print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))


