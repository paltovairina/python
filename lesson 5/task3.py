salary_sum = []
workers_small_salary = []
with open("salary_amount.txt", "r", encoding="UTF-8") as worker_salary:
    for line in worker_salary:
        surname_sal = line.split()
        surname = surname_sal[0]
        salary_amount = surname_sal[1]
        salary_amount = float(salary_amount)
        if salary_amount < 20000:
            workers_small_salary.append(surname)
        salary_sum.append(salary_amount)
print(f"Сотрудники с окладом менее 20000:{workers_small_salary}")
mean_salary = sum(salary_sum) / len(salary_sum)
print(f"Средняя величина дохода сотрудников равна {mean_salary}")
