import random
import math

def greet_user():
    name = input("Введіть ваше ім'я: ")
    age = int(input("Введіть ваш вік: "))
    print(f"Привіт {name}, тобі {age}!")

def check_access():
    age = int(input("Введіть ваш вік: "))
    if age >= 18:
        print("Вхід дозволено!")
    else:
        print("Вхід заборонено!")

def guess_number():
    number = random.randint(1, 10)
    attempts = 3
    while attempts > 0:
        guess = int(input("Вгадайте число від 1 до 10: "))
        if guess > number:
            print("Менше")
        elif guess < number:
            print("Більше")
        else:
            print("Вітаю, ви вгадали!")
            return
        attempts -= 1
    print(f"Ви програли! Загадане число було {number}.")

def print_range():
    start = int(input("Введіть початкове число: "))
    end = int(input("Введіть кінцеве число: "))
    for i in range(start, end + 1):
        print(i, end=" ")
    print()

def print_even_reverse():
    n = int(input("Введіть число n: "))
    for i in range(n, 0, -1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

def factorial():
    n = int(input("Введіть число для обчислення факторіалу: "))
    print(f"Факторіал {n} дорівнює {math.factorial(n)}")

def grade_student():
    score = int(input("Введіть кількість балів: "))
    if score < 50:
        print("Незадовільно")
    elif score < 70:
        print("Задовільно")
    elif score < 90:
        print("Добре")
    else:
        print("Відмінно")

def calculator():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    operation = input("Введіть операцію (+, -, *, /): ")
    if operation == "+":
        print(f"Результат: {a + b}")
    elif operation == "-":
        print(f"Результат: {a - b}")
    elif operation == "*":
        print(f"Результат: {a * b}")
    elif operation == "/":
        if b == 0:
            print("Ділення на нуль")
        else:
            print(f"Результат: {a / b}")
    else:
        print("Невідома операція")

# Виклик бажаної функції для тестування
# greet_user()
# check_access()
# guess_number()
# print_range()
# print_even_reverse()
# factorial()
# grade_student()
# calculator()