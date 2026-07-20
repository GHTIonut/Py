employees = [
    {"name": "Peter", "salary": 50000},
    {"name": "Mila", "salary": 60000},
    {"name": "Nemanja", "salary": 55000},
]

increased_salary_employees = list(map(lambda x: {"name": x["name"], "salary": x["salary"] * 1.05}, employees))
print(increased_salary_employees)
for e in increased_salary_employees:
    print(f"{e["name"]}'s salary was increased to {e["salary"]}")