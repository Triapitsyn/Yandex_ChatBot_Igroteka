# coding: utf-8
from __future__ import unicode_literals
import json
import little_fuctions


aliceAnswers = read_answers_data("data/answers_dict_example")

def message_return(response, user_storage, message, button, database, request, mode):
    # ща будет магия
    response.set_text(message)
    response.set_tts(message)
    buttons, user_storage = little_fuctions.get_suggests(user_storage)
    print(buttons)
    response.set_buttons(button)
    return response, user_storage


def handle_dialog(request, response, user_storage, database, morph):
    import alice_interaction
    mode = little_fuctions.get_mode(id, database)
    if mode.startswith('yesno') or (mode == '' and little_fuctions.isequal(response, 'Данетки')):
        import yes_no_puzzle
        yes_no_puzzle.start(response, id, database)
    else:
        alice_interaction.idk(id, database)