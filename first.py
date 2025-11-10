info = {
"név": "Benedek",
"kor": "17",
"tantárgy": "informatika    "
}

# print(info["tantárgy"])

info["iskola"] = "Vak Bottyán"

info["kor"] = 18

del info["tantárgy"]

for i in info.keys():
    print (i)


for i in info.values():
    print(i)

for i in info.items():
    print(i)