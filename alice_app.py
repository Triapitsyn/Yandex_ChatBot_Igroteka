# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с логами.
import logging

# Импортируем модуль для работы с API Алисы
from alice_sdk import AliceRequest, AliceResponse

# Импортируем модуль с логикой игры
from main_function import *

# Импортируем модуль работы с базами данных
import postgresql_database

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
app = Flask(__name__)


# Хранилище данных о сессиях.
session_storage = {}


logging.basicConfig(level=logging.DEBUG)

def init_database(host, user, password, dbname):
    psdb = postgresql_database.DatabaseManager(host, user, password, dbname)
    psdb.create_table("users_info",
                      {'user_id': "serial primary", "request_id": "str NOT NULL UNIQUE",
                       "mode": "str DEFAULT ''", "new": "str DEFAULT 'sample_text'",
                       "last_text": "str DEFAULT ''", "last_speech": "str DEFAULT ''",
                       "last_buttons": "str DEFAULT ''", "word_set":  "str DEFAULT ''",
                       "color": "int DEFAULT 0", "silent": "int DEFAULT 0", "last_riddle": "int DEFAULT 0"
                       })
    # psdb.drop_table("users_info")
    return psdb


@app.route("/life_simulation/ping")
def mainn():
    return "pong"


# Задаем параметры приложения Flask.
@app.route("/alice_hackaton/", methods=['POST'])
def main():
    database = init_database(host='localhost', user='postgr', password='1488', dbname='new_game')
    alice_request = AliceRequest(request.json)
    logging.info('Request: {}'.format(alice_request))
    alice_response = AliceResponse(alice_request)

    user_id = alice_request.user_id
    alice_response, session_storage[user_id] = handle_dialog(
        alice_request, alice_response, session_storage.get(user_id), database
    )

    logging.info('Response: {}'.format(alice_response))
    print()

    return alice_response.dumps()


@app.route("/word_coach/", methods=['POST'])
def mainnn():
    from other import main_function
    from other import alice_app
    import pymorphy2
    database = alice_app.init_database(host='localhost', user='postgr', password='1488', dbname='word_coach')
    alice_request = AliceRequest(request.json)
    morph = pymorphy2.MorphAnalyzer()
    logging.info('Request: {}'.format(alice_request))
    alice_response = AliceResponse(alice_request)

    user_id = alice_request.user_id
    print(user_id)
    print(session_storage.get(user_id))
    print(len(session_storage))
    alice_response, session_storage[user_id] = main_function.handle_dialog(
        alice_request, alice_response, session_storage.get(user_id), database, morph
    )

    logging.info('Response: {}'.format(alice_response))
    print()

    return alice_response.dumps()


@app.route("/zavalinka/", methods=['POST'])
def zavalinka():
    from other2 import database_module
    from other2 import zavalinka
    import pymorphy2
    from other2.alice_sdk import AliceRequest, AliceResponse
    morph = pymorphy2.MorphAnalyzer()
    database = database_module.DatabaseManager()
    # Функция получает тело запроса и возвращает ответ.
    alice_request = AliceRequest(request.json)
    logging.info('Request: {}'.format(alice_request))

    alice_response = AliceResponse(alice_request)

    user_id = alice_request.user_id
    print(user_id)
    print(session_storage.get(user_id))
    print(len(session_storage))
    alice_response, session_storage[user_id] = zavalinka.handle_dialog(
        alice_request, alice_response, session_storage.get(user_id), database, morph.parse('очко')[0]
    )

    logging.info('Response: {}'.format(alice_response))

    return alice_response.dumps()

if __name__ == '__main__':
    app.run()
