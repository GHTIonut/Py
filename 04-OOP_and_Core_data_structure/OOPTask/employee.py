class Employee:

    def __init__(self, name, email, salary, address):
        self.name = str(name)
        self.email = str(email)
        self.salary = float(salary)
        self.address = str(address)

    def check_email(self):
        if "@" in self.email:
            return True
        else:
            return False

    def increase_salary(self, percentage):
        self.salary = self.salary * (1 + percentage)
        return self.salary


