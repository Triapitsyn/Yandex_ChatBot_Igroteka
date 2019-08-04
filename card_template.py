colors = 3
home = ["1652229/c2193d73b25401b5362a", '965417/2838858020e269575ce3', '937455/5ce1d2c4e53d64fb1f47']
rules = ["965417/00447ee42d0940013267", '1652229/d0e2d4a9e0d0bb2ffda3', '1652229/3e0bbfd9a953de0d46b4']
start = ['1540737/79627bde770d8f34397c', '1030494/49ec2debd850950e74f0', '1030494/46deb85e9c129f1acb49']

yesno = ["1652229/7c3339e7fe69bdc4f353", '1030494/5992bbd0eabebd28dbfe', '1656841/e51b8ffb620d18a2d34a']
Inever = ["965417/6217dbc67deb68a944c1"]
croco = ["1540737/e4f18f914499c70be0d4", '1540737/c6823b8ea52d63ac612d', '1652229/e87e4ec30cbe1aefdc3a']
helper = ["937455/425ee5f062cb333a36b8", '1540737/c1d96c906443760415b0', '937455/d8dcbc769defad8c1129']
Ineverwith = ["965417/cbafe44df6130a53c3dc", '1652229/9d98062fbb6a738aaa60', '1652229/6f3f8b2e004dc95a3ff6']

easy = ["1030494/f17aed3293f46bf1e960", '1540737/b3a5645da0c305f09740', '1656841/e3e755739b7465e4e085']
normal = ["965417/c995920af01333ad2b43", '965417/e9cc44576df31ce2064c', '1652229/13733d31b7f1ebc82fe2']
hard = ["1652229/8b1dfcea37a970a08596", '965417/3d046ed1ed7517e10485', '965417/0f2219da6460bf640bdd']
unreal = ["1652229/131158d510f8dc34c9a4", '937455/499dc6a73b8538ce57d2', '965417/2d2b928534e5dd0bc08f']



def start_card(color = 0):
    color = color % colors
    return {
            "type": "ItemsList",
            "header": {
                "text": "Стартовое меню (название временное)",
            },
            "items": [
                {
                    "image_id": yesno[color],
                    "title": "Данетки",
                    "description": "Занимательная игра для друзей. Почувствуй себя детективом.",
                    "button": {
                        "payload": {"name": "Данетки"}
                    }
                },
                {
                    "image_id": Inever[0],
                    "title": "Я никогда не",
                    "description": "Игра сближает людей. Узнайте друг о друге много нового.",
                    "button": {
                        "payload": {"name": "Я никогда не"}
                    }
                },
                {
                    "image_id": croco[color],
                    "title": "Крокодил",
                    "description": "Известная веселая игра, подходящая и взрослым, и детям.",
                    "button": {
                        "payload": {"name": "Крокодил"}
                    }
                },
                {
                    "image_id": helper[color],
                    "title": "Сменить цвета",
                    "description": "Почему бы и нет?",
                    "button": {
                        "payload": {"name": "Сменить цвет!"}
                    }
                },
                {
                    "image_id": helper[color],
                    "title": "Помощь",
                    "description": "Я помогу тебе разобраться в этом навыке.",
                    "button": {
                        "payload": {"name": "Помощь"}
                    }
                }
            ],
    }

def inever_card(color = 0):
    color = color % colors
    return {
            "type": "ItemsList",
            "header": {
                "text": "Я никогда не",
            },
            "items": [
                {
                    "image_id": start[color],
                    "title": "Начать",
                    "description": "Не забудь уточнить правила. Приятной игры!",
                    "button": {
                        "payload": {"name": "Начать"}
                    }
                },
                {
                    "image_id": Ineverwith[color],
                    "title": "Играть с разработчиком",
                    "description": "Кто-то из команды разработчиков сыграет с вами.",
                    "button": {
                        "payload": {"name": "Играть с разработчиком"}
                    }
                },
                {
                    "image_id": rules[color],
                    "title": "Правила",
                    "description": "Я быстро расскажу тебе немного правил.",
                    "button": {
                        "payload": {"name": "Правила"}
                    }
                },
                {
                    "image_id": home[color],
                    "title": "В начало",
                    "description": "Вернуться к истокам.",
                    "button": {
                        "payload": {"name": "В начало"}
                    }
                }
            ],
    }

def croco_card(color = 0):
    color = color % colors
    return {
            "type": "ItemsList",
            "header": {
                "text": "Крокодил",
            },
            "items": [
                {
                    "image_id": start[color],
                    "title": "Начать",
                    "description": "Не забудь уточнить правила. Приятной игры!",
                    "button": {
                        "payload": {"name": "Начать"}
                    }
                },
                {
                    "image_id": rules[color],
                    "title": "Правила",
                    "description": "Я быстро расскажу тебе немного правил.",
                    "button": {
                        "payload": {"name": "Правила"}
                    }
                },
                {
                    "image_id": home[color],
                    "title": "В начало",
                    "description": "Вернуться к истокам.",
                    "button": {
                        "payload": {"name": "В начало"}
                    }
                }
            ],
    }

def yesno_card(color = 0):
    color = color % colors
    return {
            "type": "ItemsList",
            "header": {
                "text": "Данетки",
            },
            "items": [
                {
                    "image_id": start[color],
                    "title": "Начать",
                    "description": 'Не забудь уточнить правила. Приятной игры!',
                    "button": {
                        "payload": {"name": "Начать"}
                    }
                },
                {
                    "image_id": rules[color],
                    "title": "Правила",
                    "description": "Я быстро расскажу тебе немного правил.",
                    "button": {
                        "payload": {"name": "Правила"}
                    }
                },
                {
                    "image_id": home[color],
                    "title": "В начало",
                    "description": "Вернуться к истокам.",
                    "button": {
                        "payload": {"name": "В начало"}
                    }
                }
            ],
    }

def croco_diff_card(color = 0):
    color = color % colors
    return {
            "type": "ItemsList",
            "header": {
                "text": "Сложности",
            },
            "items": [
                {
                    "image_id": easy[color],
                    "title": "Легкие",
                    "description": "Подойдет для разминки.",
                    "button": {
                        "payload": {"name": "Легкие"}
                    }
                },
                {
                    "image_id": normal[color],
                    "title": "Нормальные",
                    "description": "Лучше всего для детей и начинающих.",
                    "button": {
                        "payload": {"name": "Нормальные"}
                    }
                },
                {
                    "image_id": hard[color],
                    "title": "Сложные",
                    "description": "Вот где происходит реальная игра.",
                    "button": {
                        "payload": {"name": "Сложные"}
                    }
                },
                {
                    "image_id": unreal[color],
                    "title": "Невозможные",
                    "description": "Для самых смелых и находчивых.",
                    "button": {
                        "payload": {"name": "Невозможные"}
                    }
                },
                {
                    "image_id": home[color],
                    "title": "В начало",
                    "description": "Вернуться к истокам.",
                    "button": {
                        "payload": {"name": "В начало"}
                    }
                }
            ],
    }
