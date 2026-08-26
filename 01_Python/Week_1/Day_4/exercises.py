

numbers=[number for number in range(1,11)]
print(numbers)




squares=[number**2 for number in range(1,11)]
print(squares)


evens=[number for number in range(1,11) if number%2==0]
print (numbers)

odds=[number**2 for number in range(1,11) if number%2 !=0]
print(odds)


numbers = [10, -5, 20, -2, 30, -7, 4]
positives=[number for number in numbers if number>0 and number%2==0]
print(positives)




numbers=[1,2,3,4,5,6,7,8,9]
even_odd=["Even" if number % 2 == 0 else "Odd" for number in numbers]
print(even_odd)

numbers = [5, 10, 15, 20, 25]

new_list=["Yes" if number %10==0 else "No" for number in numbers]
print(new_list)


numbers = [-10, -5, 0, 5, 10]

status=["Positive" if number >0   else "Zero" if number==0 else "Negative" for number in numbers]
print(status)


numbers = [1, 2, 3, 4, 5, 6]
new_list=[number**2 if number%2==0 else number**3 for number in numbers]
print(new_list)


numbers = [-5, 0, 3, 8, -2, 10, 7]
status=["Positive even" if number%2==0 and number>0 else "Positive odd" if number%2!=0 and number>0 else "zero" if number==0 else"negative" for number in numbers]
print(status)



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

lists=[number for row in matrix  for number in row]
print(lists)

odds=[odds for row in matrix for odds in row if odds %2!=0 and odds>0 ]
print(odds)

square=[square **2 for row in matrix for square in row ]
print(square)

evens_square=[even**2 for row in matrix for even in row if even %2==0 and even>0]
print(evens_square)