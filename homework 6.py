result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a повинно бути не менше за b")
        if b > 100:
            raise IndexError("b не може бути більше за 100")
        return a / b
    except ZeroDivisionError:
        print(f"Помилка: Ділення на нуль ({a} / {b})")
    except ValueError as e:
        print(f"Помилка: {e}")
    except IndexError as e:
        print(f"Помилка: {e}")

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(int(key), value) 
        if res is not None:
            result.append(res)
    except (TypeError, ValueError) as e:
        print(f"Помилка: неможливо виконати операцію з {key}: {e}")

print(result)

