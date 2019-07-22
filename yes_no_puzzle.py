def start(input, id, database):
    import little_fuctions
    mode = little_fuctions.get_mode(id, database)
    if not mode.startswith('yesno'):
        text, speech, buttons = return_start()
        mode = 'yesno>main'
    elif mode == 'yesno>main' and little_fuctions.isequal(input, 'Правила'):
        text, speech, buttons = return_rules()
        mode = 'yesno>rules'
    elif (mode == 'yesno>rules' or mode == 'yesno>main') and little_fuctions.isequal(input, 'Начать'):
        text, speech, buttons = return_riddle(1)
        mode = 'yesno>riddle>1'
    elif mode.startswith('yesno>riddle>'):
        number = int(mode.split('>')[2])
        if little_fuctions.isequal(input, 'Назад'):
            text, speech, buttons = return_riddle(number - 1)
            mode = 'yesno>riddle>{}'.format(number - 1)
        elif little_fuctions.isequal(input, 'Дальше'):
            text, speech, buttons = return_riddle(number + 1)
            mode = 'yesno>riddle>{}'.format(number + 1)
        elif little_fuctions.isequal(input.split()[0], 'Пропустить'):
            if input.split()[1].isdigit():
                skip = int(input.split()[1])
            else:
                skip = 1
            text, speech, buttons = return_riddle(number + skip)
            mode = 'yesno>riddle>{}'.format(number + skip)
        else:
            return False
    else:
        return False
    little_fuctions.update_mode(id, mode, database)
    return text, speech, buttons


def return_start():
    text = 'Для вашего удобства загадки будут представлены по возрастанию сложности.'
    speech = 'Для вашего удобства загадки будут представлены по возрастанию сложности.'
    buttons = ['Начать', 'Правила', 'В начало']
    return text, speech, buttons

def return_rules():
    text='Ведущий описывает странную ситуацию, а угадывающие должны, задавая уточняющие вопросы, выяснить её. При угадывании можно задавать вопросы, но ответом на них могут быть только слова «да», «нет», «не имеет значения» или «не корректно».'
    speech='Ведущий описывает странную ситуацию, а угадывающие должны, задавая уточняющие вопросы, выяснить её. При угадывании можно задавать вопросы, но ответом на них могут быть только слова «да», «нет», «не имеет значения» или «не корректно».'
    buttons=['Начать', 'В начало']
    return text, speech, buttons

def return_riddle(number):
    import yes_no_puzzle_biblio

    warning = False
    if number > len(yes_no_puzzle_biblio.riddles):
        number = len(yes_no_puzzle_biblio.riddles)
        warning = 'Сегодня у нас только {} загадок, показываю последнюю.\n'.format(number)

    text='{}{}\n\nОтвет: {}'.format(str(number)+') ' if not warning else warning,
                                yes_no_puzzle_biblio.riddles[number - 1],
                                yes_no_puzzle_biblio.answers[number - 1])
    speech=yes_no_puzzle_biblio.riddles[number - 1]
    buttons=['Дальше', 'Назад', 'В начало']
    return text, speech, buttons