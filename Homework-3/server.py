# save this as app.py
import time
import datetime

import flask
from flask import Flask, abort

app = Flask(__name__)
db = []
for i in range(3):
    db.append({
        'name': 'Anton',
        'time': 12343,
        'text': 'text01923097'
    })

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/send", methods= ['POST'])
def send_message():
    '''
    функция для отправки нового сообщения пользователем
    :return:
    '''
    # TODO
    # проверить, является ли присланное пользователем правильным json-объектом
    # проверить, есть ли там имя и текст
    # Добавить сообщение в базу данных db
    data = flask.request.json
    if not isinstance(data, dict):
        return abort(400)

    if 'name' not in data or \
        'text' not in data:
        return abort(400)

    # проверка, есть ли имя у пользователя
    if isinstance(data['name'], type(None)):
        data['name'] = 'Аноним'

    if not isinstance(data['name'], str) or \
        not isinstance(data['text'], str) or \
        len(data['name']) == 0 or \
        len(data['text']) == 0:
        return abort(400)

    text = data['text']
    name = data['name']
    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
    db.append(message)
    return {'ok': True}

@app.route("/messages")
def get_messages():
    try:
        after = float(flask.request.args['after'])
    except:
        abort(400)
    db_after = []
    for message in db:
        if message['time'] > after:
            db_after.append(message)
    return {'messages': db_after}

@app.route("/status")
def print_status():
    messanger_users = []

    # собираем все имена из сообщений
    for message in db:
        messanger_users.append(message['name'])

    # убираем дубликаты
    messanger_users = set(messanger_users)

    # получаем длины списков
    number_of_users = len(messanger_users)
    number_of_messages = len(db)

    # формируем сообщение
    status = f'Статус: OK | ' + \
             f'Время сейчас: {datetime.datetime.now()} | ' + \
             f'Количество пользователей: {number_of_users} | ' + \
             f'Количество сообщений: {number_of_messages}'

    return status



app.run()