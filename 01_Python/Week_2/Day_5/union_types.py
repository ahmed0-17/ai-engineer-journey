def process_id(user_id: str | int) -> str:
    return f"User ID: {user_id}"

print(process_id("34"))



def format_price(price:int | float):
    return f"Price : ${price}."


print(format_price(150))
print(format_price(99.5))