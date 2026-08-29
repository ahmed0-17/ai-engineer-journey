from typing import Callable


def clean_text(text:str)->str:
    return text.strip().lower()


def add_ai_prefix(text:str)->str:
    return f"AI response : {text}"


def run_processor(task:Callable[[str],str],text:str)->str:
    return task(text)



print(run_processor(clean_text,"Hi HOW aRe you"))
print(run_processor(add_ai_prefix,"Hi HOW aRe you"))