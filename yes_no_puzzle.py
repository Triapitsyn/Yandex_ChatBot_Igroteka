def start(response, id):
    import little_fuctions
    mode = little_fuctions.get_mode(id)
    if not mode.startswith('yesno'):
        return_start()
        mode = 'yesno>main'
    elif mode == 'yesno>main' and little_fuctions.isequal(response, 'Правила'):
        return_rules()
        mode = 'yesno>rules'
    elif mode == 'yesno>rules' and little_fuctions.isequal(response, 'Начать'):
        return_riddle(1)
        mode = 'yesno>riddle>1'
    elif mode.startswith('yesno>riddle>'):
        number = int(mode.split('>')[2])
        if little_fuctions.isequal(response, 'Назад'):
            return_riddle(number - 1)
            mode = 'yesno>riddle>{}'.format(number - 1)
        elif little_fuctions.isequal(response, 'Дальше'):
            return_riddle(number + 1)
            mode = 'yesno>riddle>{}'.format(number + 1)
        elif little_fuctions.isequal(reponse.split()[0], 'Пропустить'):
            if len(response.split()) == 2 and response.split[1].isdigit():
                skip = int(response.split[1])
            else:
                skip = 1
            return_riddle(number + skip)
            mode = 'yesno>riddle>{}'.format(number + skip)
    else:
        little_fuctions.idk()
    little_fuctions.update_mode(id, mode)
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
    alice_interaction.return_answer(buttons=['Дальше', 'Назад', 'В начало'],
                                    text='{}) {}\nОтвет: {}'.format(number,
                                                                    yes_no_puzzle_biblio.riddles[number],
                                                                    yes_no_puzzle_biblio.answers[number]),
                                    speech=yes_no_puzzle_biblio.riddles[number])
    return

def quit():
    pass
