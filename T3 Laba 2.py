list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max = (list_numbers[0])
i_max = 0
for i in range(len(list_numbers)):
    if max < list_numbers[i]:
        max = list_numbers[i]
        i_max = i

list_numbers[i_max], list_numbers[len(list_numbers)-1] = list_numbers[len(list_numbers)-1], list_numbers[i_max]
print(list_numbers)
