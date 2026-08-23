def add(a, b):
  return  (a + b)

sum=add(2,3)    
print(sum)


def calculate_area(length, width):
    return length * width


if calculate_area(20,10)>180:
   print("Area is large")

result = calculate_area(10, 5) + 100
print(result)



def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication

result = calculate(10, 5)

print(result)

addition,subtraction,multiplication=calculate(30,5)

print(addition)
print(subtraction)
print(multiplication)