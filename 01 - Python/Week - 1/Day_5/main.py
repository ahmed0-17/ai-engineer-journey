from utils.calculator import add,subtract
import student as std
import string_utils as stu

print(add(3,4))
print(subtract(3,4))

# print(division(3,4))
# print(multiplication(3,4))
marks=[75,80,90]
print(std.average(marks))
std.grade(78)


name="Ahmed Ali Malik"
print(stu.count_words(name))
print(stu.reverse_text(name))
print(stu.greet(name))