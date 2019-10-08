def count(argument, array):
    multiple = 1
    for y in range(len(array)):
        if y == argument:
            continue
        multiple *= array[y]
    return multiple


num = int(input("Введите количество чисел в массиве:\t"))
list_of_nums = []

for i in range(num):
    list_of_nums.append(int(input(str(i+1)+" элемент =\t")))

memory = dict()
maxim = 0

for i in range(num):
    variable = count(i,list_of_nums)
    memory[i] = variable
    if variable > maxim:
        maxim = variable

for iters, value in memory.items():
    if value == maxim:
        list_of_nums.pop(iters)

print(list_of_nums)
