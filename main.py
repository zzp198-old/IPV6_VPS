import time

from pyquery import PyQuery

while True:
    doc = PyQuery(url="https://woiden.id/create-vps/")

    for i in doc.find("#datacenter").children():
        if "best" in i.text.lower():
            print("best出现了,赶紧去抢啊!")
        if i.text != "-select-":
            print(i.text)

    print("-------------")
    time.sleep(3)
