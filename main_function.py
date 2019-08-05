# coding: utf-8
from __future__ import unicode_literals
import little_fuctions
from card_template import *

def message_return(response, user_storage, text, speech, buttons, mode, user_id, database):
    little_fuctions.update_mode(user_id, mode, database)
    text = text.replace('+', '')
    response.set_text(text)
    response.set_tts(speech)
    user_storage["suggests"] = buttons
    database.update_entries('users_info', user_id, {'last_buttons': '#'.join(buttons)}, update_type='rewrite')
    buttons, user_storage = little_fuctions.get_suggests(user_storage)
    if mode == "":
        user_storage["card"] = start_card(little_fuctions.get_color(user_id, database))
        user_storage["card"]["header"]["text"] = text
        response.set_card(user_storage["card"])
    elif mode == "yesno>main":
        user_storage["card"] = yesno_card(little_fuctions.get_color(user_id, database))
        user_storage["card"]["header"]["text"] = text
        response.set_card(user_storage["card"])
    elif mode == "croco>main":
        user_storage["card"] = croco_card(little_fuctions.get_color(user_id, database))
        user_storage["card"]["header"]["text"] = text
        response.set_card(user_storage["card"])
    elif mode == "Inever>main":
        user_storage["card"] = inever_card(little_fuctions.get_color(user_id, database))
        user_storage["card"]["header"]["text"] = text
        response.set_card(user_storage["card"])
    elif mode == "croco>difficulty":
        user_storage["card"] = croco_diff_card(little_fuctions.get_color(user_id, database))
        user_storage["card"]["header"]["text"] = text
        response.set_card(user_storage["card"])
    else:
        response.set_buttons(buttons)
    database.update_entries('users_info', user_id, {'last_text': text}, update_type='rewrite')
    database.update_entries('users_info', user_id, {'last_speech': speech}, update_type='rewrite')
    return response, user_storage

def idk_return(response, user_storage, user_id, database, mode, again = 0):
    last_text, last_speech, last_buttons = little_fuctions.get_lasts(user_id, database)
    if again:
        #text = str(last_text) + ' '
        #speech = str(last_speech) + ' '
        text = 'Я вас не поняла, давайте попробуем еще раз.\n\n{}'.format(last_text)
        speech = 'Я вас не поняла, давайте попробуем еще раз.\n\n{}'.format(last_speech)
        print('!!!!!!!!!', 'ТЕКСТ: {}'.format(text), 'СПИЧ: {}'.format(speech), '!!!!!!!!', sep = '\n')
    else:
        text = 'Я вас не поняла, давайте попробуем еще раз.\n\n{}'.format(last_text)
        speech = 'Я вас не поняла, давайте попробуем еще раз.\n\n{}'.format(last_speech)
    buttons = last_buttons
    text = text.replace('+', '')
    response.set_text(text)
    response.set_tts(speech)
    user_storage["suggests"] = buttons
    buttons, user_storage = little_fuctions.get_suggests(user_storage)
    if mode == "":
        user_storage["card"] = start_card(little_fuctions.get_color(user_id, database))
        user_storage["card"]["header"]["text"] = text
        response.set_card(user_storage["card"])
    elif mode == "yesno>main":
        user_storage["card"] = yesno_card(little_fuctions.get_color(user_id, database))
        response.set_card(user_storage["card"])
    elif mode == "croco>main":
        user_storage["card"] = croco_card(little_fuctions.get_color(user_id, database))
        user_storage["card"]["header"]["text"] = text
        response.set_card(user_storage["card"])
    elif mode == "Inever>main":
        user_storage["card"] = inever_card(little_fuctions.get_color(user_id, database))
        user_storage["card"]["header"]["text"] = text
        response.set_card(user_storage["card"])
    elif mode == "croco>difficulty":
        user_storage["card"] = croco_diff_card(little_fuctions.get_color(user_id, database))
        user_storage["card"]["header"]["text"] = text
        response.set_card(user_storage["card"])
    else:
        response.set_buttons(buttons)
    return response, user_storage


def handle_dialog(request, response, user_storage, database):
    if not database.get_entry("users_info", ['new'], {'request_id': request.user_id}):
        database.add_entries("users_info", {"request_id": request.user_id})
    if not user_storage:
        user_storage = {"suggests": []}
    if "command" in request.request.keys():
        input = request.command
    else:
        input = request.payload
    user_id = request.user_id
    is_first_time = request.is_new_session
    if is_first_time:
        mode = ''
        little_fuctions.update_mode(user_id, mode, database)
    else:
        mode = little_fuctions.get_mode(user_id, database)

    if little_fuctions.isequal(input, 'В начало'):
        mode = ''
        input = ''

    games = ['Данетки', 'Я никогда не', 'Крокодил']

    if little_fuctions.isequal(input, 'Помощь'):
        text = 'В этом навыке все просто! Выбери игру и скажи "начать". ' \
               'Правила ты сможешь посмотреть в меню игры. Желаю хорошо провести время!'
        speech = text
        buttons = games[:]
        mode = ''
        return message_return(response, user_storage, text, speech, buttons, mode, user_id, database)
    elif little_fuctions.isequal(input, 'Еще раз'):
        idk_return(response, user_storage, user_id, database, mode, 1)
    elif mode.startswith('yesno') or (mode == '' and little_fuctions.isequal(input, 'Данетки')):
        import yes_no_puzzle
        succes = yes_no_puzzle.start(input, user_id, database)
        if succes:
            return message_return(response, user_storage, *succes, user_id, database)
        else:
            return idk_return(response, user_storage, user_id, database, mode, 0)
    elif mode.startswith('Inever') or (mode == '' and little_fuctions.isequal(input, 'Я никогда не')):
        import I_have_never_ever
        succes = I_have_never_ever.start(input, user_id, database)
        if succes:
            return message_return(response, user_storage, *succes, user_id, database)
        else:
            return idk_return(response, user_storage, user_id, database, mode, 0)
    elif mode.startswith('croco') or (mode == '' and little_fuctions.isequal(input, 'Крокодил')):
        import croco
        succes = croco.start(input, user_id, database)
        if succes:
            return message_return(response, user_storage, *succes, user_id, database)
        else:
            return idk_return(response, user_storage, user_id, database, mode, 0)
    elif mode == '' and little_fuctions.isequal(input, 'Сменить цвета'):
        little_fuctions.update_color(little_fuctions.get_color(user_id, database) + 1, user_id, database)
        if little_fuctions.get_color(user_id, database) % colors == 2:
            little_fuctions.update_color(little_fuctions.get_color(user_id, database) + 1, user_id, database)
        text = little_fuctions.hello()
        speech = text
        mode = ''
        buttons = []
        return message_return(response, user_storage, text, speech, buttons, mode, user_id, database)
    elif mode == '':
        text = little_fuctions.hello()
        speech = text
        mode = ''
        buttons = []
        little_fuctions.update_set(set(), user_id, database)
        return message_return(response, user_storage, text, speech, buttons, mode, user_id, database)
    else:
        return idk_return(response, user_storage, user_id, database, mode, 0)
