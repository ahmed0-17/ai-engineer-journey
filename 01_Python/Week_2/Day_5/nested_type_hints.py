def calculate_total_scores(students:list[dict[str,int]])->int:
    total=0
    for student in students:
        total+=list(student.values())[0]

    return total


students=[{"Ahmed":87},{"Ali":89}]
print(calculate_total_scores(students))
