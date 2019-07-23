# coding: utf-8
from __future__ import unicode_literals
import little_fuctions

def message_return(response, user_storage, text, speech, buttons, mode, user_id, database):
    little_fuctions.update_mode(user_id, mode, database)
    response.set_text(text)
    response.set_tts(speech)
    user_storage["suggests"] = buttons
    database.update_entries('users_info', user_id, {'last_buttons': '#'.join(buttons)}, update_type='rewrite')
    buttons, user_storage = little_fuctions.get_suggests(user_storage)
    response.set_buttons(buttons)
    database.update_entries('users_info', user_id, {'last_text': text}, update_type='rewrite')
    database.update_entries('users_info', user_id, {'last_speech': speech}, update_type='rewrite')
    return response, user_storage

def idk_return(response, user_storage, user_id, database):
    last_text, last_speech, last_buttons = little_fuctions.get_lasts(user_id, database)
    text = 'Я вас не поняла, давайте попробуем еще раз.\n\n{}'.format(last_text)
    speech = 'Я вас не поняла, давайте попробуем еще раз.'.format(last_speech)
    buttons = last_buttons
    response.set_text(text)
    response.set_tts(speech)
    user_storage["suggests"] = buttons
    buttons, user_storage = little_fuctions.get_suggests(user_storage)
    response.set_buttons(buttons)
    return response, user_storage


def handle_dialog(request, response, user_storage, database):

    if not database.get_entry("users_info", ['new'], {'request_id': request.user_id}):
        database.add_entries("users_info", {"request_id": request.user_id})
    if not user_storage:
        user_storage = {"suggests": []}

    input = request.command
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

    games = ['Данетки', 'Я никогда не']

    if little_fuctions.isequal(input, 'Помощь'):
        text = 'В этом навыке все просто! Выбери игру и скажи "начать". ' \
               'Правила ты сможешь посмотреть в меню игры. Желаю хорошо провести время!'
        speech = text
        buttons = games[:]
        mode = 'start'
        return message_return(response, user_storage, text, speech, buttons, mode, user_id, database)

    elif mode.startswith('yesno') or (mode == 'start' and little_fuctions.isequal(input, 'Данетки')):
        import yes_no_puzzle
        succes = yes_no_puzzle.start(input, user_id, database)
        if succes:
            return message_return(response, user_storage, *succes, user_id, database)
        else:
            return idk_return(response, user_storage, user_id, database)
    elif mode.startswith('Inever') or (mode == 'start' and little_fuctions.isequal(input, 'Я никогда не')):
        import I_have_never_ever
        succes = I_have_never_ever.start(input, user_id, database)
        if succes:
            return message_return(response, user_storage, *succes, user_id, database)
        else:
            return idk_return(response, user_storage, user_id, database)
    elif mode == '' and input == '':
        text = little_fuctions.hello()
        speech = text
        buttons = games[:]
        mode = 'start'
        return message_return(response, user_storage, text, speech, buttons, mode, user_id, database)
    else:
        return idk_return(response, user_storage, user_id, database)