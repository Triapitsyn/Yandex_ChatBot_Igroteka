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
    text = 'Начнем?'
    speech = text
    buttons = ['Начать', 'Правила', 'В начало']
    return text, speech, buttons

def return_rules():
    text='Ведущий описывает странную ситуацию, а угадывающие должны выяснить её, ' \
         'задавая ведущему вопросы, на которые можно ответить только «да», «нет», «не имеет значения» или «не корректно»\n\n' \
         'Вы можете использовать команду "пропустить" с любым числом, чтобы перейти к более сложным ситуациям.'
    speech=text
    buttons=['Начать', 'В начало']
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