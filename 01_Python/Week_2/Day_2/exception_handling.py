try:
      # risky code
    number1 = int(input("Enter a number1: "))
    number2 = int(input("Enter a number2: "))
    result = number1 / number2
 

except ZeroDivisionError:
        # handle error
    print("You cannot divide by zero.")

except ValueError:
      # handle error
    print("Please enter a valid number.")

else:
     # runs if successful
    print("division successful")
    print("Answer is : ",result)

finally:
        # always runs
     print("Program finished")



# 2nd example

try:
    file = open("file.txt", "r")
    content = file.read()

except FileNotFoundError:
    print("File not found.")

else:
    print("File exists.")
    print(content)

finally:
    try:
        file.close()
        print("File is closed")
    except NameError:
        print("File was never opened")

    print("Program is finished")