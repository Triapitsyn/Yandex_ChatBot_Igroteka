# coding: utf-8
from __future__ import unicode_literals
import little_fuctions

def message_return(response, user_storage, text, speech, buttons, user_id, database):
    response.set_text(text)
    response.set_tts(speech)
    user_storage["suggests"] = buttons
    buttons, user_storage = little_fuctions.get_suggests(user_storage)
    response.set_buttons(buttons)
    database.update_entries('users_info', user_id, {'last_text': text}, update_type='rewrite')
    database.update_entries('users_info', user_id, {'last_speech': speech}, update_type='rewrite')
    database.update_entries('users_info', user_id, {'last_buttons': '#'.join(buttons)}, update_type='rewrite')
    return response, user_storage

def idk_return(response, user_storage, user_id, database):
    last_text, last_speech, last_buttons = little_fuctions.get_lasts(user_id, database)
    text = 'Я вас не поняла, давайте попробуем еще раз.\n{}'.format(last_text)
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

    if mode.startswith('yesno') or (mode == '' and little_fuctions.isequal(input, 'Данетки')):
        import yes_no_puzzle
        succes = yes_no_puzzle.start(response, user_id, database)
        if succes:
            return message_return(response, user_storage, *succes, user_id, database)
        else:
            return idk_return(response, user_storage, user_id, database)
    elif mode == '' and input == '':
        text = 'Привет, выбери игру'
        speech = text
        buttons = ['Данетки']
        return message_return(response, user_storage, text, speech, buttons, user_id, database)
    else:
        return idk_return(response, user_storage, user_id, database)