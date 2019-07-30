import requests
from main import main_select
from misc import token
from time import sleep


#https://api.telegram.org/bot879499363:AAH80agvPpGX-Mzzdn_aAhZ4-Ni0MN5FYwU/sendmessage?chat_id=506242371&text=%20%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82


URL = "https://api.telegram.org/bot" + token + "/"
global last_update_id 
last_update_id = 0

def get_updates():
    url = URL + "getUpdates"
    r = requests.get(url)
    return r.json()

def get_message():
    #Отвечать тольео на новые сообщения
    #Получаем update_id каждого обновления
    #записываем в переменную,а затем сравнивать с update_id последнего элемента 
    #в списке result
    
    data = get_updates()

    last_object = data['result'][-1]
    current_update_id = last_object['update_id']
    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id = data['result'][-1]['message']['chat']["id"]
        message_text = data["result"][-1]["message"]["text"]
        message = {"chat_id" : chat_id,
                    'text' : message_text}
        return message
    return None

def send_message(chat_id, text = "hello my friend!"):
    url = URL + "sendmessage?chat_id={}&text={}".format(chat_id, text)
    requests.get(url)

def main():
    # d = get_updates()
    # with open("D:/Python/project/mr.kaa/updates.json", "w") as file:
    #     json.dump(d, file, indent = 2, ensure_ascii = False)
    answer = get_message()
    chat_id = answer["chat_id"]
    text = answer['text']
    send_message(chat_id, "Привет,чтобы посмотреть курс валют,набери команду /btc@MrKaa_bot")
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer["chat_id"]
            text = answer['text']
            if text == "/btc@MrKaa_bot":
                send_message(chat_id, "Вот курс валют  данный момент:")
                send_message(chat_id, 'usd_client, usd_bank, euro_client, euro_bank, rub_client, rub_bank')
                send_message(chat_id, main_select())
        else:
            continue
        sleep(5)
if __name__ == "__main__":
    main()
   