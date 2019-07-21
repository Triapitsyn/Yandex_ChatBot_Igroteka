def get_response():
    pass

def return_answer(buttons, text, speech, idk = False):
    if idk:
        #НЕ ОБНОВЛЯТЬ ПОСЛЕДНИЕ ОТВЕТЫ
        pass
    pass

def idk(id, database):
    import little_fuctions
    last_text, last_speech, last_buttons = little_fuctions.get_lasts(id, database)
    text = 'Я вас не поняла, давайте попробуем еще раз.\n{}'.format(last_text)
    speech = 'Я вас не поняла, давайте попробуем еще раз.'.format(last_speech)
    buttons = last_buttons
    return_answer(buttons=buttons,
                  text=text,
                  speech=speech,
                  idk = True)