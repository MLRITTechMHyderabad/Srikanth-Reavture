def salary_increase(employee):
    if employee["rating"] >= 4:
        bonus = employee["salary"] / 10
        employee["salary"] += bonus
    elif employee["rating"] == 3:
        bonus = employee["salary"] * 5 / 100  
        employee["salary"] += bonus
    else:
        bonus = employee["salary"] * 3 / 100  
        employee["salary"] = employee["salary"]- bonus
    return employee


employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]


updated_employees = [salary_increase(employee) for employee in employees]


print(updated_employees)