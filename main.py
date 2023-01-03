import time

from pyquery import PyQuery
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 125)
while True:
    doc = PyQuery(url="https://woiden.id/create-vps/")

    for i in doc.find("#datacenter").children():
        if "best" in i.text.lower():
            print("best出现了,赶紧去抢啊!")
            engine.say("best出现了,handsome有了,赶紧去抢啊!")
            engine.runAndWait()
        if i.text != "-select-":
            print(i.text)
    print("-------------")
    time.sleep(3)

    doc = PyQuery(url="https://hax.co.id/create-vps/")

    for i in doc.find("#datacenter").children():
        if "eu-1" in i.text.lower():
            print("eu-1出现了,赶紧去抢啊!")
            engine.say("eu-1出现了,tz有了啊,赶紧去抢啊!")
            engine.runAndWait()
        if i.text != "-select-":
            print(i.text)
    print("-------------")
    time.sleep(3)
