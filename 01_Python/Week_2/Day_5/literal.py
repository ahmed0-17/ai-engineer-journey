from typing import Literal
def process_status(status:Literal["pending","completed","failed"]):
    return f"Status: {status}"


print(process_status("pending"))