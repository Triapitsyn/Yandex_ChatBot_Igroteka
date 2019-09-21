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
    elif mode.startswith('{}>main'.format(game)) and little_fuctions.isequal(input, 'Начать'):
        text, speech, buttons = return_difficulties()
        mode = '{}>difficulty'.format(game)
    elif mode.startswith('{}>rules'.format(game)) and little_fuctions.isequal(input, 'Начать'):
        text, speech, buttons = return_difficulties()
        mode = '{}>difficulty'.format(game)
    elif mode.startswith('{}>diff>'.format(game)) and little_fuctions.isequal(input, 'Поменять сложность'):
        text, speech, buttons = return_difficulties()
        mode = '{}>difficulty'.format(game)
    elif mode == '{}>difficulty'.format(game):
        if little_fuctions.isequal(input, 'Легкие'):
            mode = '{}>diff>easy'.format(game)
            text, speech, buttons = return_riddle('easy', id, database)
        elif little_fuctions.isequal(input, 'Средние'):
            mode = '{}>diff>medium'.format(game)
            text, speech, buttons = return_riddle('medium', id, database)
        elif little_fuctions.isequal(input, 'Сложные'):
            mode = '{}>diff>pro'.format(game)
            text, speech, buttons = return_riddle('pro', id, database)
        elif little_fuctions.isequal(input, 'Невозможные'):
            mode = '{}>diff>unreal'.format(game)
            text, speech, buttons = return_riddle('unreal', id, database)
        else:
            return False
    elif mode.startswith('{}>diff>'.format(game)):
        difficulty = mode.split('>')[2]
        if little_fuctions.isequal(input, 'Дальше'):
            text, speech, buttons = return_riddle(difficulty, id, database)
        else:
            return False
    else:
        return False
    return text, speech, buttons, mode


def return_start():
    import little_fuctions
    text = little_fuctions.ready()
    speech = text
    buttons = ['Легкие', 'Средние', 'Сложные', 'Невозможные', 'В начало']
    return text, speech, buttons


def return_difficulties():
    text = 'Выберите уровень сложности слов'
    speech = text
    buttons = ['Легкие', 'Средние', 'Сложные', 'Невозможные', 'В начало']
    return text, speech, buttons


def return_rules():
    text='Ваша задача - без слов и указаний на реальные предметы объяснить твоим друзьям ' \
         'значение сл+ова, которое я тебе покажу. ' \
         'Кто из них отгадает - тот и объясняет следующее слово.\n\n' \
         'Например, вы можете указать на запястье, и все поймут, что вы показываете часы, ' \
         'но вы не можете показать на настенные часы.'
    speech=text
    buttons=['Начать', 'В начало']
    return text, speech, buttons


def return_riddle(difficulty, id, database):
    import croco_biblio, random, little_fuctions

    used = little_fuctions.get_set(id, database)
    mediator = set(croco_biblio.words[difficulty]).difference(used)
    if not mediator:
        little_fuctions.update_set(set(), id, database)
        mediator = set(croco_biblio.words[difficulty])
        used = set()
    text=random.choice(list(mediator))
    used.add(text)
    little_fuctions.update_set(used, id, database)
    speech=random.choice(croco_biblio.phrase[difficulty]) if random.randint(0, 5) < 4 else ' '
    buttons=['Дальше', 'Поменять сложность', 'В начало']
    return text, speech, buttons
