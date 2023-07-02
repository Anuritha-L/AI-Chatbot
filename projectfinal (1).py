from _tkinter import *
from http import server
import random
from datetime import datetime
import pywhatkit as kt
from subprocess import call
import subprocess
import cv2
import pyttsx3
import speech_recognition as tp
import smtplib
import time
import webbrowser
import requests
from pprint import pprint
import bs4 as bs4
ct = datetime.now()


def countdown(y):
    while y > 0:
        print(y)
        eng.say(str(y))
        eng.runAndWait()
        y = y-1
        time.sleep(1)
    print('bot->times up')
    eng.say('times up')
    eng.runAndWait()


def good():
    # print(ct.hour)
    if ct.hour <= 12 and ct.hour >= 6:
        q = "Good Morning"
    elif ct.hour > 12 and ct.hour < 18:
        q = "Good afternoon"
    else:
        q = "Good evening"
    return q


def name():
    print("bot -> My name is beelzebub ,what's yours")
    eng.say("My name is beelzebub ,what's yours")
    eng.runAndWait()
    v = input()
    print("bot -> nice to meet you "+v)
    eng.say('nice to meet you')
    eng.runAndWait()


def cam():
    print('bot->opening camera')
    eng.say("opening camera")
    eng.runAndWait()
    cam = cv2.VideoCapture(0)
    count = 0
    while True:
        suc, f = cam.read()
        if suc:
            cv2.imshow("web cam", f)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.waitKey(1) & 0xFF == ord(' '):
            img_name = f'image{count}.png'
            cv2.imwrite(img_name, f)
            count += 1
    cam.release()
    cv2.destroyAllWindows()


def sear():
    z = ui.split()
    z.remove('search')
    # print(z)
    t = ""
    for i in z:
        t += i+' '
        # print(t)
    print(f'bot->searching {t}in google')
    eng.say(f'searching {t} in google')
    eng.runAndWait()
    kt.search(t)


def play():
    z = ui.split()
    # print(z)
    z.remove('play')
    # print(z)
    t = ""
    for i in z:
        t += i+' '
    print(f"bot->playing {t}on youtube")
    eng.say(f'playing {t}on youtube')
    eng.runAndWait()
    kt.playonyt("https://www.youtube.com/results?search_query="+t)


def open_py_file():
    call(['python', 'r,p,s.py'])


def mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('muhammadsuarim@gmail.com', 'gpqaspqgvzzfhbps')
    tad = input('inpput to address = ')
    subject = input('enter subject = ')
    body = input('enter body = ')
    msg = f'subject:{subject}\n\n{body}'

    server.sendmail(from_addr='muhammadsuraim@gmail.com',
                    to_addrs=tad, msg=msg)
    print('bot->mail was sent')


def cal():
    pass
    print('bot->opening calculator')
    eng.say('opening calculator')
    eng.runAndWait()
    subprocess.Popen('C:\\Windows\\System32\\calc.exe')


def web():
    z = ui.split()
    # print(z)
    z.remove('open')
    # print(z)
    t = ""
    for i in z:
        t += i
    print(f'bot->opening {t}')
    eng.say(f'opening {t}')
    eng.runAndWait()
    webbrowser.open(f'https://www.{t}.com/')


eng = pyttsx3.init('sapi5')
voices = eng.getProperty('voices')
# print(voices[0].id)
eng.setProperty('voice', voices[1].id)

gr = ['hello', 'hi', 'whats up']
gs = ['hi', 'hello', 'nice to meet you', good()]
er = ['bye', 'see you later', 'talk to you later']
es = ['take care see you later', 'bye bye', 'bye']
while 1:
    r = tp.Recognizer()
    with tp.Microphone() as source:
        print("user->", end='')
        r.adjust_for_ambient_noise(source, duration=.2)
        aa = r.listen(source)
        ui = ''
        try:
            ui = r.recognize_google(aa, language='en-in')
            ui.lower()
            print(ui)
        except:
            print("try again")
            continue
    z = ui.split()
    if ui in gr:
        tt = random.choice(gs)
        print('bot->', tt)
        eng.say(tt)
        eng.runAndWait()
    elif 'time' in ui.split():
        eng.say(ct.hour)
        eng.say(ct.minute)
        eng.runAndWait()
    elif 'name' in ui.split() and 'your' in ui:
        name()
    elif ui in er:
        pp = random.choice(es)
        print('bot -> '+pp)
        eng.say(pp)
        eng.runAndWait()
        break
    elif 'search' in ui.split():
        sear()
    elif 'timer' in ui.split():
        yu = int(input('enter count = '))
        countdown(yu)
    elif 'game' in ui.split():
        open_py_file()
    elif 'play' in ui.split():
        play()
    elif 'camera' in ui.split():
        cam()
    elif 'mail' in ui.split():
        mail()
    elif 'calculator' in ui.split() and 'open' in ui.split():
        cal()
    elif 'open' in ui.split():
        web()
    else:
        print(f'bot->heres a google search for {ui}')
        eng.say(f'heres a google search for {ui}')
        eng.runAndWait()
        kt.search(ui)
