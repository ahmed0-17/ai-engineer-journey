def calculate_total(prices:list[float])->float:
     return sum(prices)

print(calculate_total([3.45,5.67,7.90]))


#dict type hint
def get_score(scores:dict[str,int])->int:
     
     return sum(scores.values())


print(get_score(
                {"Ahmed":85,
                 "Ali":77,
                 "Abid":81,
                 "Anus":89
                 }
                 ))



#tuple type hint
#we can define tuples types based on position
def get_user_info(user:tuple[str,int|None])->str | None:
     if user[0] is None:
          return f"User is {user[1]} years old ."
     return f"{user[0]} is {user[1]} years old ."
  


print(get_user_info((None,22)))



#set type hint
def count_unique_skills(skills:set[str])->int:
    return len(skills)



skills={"Python","Fastapi","Rag","Python"}
print(count_unique_skills(skills))