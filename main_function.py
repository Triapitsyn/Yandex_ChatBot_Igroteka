# coding: utf-8
from __future__ import unicode_literals
import json
import little_fuctions


aliceAnswers = read_answers_data("data/answers_dict_example")

def message_return(response, user_storage, text, speech, buttons):
    response.set_text(message)
    response.set_tts(message)
    buttons, user_storage = little_fuctions.get_suggests(user_storage)
    response.set_buttons(buttons)
    return response, user_storage


def handle_dialog(request, response, user_storage, database):

    if not database.get_entry("users_info", ['new'], {'request_id': request.user_id}):
        database.add_entries("users_info", {"request_id": request.user_id})
    if not user_storage:
        user_storage = {"suggests": []}

    input = request.command
    isfirsttime = request.is_new_session
    if isfirsttime:
        mode = ''
        update_mode(request.user_id, mode, database)
    else:
        mode = database.get_entry("users_info", ['mode'], {'request_id': request.user_id})[0][0]
    last_text, last_speech, last_buttons = little_fuctions.get_lasts(id, database)

    import alice_interaction
    mode = little_fuctions.get_mode(id, database)
    if mode.startswith('yesno') or (mode == '' and little_fuctions.isequal(response, 'Данетки')):
        import yes_no_puzzle
        yes_no_puzzle.start(response, id, database)
    else:
        alice_interaction.idk(id, database)