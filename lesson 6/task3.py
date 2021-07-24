class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"Полное имя сотрудника - {self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


worker_inform = Position("Sergey", "Ivanov", "Biology teacher", 10000, 15000)
print(worker_inform.position)
print(worker_inform.get_full_name())
print(worker_inform.get_total_income())
