# Импорт классов из других файлов
from time_class import Time
from rectangle_class import Rectangle
from student_class import Student, ContractStudent

# Демонстрация работы с классом Time
time1 = Time(10, 30, 45)
print(time1)

# Определение минут до полуночи
minutes_left = time1.minutes_until_midnight()
print(f"Минут до полуночи: {minutes_left}")

# Увеличение времени на 100 минут
time1.add_minutes()
print(f"После добавления 100 минут: {time1}")

# Демонстрация работы с классом Rectangle
rect = Rectangle(0, 0, 4, 3)
print(rect)

# Демонстрация работы с классами Student и ContractStudent
student1 = Student("Иван Иванов", "Физика", 1, 4)
contract_student1 = ContractStudent("Петр Петров", "Математика", 1, 5, True)
contract_student2 = ContractStudent("Анна Антонова", "Биология", 2, 3, False)

# Вывод информации о студентах
print(student1.info())
print(contract_student1.info())
print(contract_student2.info())

# Применение метода перевода на следующий курс
student1.next_course()
contract_student1.next_course()
contract_student2.next_course()

# Снова вывод информации после перевода
print(student1.info())
print(contract_student1.info())
print(contract_student2.info())
