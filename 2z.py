import json

mayfile = "task_2.json"
with open(mayfile,encoding="utf-8") as read_file:
    data = json.load(read_file)
    m
    y
    data.sort(key=lambda user: user["shop"])
    print (data)
