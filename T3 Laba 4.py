salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение

x = 1.0
for i in range(10):
    need_money += ((salary - (spend * x)) * -1)
    x *= 1.03

print(round(need_money))
