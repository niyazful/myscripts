dict_of_orders = {}
dict_of_promocodes = {}

num_of_orders = int(input("Введите количество заказов:\t"))
num_of_promocodes = int(input("Введите количество промокодов:\t"))
for i in range(num_of_orders):
    order_id = input(str(i+1)+" заказ =\t")
    promocode_id = input(str(i+1)+" промокод =\t")
    dict_of_orders[order_id]=promocode_id

for i in range(num_of_promocodes):
    promocode_id = input(str(i+1)+" промокод =\t")
    name = input("Название промокода =\t")
    discount = input("Скидка:\t")
    dict_of_promocodes[promocode_id]=name,discount

print("Доля заказов с промокодами:\t",len(dict_of_promocodes)/len(dict_of_orders))

rev_dict = {}

for key, value in dict_of_orders.items():
    rev_dict.setdefault(value, set()).add(key)

result = [key for key, values in rev_dict.items()
          if len(values) > 1]
dupkey = result[0]
sum_of_use = 0

for key,value in dict_of_orders.items():
    if value == dupkey:
        sum_of_use+=1

print("Самый популярный промокод", str(result[0])," был использован ", str(sum_of_use), "раз")
#print(dict_of_orders)
#print(dict_of_promocodes)
