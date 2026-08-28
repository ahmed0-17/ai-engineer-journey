def calculate_total(prices:list[float])->float:
    total=0
    for price in prices:
       total+=price
    return total   


print(calculate_total([3.45,5.67,7.90]))

