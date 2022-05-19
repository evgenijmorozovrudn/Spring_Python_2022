import requests

# Стартовое сообщение
print('Приветствуем в нашем мессенджере!\n/help - помощь\n/change_user - изменить имя пользователя')
name = input('Введите имя: ')
while True:
    text = input('Введите сообщение: ')

    # проверка на ввод команд
    if text == '/help':
        print('Как пользоваться мессенджером: ...')

    elif text == '/change_user':
        name = input('Введите имя: ')

    else:
        # Замена пустой строки на None
        if name == '':
            name = None

        response = requests.post('http://127.0.0.1:5000/send',
                                json={
                                    'name': name,
                                    'text': text
                                }
                                )
