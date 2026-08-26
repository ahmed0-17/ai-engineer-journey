matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(matrix[0])
# print(matrix[1][2])


# numbers = []

# for row in matrix:
#     for number in row:
#         numbers.append(number)

# print(numbers)

numbers = [number for row in matrix for number in row]

print(numbers)
squares = [number**2 for row in matrix for number in row]

print(squares)


evens = [number for row in matrix for number in row if number % 2 == 0]

print(evens)
