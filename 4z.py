num_of_first = int(input("Введите количество элементов в первом массиве:\t"))
num_of_second = int(input("Введите количество элементов во втором массиве:\t"))

first_list = [int(input(str(i+1)+" элемент первого массива:\t")) for i in range(num_of_first)]
print()
second_list = [int(input(str(i+1)+" элемент второго массива:\t")) for i in range(num_of_second)]
first_list.sort()
second_list.sort()


intersect = []
for i in first_list:
    if i in second_list:
        intersect.append(i)
intersect = list(dict.fromkeys(intersect))
print(intersect)