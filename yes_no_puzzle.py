def start(input, id, database):
    import little_fuctions
    mode = little_fuctions.get_mode(id, database)
    game = 'yesno'
    if not mode.startswith(game):
        text, speech, buttons = return_start()
        mode = '{}>main'.format(game)
    elif mode == '{}>main'.format(game) and little_fuctions.isequal(input, 'Правила'):
        text, speech, buttons = return_rules(id, database)
        text += '' + '\n\nНе забывайте нажимать на синюю кнопку, чтобы я не мешала вам разгадывать данетку.' * (1 - little_fuctions.get_silent(id, database))
        speech += '' + '\n\n - - - Не забывайте нажимать на синюю кнопку, чтобы я не мешала вам разгадывать данетку.' * (1 - little_fuctions.get_silent(id, database))
        mode = '{}>rules'.format(game)
    elif (mode == '{}>rules'.format(game) or mode == '{}>main'.format(game)) and little_fuctions.isequal(input, 'Начать заново'):
        text, speech, buttons = return_riddle(1)
        mode = '{}>riddle>1'.format(game)
        little_fuctions.update_last_riddle(0, id, database)
    elif (mode == '{}>rules'.format(game) or mode == '{}>main'.format(game)) and little_fuctions.isequal(input, 'Продолжить'):
        last_riddle = little_fuctions.get_last_riddle(id, database)
        text, speech, buttons = return_riddle(last_riddle)
        mode = '{}>riddle>{}'.format(game, last_riddle)
    elif mode == '{}>rules'.format(game) and little_fuctions.isequal(input, 'Подробнее'):
        text, speech, buttons = return_more_details(id, database)
    elif mode.startswith('{}>riddle>'.format(game)):
        import yes_no_puzzle_biblio
        number = int(mode.split('>')[2])
        if little_fuctions.isequal(input, 'Назад'):
            text, speech, buttons = return_riddle(number - 1)
            mode = '{}>riddle>{}'.format(game, number - 1)
            little_fuctions.update_last_riddle(number - 2, id, database)
        elif little_fuctions.isequal(input, 'Дальше'):
            num = min(number + 1, len(yes_no_puzzle_biblio.riddles))
            text, speech, buttons = return_riddle(number + 1)
            mode = '{}>riddle>{}'.format(game, num - 1)
            little_fuctions.update_last_riddle(num, id, database)
        elif little_fuctions.isequal(input.split()[0], 'Пропустить'):
            if input.split()[1].isdigit():
                skip = int(input.split()[1])
            else:
                skip = 1
            num = min(number + skip, len(yes_no_puzzle_biblio.riddles))
            text, speech, buttons = return_riddle(number + skip)
            mode = '{}>riddle>{}'.format(game, num)
            little_fuctions.update_last_riddle(num, id, database)
        else:
            return False
    else:
        return False
    return text, speech, buttons, mode


def return_start():
    import little_fuctions
    text = little_fuctions.ready()
    speech = text
    buttons = ['Начать', 'Правила', 'В начало']
    return text, speech, buttons

def return_rules(user_id, database):
    import little_fuctions
    text='Ведущий описывает странную ситуацию. Угадывающие должны разгадать ситуацию. ' \
         'Они могут задавать ведущему вопросы, на которые можно ответить только «да», «нет», «не имеет значения» или «не корректно»\n\n' \
         'Во время игры вы сможете использовать команду "пропустить" с любым числом, чтобы перейти к более сложным ситуациям.'
    speech='Ведущий описывает странную ситуацию. Угадывающие должны разгадать ситуацию. ' \
           'Они могут задавать ведущему вопросы, на которые можно ответить только «да», «нет», «не имеет значения» или «не корректно»\n\n' \
           ' - - - Во время игр+ы вы сможете использовать команду "пропустить" с любым числом, чтобы перейти к более сложным ситуациям.'
    if little_fuctions.get_last_riddle(user_id, database):
        buttons = ['Начать заново', 'Продолжить', 'Подробнее', 'В начало']
    else:
        buttons=['Начать', 'Подробнее', 'В начало']
    return text, speech, buttons

def return_more_details(user_id, database):
    import little_fuctions
    text = 'Телефон находится в руках у ведущего. На экране ведущий видит ситуацию и ответ к ней. Например: \n\n' \
           'Человек на вокзале покупает в кассе билет, ему говорят „Поезд через 13 минут“. Человек смотрит на билет и выбрасывает. Почему?\n\n' \
           'Ответ: он купил билет, чтобы узнать время.\n\n' \
           'Друзья ведущего слышат только саму ситуацию и должны задавать ведущему вопросы, чтобы узнать ответ. ' \
           'Задавать можно только вопросы, ответы на которые "да" или "нет". Помимо этого ведущий может ответить "не имеет значения" или "не корректно".'
    speech = 'Телефон находится в руках у ведущего. На экране ведущий видит ситуацию и ответ к ней. Например: \n\n - - -' \
           'Человек на вокзале покупает в кассе билет, ему говорят „Поезд через 13 минут“. Человек смотрит на билет и выбрасывает. - Почему?\n\n' \
           'Ответ: он купил билет, чтобы узнать время.\n\n - - - ' \
           'Друзья ведущего слышат только саму ситуацию и должны задавать ведущему вопросы, чтобы узнать ответ. ' \
           'Задавать можно только вопросы, ответы на которые "да" - или "нет". Помимо этого ведущий может ответить "не имеет значения" - - - или "не корректно".'
    if little_fuctions.get_last_riddle(user_id, database):
        buttons = ['Начать заново', 'Продолжить', 'В начало']
    else:
        buttons = ['Начать', 'В начало']
    return text, speech, buttons

def return_riddle(number):
    import yes_no_puzzle_biblio, little_fuctions

    warning = False
    if number > len(yes_no_puzzle_biblio.riddles):
        number = len(yes_no_puzzle_biblio.riddles)
        warning = 'Сегодня у нас только {} загадок, показываю последнюю.\n\n'.format(number)

    text='{}{}\n\nОтвет: {}'.format(str(number)+') ' if not warning else warning,
                                yes_no_puzzle_biblio.riddles[number - 1],
                                yes_no_puzzle_biblio.answers[number - 1])
    speech=yes_no_puzzle_biblio.riddles[number - 1]
    if number == 1:
        buttons = ['Дальше', 'Пропустить 10', 'В начало']
    else:
        buttons=['Дальше', 'Назад', 'Пропустить 10', 'В начало']
    return text, speech, buttons