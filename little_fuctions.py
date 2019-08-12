def get_suggests(user_storage):
    if "suggests" in user_storage.keys():
        suggests = []
        for suggest in user_storage['suggests']:
            if type(suggest) != list:
                suggests.append({'title': suggest, 'hide': True})
            else:
                suggests.append({'title': suggest[0], "url": suggest[1], 'hide': False})
    else:
        suggests = []

    return suggests, user_storage


def IDontUnderstand(response, user_storage, answer):
    import random
    message = random.choice(answer)
    response.set_text(message)
    response.set_tts(message + "Доступные команды: {}.".format(" ,".join(user_storage['suggests'])))
    buttons, user_storage = get_suggests(user_storage)
    response.set_buttons(buttons)
    return response, user_storage


def read_answers_data(name):
    import json
    with open(name+".json", encoding="utf-8") as file:
        data = json.loads(file.read())
        return data


aliceAnswers = read_answers_data("data/answers_dict_example")


def get_mode(user_id, database):
    return database.get_entry("users_info", ['mode'], {'request_id': user_id})[0][0]


def update_mode(user_id, mode, database):
    database.update_entries('users_info', user_id, {'mode': mode}, update_type='rewrite')
    return True


def get_set(user_id, database):
    return set(database.get_entry("users_info", ['word_set'], {'request_id': user_id})[0][0].split("#$"))


def update_set(word_set, user_id, database):
    database.update_entries('users_info', user_id, {'word_set': "#$".join(list(word_set))}, update_type='rewrite')
    return True


def get_color(user_id, database):
    return database.get_entry("users_info", ['color'], {'request_id': user_id})[0][0]


def update_color(color, user_id, database):
    database.update_entries('users_info', user_id, {'color': color}, update_type='rewrite')
    return True


def get_silent(user_id, database):
    return database.get_entry("users_info", ['silent'], {'request_id': user_id})[0][0]


def update_silent(silent, user_id, database):
    database.update_entries('users_info', user_id, {'silent': silent}, update_type='rewrite')
    return True


def isequal(text, pattern):
    import synonyms
    return text.capitalize().strip('.,?!').replace('ё', 'е') in synonyms.synonyms[pattern]


def get_lasts(user_id, database):
    return database.get_entry("users_info", ['last_text'], {'request_id': user_id})[0][0],\
            database.get_entry("users_info", ['last_speech'], {'request_id': user_id})[0][0],\
            database.get_entry("users_info", ['last_buttons'], {'request_id': user_id})[0][0].split('#')

def hello():
    import random
    return random.choice(['Выбери игру.',
                          'Во что играем теперь?',
                          'Советую Данетки',
                          'Какая игра вам нравится?',
                          'Прочитайте описания и выберите, во что хотите играть.',
                          'Мне нравятся Крокодил, очень рекомендую.'])
def ready():
    import random
    return random.choice(['Только скажите "начать".',
                          'Начнем игру?',
                          'Начинаем?',
                          'Поехали!',
                          'Желаю приятной игр+ы!',
                          'Отличный выбор!',
                          'Я тоже люблю эту игру',
                          'А у вас хороший вкус в играх.'])

def go_settings():
    import random
    return random.choice(['Ваше указание - честь для меня.',
                          'Только прикажите, Сэр.',
                          'Ваше слово - закон.',
                          'Слушаюсь и повинуюсь.',
                          'Я готова измениться для тебя.',
                          'Ваше желание будет исполнено.'])

def go_color():
    import random
    return random.choice(['Как вам такой цвет?',
                          'Теперь выглядит лучше.',
                          'Довольно милый цвет.',
                          'Я бы сменила цвет+а еще раз.',
                          'Этот цвет мне точно нравится!'])