import tkinter as tk
from tkinter import Text
from time_class import Time
from rectangle_class import Rectangle
from student_class import Student, ContractStudent

# Функция для вывода информации о времени
def show_time_info():
    time1 = Time(10, 30, 45)
    minutes_left = time1.minutes_until_midnight()
    time1.add_minutes()

    output_text.delete(1.0, tk.END)  # Очистка окна вывода
    output_text.insert(tk.END, f"Текущее время: {time1}\n")
    output_text.insert(tk.END, f"Минут до полуночи: {minutes_left}\n")
    output_text.insert(tk.END, f"После добавления 100 минут: {time1}\n")

# Функция для вывода информации о прямоугольнике
def show_rectangle_info():
    rect = Rectangle(0, 0, 4, 3)
    
    output_text.delete(1.0, tk.END)  # Очистка окна вывода
    output_text.insert(tk.END, f"Информация о прямоугольнике:\n")
    output_text.insert(tk.END, f"{rect}\n")

# Функция для вывода информации о студентах
def show_students_info():
    student1 = Student("Иван Иванов", "Физика", 1, 4)
    contract_student1 = ContractStudent("Петр Петров", "Математика", 1, 5, True)
    contract_student2 = ContractStudent("Анна Антонова", "Биология", 2, 3, False)

    output_text.delete(1.0, tk.END)  # Очистка окна вывода
    output_text.insert(tk.END, f"{student1.info()}\n")
    output_text.insert(tk.END, f"{contract_student1.info()}\n")
    output_text.insert(tk.END, f"{contract_student2.info()}\n")

    # Применение метода перевода на следующий курс
    student1.next_course()
    contract_student1.next_course()
    contract_student2.next_course()

    # Вывод информации после перевода на следующий курс
    output_text.insert(tk.END, f"\nПосле перевода на следующий курс:\n")
    output_text.insert(tk.END, f"{student1.info()}\n")
    output_text.insert(tk.END, f"{contract_student1.info()}\n")
    output_text.insert(tk.END, f"{contract_student2.info()}\n")

# Создание главного окна
root = tk.Tk()
root.title("Демонстрация работы классов")
root.geometry("600x400")

# Поле для вывода (аналог Memo)
output_text = Text(root, wrap=tk.WORD, height=15, width=70)
output_text.pack(pady=10)

# Кнопки для выполнения функций
btn_time = tk.Button(root, text="Показать время", command=show_time_info)
btn_time.pack(pady=5)

btn_rectangle = tk.Button(root, text="Показать прямоугольник", command=show_rectangle_info)
btn_rectangle.pack(pady=5)

btn_students = tk.Button(root, text="Показать студентов", command=show_students_info)
btn_students.pack(pady=5)

# Запуск основного цикла приложения
root.mainloop()
