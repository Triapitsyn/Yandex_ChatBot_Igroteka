def start(input, id, database):
    import little_fuctions
    mode = little_fuctions.get_mode(id, database)
    game = 'Inever'
    if not mode.startswith(game):
        text, speech, buttons = return_start()
        mode = '{}>main'.format(game)
    elif mode == '{}>main'.format(game) and little_fuctions.isequal(input, 'Правила'):
        text, speech, buttons = return_rules()
        text += '' + '\n\nНе забывайте нажимать на синюю кнопку, чтобы я не мешала вам разгадывать данетку.' * (1 - little_fuctions.get_silent(id, database))
        speech += '' + '\n\nНе забывайте нажимать на синюю кнопку, чтобы я не мешала вам разгадывать данетку.' * (1 - little_fuctions.get_silent(id, database))
        mode = '{}>rules'.format(game)
    elif (mode == '{}>rules'.format(game) or mode == '{}>main'.format(game)) and little_fuctions.isequal(input, 'Начать'):
        text, speech, buttons = return_riddle(0, id, database)
        mode = '{}>riddle>1>0'.format(game)
    elif (mode == '{}>rules'.format(game) or mode == '{}>main'.format(game)) and little_fuctions.isequal(input, 'Играть с разработчиком'):
        text, speech, buttons = return_riddle(1, id, database)
        mode = '{}>riddle>1>1'.format(game)
    elif mode == '{}>rules'.format(game) and little_fuctions.isequal(input, 'Другой вариант игры'):
        text, speech, buttons = return_another_rules()
        mode = '{}>another_rules'.format(game)
    elif mode == '{}>another_rules'.format(game) and little_fuctions.isequal(input, 'Другой вариант игры'):
        text, speech, buttons = return_rules()
        mode = '{}>rules'.format(game)
    elif mode == '{}>another_rules'.format(game) and little_fuctions.isequal(input, 'Варианты действий'):
        import I_have_never_ever_biblio, random
        mediator = I_have_never_ever_biblio.questions[:]
        random.shuffle(mediator)
        text = 'У нас много вариантов, покажу случайные 20\n\n' \
               'Я никогда не...\n' + '\n'.join([ str(i + 1) + ') ' + j for i, j in enumerate(mediator[:20])])
        speech = 'Приятной игр+ы!'
        buttons = ['В начало']
        mode = '{}>another'.format(game)
    elif mode.startswith('{}>riddle>'.format(game)):
        import I_have_never_ever_biblio
        number = int(mode.split('>')[2])
        fl = int(mode.split('>')[3])
        if little_fuctions.isequal(input, 'Дальше'):
            text, speech, buttons = return_riddle(fl, id, database)
            mode = '{}>riddle>{}>{}'.format(game, number, fl)
        else:
            return False
    else:
        return False
    return text, speech, buttons, mode


def return_start():
    import little_fuctions
    text = little_fuctions.ready()
    speech = text
    buttons = ['Начать', 'Играть с разработчиком', 'Правила', 'В начало']
    return text, speech, buttons

def return_rules():
    text='Я буду описывать действия, а каждый из вас должен честно отвечать, делал он его или нет. ' \
         'Эта игра позволяет узнать друг о друге много нового и интересного.'
    speech=text
    buttons=['Начать', 'Играть с разработчиком', 'Другой вариант игры', 'В начало']
    return text, speech, buttons

def return_another_rules():
    text = 'Заранее нужно приготовить фишки, это могут быть спички, монеты, крупная фасоль и так далее. ' \
           'Каждому игроку даётся определённое количество фишек, например 20.\n\n' \
           'Первый игрок говорит: «Я никогда не ела креветки». ' \
           'Те участники, которые ели креветки, отдают одну свою фишку ему. ' \
           'Далее ход переходит к другому участнику и так далее.\n\n' \
           'Задача каждого участника назвать что-то такое, что он никогда не делал, а остальные делали.\n\n' \
           'Игрок, у которого закончились фишки, выбывает. Выигрывает тот, кто набрал больше всех фишек.\n\n' \
           'Главное быть предельно честным, иначе суть игр+ы пропадает.\n\n' \
           'Я могу предложить тебе варианты действий, если ты не знаешь, что назвать.'
    speech = text
    buttons = ['Варианты действий', 'Другой вариант игры', 'В начало']
    return text, speech, buttons

def return_riddle(fl, id, database):
    import I_have_never_ever_biblio
    import random
    import little_fuctions

    used = little_fuctions.get_set(id, database)
    choice = set(I_have_never_ever_biblio.questions).difference(used)
    if not choice:
        choice = random.choice(I_have_never_ever_biblio.questions)
        used = set()
    else:
        choice = random.choice(list(choice))
    used.add(choice)
    little_fuctions.update_set(used, id, database)
    text='{}{}'.format('Я никогда не ' + choice,
                       '\n\n{}'.format(random.choice(['Я делал это', 'Я не делал это']))*fl)
    speech=text

    buttons = ['Дальше', 'В начало']
    return text, speech, buttons