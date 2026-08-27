class MyNumbers:

    def __init__(self, max_number):
        self.current = 1
        self.max_number = max_number

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_number:
            number = self.current
            self.current += 1
            return number

        raise StopIteration


numbers = MyNumbers(5)

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))