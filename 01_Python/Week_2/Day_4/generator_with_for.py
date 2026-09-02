def count_down(number):

    while number > 0:
        yield number
        number -= 1


for number in count_down(5):
    print(number)

