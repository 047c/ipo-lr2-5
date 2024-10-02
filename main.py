n = 1500
hours = 0
hours = n // 60
n = n - (hours * 60)
while hours > 24:
    hours = hours - 24
print(f"Количество часов: {hours}\nКоличество минут: {n}")
