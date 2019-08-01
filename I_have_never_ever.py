def start(input, id, database):
    import little_fuctions
    mode = little_fuctions.get_mode(id, database)
    game = 'Inever'
    if not mode.startswith(game):
        text, speech, buttons = return_start()
        mode = '{}>main'.format(game)
    elif mode == '{}>main'.format(game) and little_fuctions.isequal(input, 'Правила'):
        text, speech, buttons = return_rules()
        mode = '{}>rules'.format(game)
    elif (mode == '{}>rules'.format(game) or mode == '{}>main'.format(game)) and little_fuctions.isequal(input, 'Начать'):
        text, speech, buttons = return_riddle(1, 0)
        mode = '{}>riddle>1>0'.format(game)
    elif (mode == '{}>rules'.format(game) or mode == '{}>main'.format(game)) and little_fuctions.isequal(input, 'Играть с разработчиком'):
        text, speech, buttons = return_riddle(1, 1)
        mode = '{}>riddle>1>1'.format(game)
    elif mode == '{}>rules'.format(game) and little_fuctions.isequal(input, 'Другой вариант игры'):
        text, speech, buttons = return_another_rules()
        mode = '{}>another_rules'.format(game)
    elif mode == '{}>another_rules'.format(game) and little_fuctions.isequal(input, 'Другой вариант игры'):
        text, speech, buttons = return_rules()
        mode = '{}>rules'.format(game)
    elif mode == '{}>another_rules'.format(game) and little_fuctions.isequal(input, 'Варианты действий'):
        import I_have_never_ever_biblio, random
        text = 'У нас много вариантов, покажу случайные 20\n\n' \
               'Я никогда не...\n' + '\n'.join([ str(i + 1) + ') ' + j for i, j in enumerate(random.shuffle(I_have_never_ever_biblio.questions)[:20])])
        speech = 'Приятной игры!'
        buttons = ['В начало']
        mode = '{}>another'.format(game)
    elif mode.startswith('{}>riddle>'.format(game)):
        import I_have_never_ever_biblio
        number = int(mode.split('>')[2])
        fl = int(mode.split('>')[3])
        if little_fuctions.isequal(input, 'Назад'):
            text, speech, buttons = return_riddle(number - 1, fl)
            mode = '{}>riddle>{}>{}'.format(game, number - 1, fl)
        elif little_fuctions.isequal(input, 'Дальше'):
            text, speech, buttons = return_riddle(number + 1, fl)
            mode = '{}>riddle>{}>{}'.format(game, min(number + 1, len(I_have_never_ever_biblio.questions)), fl)
        elif little_fuctions.isequal(input.split()[0], 'Пропустить'):
            if input.split()[1].isdigit():
                skip = int(input.split()[1])
            else:
                skip = 1
            text, speech, buttons = return_riddle(number + skip, fl)
            mode = '{}>riddle>{}>{}'.format(game, min(number + skip, len(I_have_never_ever_biblio.questions)), fl)
        else:
            return False
    else:
        return False
    return text, speech, buttons, mode


def return_start():
    text = ' '
    speech = text
    buttons = ['Начать', 'Играть с разработчиком', 'Правила', 'В начало']
    return text, speech, buttons

def return_rules():
    text='Я буду описывать действия, а каждый из вас должен честно отвечать делал он его или нет. ' \
         'Эта игра позволяет узнать друг о друге много нового и интересного.\n\n' \
         'Вы можете использовать команду "пропустить" с любым числом.'
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
           'Главное быть предельно честным, иначе суть игры пропадает.\n\n' \
           'Я могу предложить тебе варианты действий, если ты не знаешь, что назвать.'
    speech = text
    buttons = ['Варианты действий', 'Другой вариант игры', 'В начало']
    return text, speech, buttons

def return_riddle(number, fl):
    import I_have_never_ever_biblio
    import random

    warning = ''
    if number > len(I_have_never_ever_biblio.questions):
        number = len(I_have_never_ever_biblio.questions)
        warning = 'Сегодня у нас только {} вопросов, показываю последний.\n\n'.format(number)

    text='{}{}{}'.format(str(number)+') ' if not warning else warning,
                         'Я никогда не ' + I_have_never_ever_biblio.questions[number - 1],
                         '\n\nМой ответ - {}'.format(random.choice(['Я делал это', 'Я не делал это']))*fl)
    speech='{}{}{}'.format(warning,
                           'Я никогда не ' + I_have_never_ever_biblio.questions[number - 1],
                           '\n\nМой ответ - {}'.format(random.choice(['Я делал это', 'Я не делал это']))*fl)

    if number == 1:
        buttons = ['Дальше', 'Пропустить 10', 'В начало']
    else:
        buttons=['Дальше', 'Назад', 'Пропустить 10', 'В начало']
    return text, speech, buttons