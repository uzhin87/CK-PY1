money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

x = 1.0
while money_capital + salary >= spend * x:
    money_capital += salary
    if money_capital - spend * x >= 0:
        money_capital -= spend * x
        month += 1
    x += increase
print("Если ЗП приходит до трат", month)

money_capital = 10000
month = 0
x = 1.0
while money_capital >= spend * x:
    if money_capital - spend * x >= 0:
        money_capital -= spend * x
        month += 1
    x += increase
    money_capital += salary


print("Если ЗП приходит после трат", month)
