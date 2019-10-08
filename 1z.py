import re
import requests
url=input("Введите URL-адрес:")'
 #\\ прямая ссылка для скачивание файла
s=requests.get(url).text
 #\\ выделить домен с помощью регулярного выражения
regex = re.findall("(\w*\.\w*/)", s)

print (regex)
