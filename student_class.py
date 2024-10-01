class Student:
    def __init__(self, full_name, faculty, course, min_grade):
        self.full_name = full_name
        self.faculty = faculty
        self.course = course
        self.min_grade = min_grade

    # Метод перевода на следующий курс
    def next_course(self):
        if self.min_grade >= 3:
            self.course += 1

    # Метод начисления стипендии
    def scholarship(self):
        if self.min_grade == 5:
            return 300
        elif self.min_grade == 4:
            return 200
        return 0

    # Метод для формирования строки информации
    def info(self):
        return (f"ФИО: {self.full_name}, Факультет: {self.faculty}, "
                f"Курс: {self.course}, Минимальная оценка: {self.min_grade}, "
                f"Стипендия: {self.scholarship()} грн")


# Класс Студент-контрактник (наследник)
class ContractStudent(Student):
    def __init__(self, full_name, faculty, course, min_grade, is_contract_paid):
        super().__init__(full_name, faculty, course, min_grade)
        self.is_contract_paid = is_contract_paid

    # Переопределение метода перевода на следующий курс
    def next_course(self):
        if self.min_grade >= 3 and self.is_contract_paid:
            self.course += 1

    # Переопределение метода стипендии
    def scholarship(self):
        return 0  # У контрактников стипендии нет

    # Метод для формирования строки информации
    def info(self):
        contract_status = "уплачен" if self.is_contract_paid else "не уплачен"
        return (f"ФИО: {self.full_name}, Факультет: {self.faculty}, "
                f"Курс: {self.course}, Минимальная оценка: {self.min_grade}, "
                f"Контракт: {contract_status}, Стипендия: {self.scholarship()} грн")
