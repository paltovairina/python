from sys import argv
script_name, work_hours, rate_wage, bonus = argv
wage = float(work_hours) * float(rate_wage) + float(bonus)
print(f"Заработная плата равна {wage}")
