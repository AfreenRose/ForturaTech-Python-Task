salary = float(input("Enter Basic Salary: "))

hra = salary * 20 / 100
da = salary * 10 / 100

final_salary = salary + hra + da

print("Final Salary:", final_salary)