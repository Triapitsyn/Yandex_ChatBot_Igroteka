def start(text, id, database):
    import little_fuctions
    mode = little_fuctions.get_mode(id, database)
    if not mode.startswith('yesno'):
        return_start()
        mode = 'yesno>main'
    elif mode == 'yesno>main' and little_fuctions.isequal(text, 'Правила'):
        return_rules()
        mode = 'yesno>rules'
    elif mode == 'yesno>rules' and little_fuctions.isequal(text, 'Начать'):
        return_riddle(1)
        mode = 'yesno>riddle>1'
    elif mode.startswith('yesno>riddle>'):
        number = int(mode.split('>')[2])
        if little_fuctions.isequal(text, 'Назад'):
            return_riddle(number - 1)
            mode = 'yesno>riddle>{}'.format(number - 1)
        elif little_fuctions.isequal(text, 'Дальше'):
            return_riddle(number + 1)
            mode = 'yesno>riddle>{}'.format(number + 1)
        elif little_fuctions.isequal(reponse.split()[0], 'Пропустить'):
            if text.split[1].isdigit():
                skip = int(text.split[1])
            else:
                skip = 1
            return_riddle(number + skip)
            mode = 'yesno>riddle>{}'.format(number + skip)
    else:
        import alice_interaction
        alice_interaction.idk(id, database)
    little_fuctions.update_mode(id, mode, database)
    pass


def return_start():
    import alice_interaction
    alice_interaction.return_answer(buttons=['Начать', 'Правила', 'В начало'],
                                    text='Для вашего удобства загадки будут представлены по возрастанию сложности.',
                                    speech='Для вашего удобства загадки будут представлены по возрастанию сложности.')
    return

def return_rules():
    import alice_interaction
    alice_interaction.return_answer(buttons=['Начать', 'В начало'],
                                    text='Ведущий описывает странную ситуацию, а угадывающие должны, задавая уточняющие вопросы, выяснить её. При угадывании можно задавать вопросы, но ответом на них могут быть только слова «да», «нет», «не имеет значения» или «не корректно».',
                                    speech='Ведущий описывает странную ситуацию, а угадывающие должны, задавая уточняющие вопросы, выяснить её. При угадывании можно задавать вопросы, но ответом на них могут быть только слова «да», «нет», «не имеет значения» или «не корректно».')
    return

def return_riddle(number):
    import alice_interaction
    import yes_no_puzzle_biblio
    warning = False
    if number > len(yes_no_puzzle_biblio.riddles):
        number = len(yes_no_puzzle_biblio.riddles)
        warning = 'Сегодня у нас только {} загадок, показываю последнюю.\n'
    alice_interaction.return_answer(buttons=['Дальше', 'Назад', 'В начало'],
                                    text='{}{}\nОтвет: {}'.format(str(number)+') ' if not warning else warning,
                                                                    yes_no_puzzle_biblio.riddles[number],
                                                                    yes_no_puzzle_biblio.answers[number]),
                                    speech=yes_no_puzzle_biblio.riddles[number])
    return