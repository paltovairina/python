class Data:

    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def int_data(cls, day_month_year):
        int_dmy = []
        split_dmy = day_month_year.split("-")
        for i in split_dmy:
            i = int(i)
            int_dmy.append(i)
        day = int_dmy[0]
        month = int_dmy[1]
        year = int_dmy[2]
        return day, month, year

    @staticmethod
    def valid_dmy(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f"Всё правильно"
                else:
                    return f"Неправильно введён год"
            else:
                return f"Неправильно введён номер месяца"
        else:
            return f"Неправильно введён день"

    def __str__(self):
        return f'Текущая дата {Data.int_data(self.day_month_year)}'


date = Data("10-04-2021")
print(date)
print(Data.valid_dmy(10, 1, 2050))
print(date.valid_dmy(2, 15, 2009))
print(Data.valid_dmy(1, 5, 1900))
print(Data.int_data('02 - 03 - 2008'))
print(date.int_data('11 - 11 - 2020'))
