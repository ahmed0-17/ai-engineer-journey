try:
      # risky code
    number1 = int(input("Enter a number1: "))
    number2 = int(input("Enter a number2: "))
    result = number1 / number2
    print(result)

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



# file = None

# try:
#     file = open("data.txt")
#     # work with file

# except FileNotFoundError:
#     print("File not found.")

# else:
#     print("file is existed")    

# finally:
#     if file:
#         file.close()


