names = ["ahmed", "ali", "usman"]

upper_names = [name.upper() for name in names]

print(upper_names)

# numbers=[number for number in range(1,11,2)]
# numbers=[number*number for number in range(1,11,2)]
numbers = [number for number in range(1, 11) if number % 2 == 0]

print(numbers)



squares = [
    number * number
    for number in range(1, 11)
    if number % 2 == 0
]

print(squares)

numbers=[1,2,3,4,5,6,7,8,9]
even_odd=["Even" if number % 2 == 0 else "Odd" for number in numbers]
print(even_odd)

numbers = [1, 2, 3, 4, 5]

result = [number * 2 if number % 2 == 0 else number * 3 for number in numbers]

print(result)