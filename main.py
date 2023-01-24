import datetime
import time

from pyquery import PyQuery
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 250)
while True:
    try:
        doc = PyQuery(url="https://woiden.id/create-vps/")
        for i in doc.find("#datacenter").children():
            if "best" in i.text.lower():
                print("best出现了,web有了,赶紧去抢啊!")
                engine.say("best出现了,web有了,赶紧去抢啊!")
                engine.runAndWait()
            if i.text != "-select-":
                print(i.text)
        print(f"{datetime.datetime.now()}-------------")
        time.sleep(3)
    except:
        pass

    try:
        # 其实hax的可抢可不抢，虽然是kvm架构，但是速度和性能相比best差了一大截(
        doc = PyQuery(url="https://hax.co.id/create-vps/")
        for i in doc.find("#datacenter").children():
            if "eu-1" in i.text.lower():
                print("eu-1出现了,tz有了啊,赶紧去抢啊!")
                engine.say("eu-1出现了,tz有了啊,赶紧去抢啊!")
                engine.runAndWait()
            if i.text != "-select-":
                print(i.text)
        print(f"{datetime.datetime.now()}-------------")
        time.sleep(3)
    except:
        pass
