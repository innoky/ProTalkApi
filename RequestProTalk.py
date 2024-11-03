import requests, json

def SendRequest(prompt, chat_id, message_id, API_TOKEN):
    """
    Эта функция отправляет промпт в указанный чат в указанную ячейку для сообщения.
    """
    url = "https://api.pro-talk.ru/api/v1.0/send_message"
    payload = { "chat_id": f"c{chat_id}", "message_id": f"m{message_id}", "message": f"{prompt}" }
    headers =  { "Content-Type": "application/json", "Authorization": f"Bearer {API_TOKEN}", }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    return response


def GetLastMessage(chat_id, API_TOKEN):
    """
    Эта функция возвращает последнее сообщение из указанного чата
    """
    url = "https://api.pro-talk.ru/api/v1.0/get_messages"
    payload = {"chat_id": f"c{chat_id}"}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_TOKEN}", }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    return response.json()[-1]['content']


def GetAllMessages(chat_id, API_TOKEN):
    """
    Эта функция возвращает все сообщения в указанном чате в формате JSON
    """
    url = "https://api.pro-talk.ru/api/v1.0/get_messages"
    payload = {"chat_id": f"c{chat_id}"}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_TOKEN}", }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    result = response.json()
    print(result)
    return result[len(result) -1]

def CountMessages(chat_id, API_TOKEN):
    """
    Эта функция вспомогательная. +10, чтобы ID сообщения был с запасом. Не берите в голову
    """
    url = "https://api.pro-talk.ru/api/v1.0/get_messages"
    payload = {"chat_id": f"c{chat_id}"}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_TOKEN}", }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    return len(response.json())+1

def SendAndGetAnswer(prompt, chat_id, API_TOKEN):

    """
    Эта функция принимает на вход промпт, id чата и ваш токен, а возвращает ответ нейронки
    """
    message_id = CountMessages(chat_id=chat_id,API_TOKEN=API_TOKEN)
    SendRequest(
        prompt=prompt,
        chat_id=chat_id,
        message_id = message_id,
        API_TOKEN=API_TOKEN,
    )
    return GetLastMessage(chat_id, API_TOKEN=API_TOKEN)

print(SendAndGetAnswer(
    prompt="Философия на 30 января доделать прикрепленную рабочую тетрадь",
    chat_id = 1,
    API_TOKEN="11085_jwwPaM1D1lQaznUlQeEPPr6GUpYDwvHr"
))

# print(GetAllMessages(1,'11085_jwwPaM1D1lQaznUlQeEPPr6GUpYDwvHr'))