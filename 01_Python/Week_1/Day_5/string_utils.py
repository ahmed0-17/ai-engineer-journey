def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
     print(greet("Ali"))

def count_vowels(value):
    vowels = 0

    for alphabet in value.lower():
        if alphabet in "aeiou":
            vowels += 1

    return vowels


def reverse_text(text):
     return text[::-1] 


def count_words(text):
     return len(text.split())     


