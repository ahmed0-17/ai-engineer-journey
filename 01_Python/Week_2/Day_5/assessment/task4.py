from typing import Callable
def clean_text(text: str) -> str:
    return text.strip().lower()


def summarize(text: str) -> str:
    return text[:20]


def process_doc(function:Callable[[str],str],text:str)->str:
    return function(text)


print(process_doc(clean_text,"My nAME IS ahmED"))
print(process_doc(summarize,"Python is a high level dynamically typed language"))