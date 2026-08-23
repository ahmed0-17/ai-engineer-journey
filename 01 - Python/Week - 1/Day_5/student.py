


def average(num):
   
    return sum(num)/len(num)


def grade(avg):
    if avg>=80 and avg<=100:
         return ("A")
    elif avg>=70:
     return ("B")
    elif avg>=60:
     return  ("C")
    elif avg>=50:
     return ("D")
    else:
     return ("Fail")