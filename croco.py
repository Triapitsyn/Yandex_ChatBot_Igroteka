def start(input, id, database):
    import little_fuctions
    mode = little_fuctions.get_mode(id, database)
    game = 'croco'
    if not mode.startswith(game):
        text, speech, buttons = return_start()
        mode = '{}>main'.format(game)
    elif mode == '{}>main'.format(game) and little_fuctions.isequal(input, 'Правила'):
        text, speech, buttons = return_rules()
        mode = '{}>rules'.format(game)
    elif (mode == '{}>rules'.format(game) or mode == '{}>main'.format(game)) and little_fuctions.isequal(input, 'Начать'):
        text, speech, buttons = return_difficulties()
        mode = '{}>difficulties'.format(game)
    elif mode.startswith('{}>diff>'.format(game)) and little_fuctions.isequal(input, 'Поменять сложность'):
        text, speech, buttons = return_difficulties()
        mode = '{}>difficulties'.format(game)
    elif mode == '{}>difficulties'.format(game):
        if little_fuctions.isequal(input, 'Легкие'):
            mode = '{}>diff>easy'.format(game)
            text, speech, buttons = return_riddle('easy')
        elif little_fuctions.isequal(input, 'Нормальные'):
            mode = '{}>diff>medium'.format(game)
            text, speech, buttons = return_riddle('medium')
        elif little_fuctions.isequal(input, 'Сложные'):
            mode = '{}>diff>pro'.format(game)
            text, speech, buttons = return_riddle('pro')
        elif little_fuctions.isequal(input, 'Невозможные'):
            mode = '{}>diff>unreal'.format(game)
            text, speech, buttons = return_riddle('unreal')
        else:
            return False
    elif mode.startswith('{}>diff>'.format(game)):
        difficulty = mode.split('>')[2]
        if little_fuctions.isequal(input, 'Дальше'):
            text, speech, buttons = return_riddle(difficulty)
        else:
            return False
    else:
        return False
    return text, speech, buttons, mode


def return_start():
    text = 'Приятной игры!'
    speech = text
    buttons = ['Начать', 'Правила', 'В начало']
    return text, speech, buttons

def return_difficulties():
    text = 'Выберите уровень сложности слов'
    speech = text
    buttons = ['Легкие', 'Нормальные', 'Сложные', 'Невозможные', 'В начало']
    return text, speech, buttons

def return_rules():
    text='Ваша задача - без слов объяснить вашим друзьям значение предложенного слова.'
    speech=text
    buttons=['Начать', 'В начало']
    return text, speech, buttons

def return_riddle(difficulty):
    import croco_biblio, random

    text=random.choice(croco_biblio.words[difficulty])
    speech=random.choice(croco_biblio.phrase[difficulty])
    buttons=['Дальше', 'Поменять сложность', 'В начало']
    return text, speech, buttons