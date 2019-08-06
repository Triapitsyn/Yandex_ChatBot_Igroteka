def start(input, id, database):
    import little_fuctions
    mode = little_fuctions.get_mode(id, database)
    game = 'yesno'
    if not mode.startswith(game):
        text, speech, buttons = return_start()
        mode = '{}>main'.format(game)
    elif mode == '{}>main'.format(game) and little_fuctions.isequal(input, 'Правила'):
        text, speech, buttons = return_rules()
        mode = '{}>rules'.format(game)
    elif (mode == '{}>rules'.format(game) or mode == '{}>main'.format(game)) and little_fuctions.isequal(input, 'Начать'):
        text, speech, buttons = return_riddle(1)
        mode = '{}>riddle>1'.format(game)
    elif mode == '{}>rules'.format(game) and little_fuctions.isequal(input, 'Подробнее'):
        text, speech, buttons = return_more_details()
    elif mode.startswith('{}>riddle>'.format(game)):
        import yes_no_puzzle_biblio
        number = int(mode.split('>')[2])
        if little_fuctions.isequal(input, 'Назад'):
            text, speech, buttons = return_riddle(number - 1)
            mode = '{}>riddle>{}'.format(game, number - 1)
        elif little_fuctions.isequal(input, 'Дальше'):
            text, speech, buttons = return_riddle(number + 1)
            mode = '{}>riddle>{}'.format(game, min(number + 1, len(yes_no_puzzle_biblio.riddles)))
        elif little_fuctions.isequal(input.split()[0], 'Пропустить'):
            if input.split()[1].isdigit():
                skip = int(input.split()[1])
            else:
                skip = 1
            text, speech, buttons = return_riddle(number + skip)
            mode = '{}>riddle>{}'.format(game, min(number + skip, len(yes_no_puzzle_biblio.riddles)))
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

def return_rules():
    text='Ведущий описывает странную ситуацию. Угадывающие должны разгадать ситуацию. ' \
         'Они могут задавать ведущему вопросы, на которые можно ответить только «да», «нет», «не имеет значения» или «не корректно»\n\n' \
         'Во время игры вы сможете использовать команду "пропустить" с любым числом, чтобы перейти к более сложным ситуациям.' \
         'Не забывайте нажимать на синюю кнопку, чтобы я не мешала вам разгадывать данетку.'
    speech='Ведущий описывает странную ситуацию. Угадывающие должны разгадать ситуацию. ' \
           'Они могут задавать ведущему вопросы, на которые можно ответить только «да», «нет», «не имеет значения» или «не корректно»\n\n' \
           ' - - - Во время игр+ы вы сможете использовать команду "пропустить" с любым числом, чтобы перейти к более сложным ситуациям.' \
           ' - - - Не забывайте нажимать на синюю кнопку, чтобы я не мешала вам разгадывать данетку.'
    buttons=['Начать', 'Подробнее', 'В начало']
    return text, speech, buttons

def return_more_details():
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
    buttons = ['Начать', 'В начало']
    return text, speech, buttons

def return_riddle(number):
    import yes_no_puzzle_biblio

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