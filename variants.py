# coding=utf-8

# Variant is a list of Tasks
# Task is a dict of id and Conditions
# Condition is a dict of path and optional fields like:
# type, permissions, owner, group, privacy_label, integrity, categories, flags

pz_variant = [
    {
        'id': '1',
        'conditions': [
            {
                'path': '/Совершенно_секретно',
                'type': 'd',
                'permissions': '770',
                # 'owner': 'root',
                'group': 'secret_users',
                'privacy_label': 'Совершенно_секретно',
                # 'integrity': 'Низкий',
                'categories': [],
                'flags': ['ccnr']
            }
        ]
    },
    {
        'id': '2',
        'conditions': [
            {
                'path': '/Совершенно_секретно/Совершенно_секретно.txt',
                'type': 'f',
                'permissions': '770',
                # 'owner': 'root',
                'group': 'secret_users',
                'privacy_label': 'Совершенно_секретно',
                # 'integrity': 'Низкий',
                'categories': [],
                'flags': []
            }
        ]
    },
    {
        'id': '3',
        'conditions': [
            {
                'path': '/Совершенно_секретно/Секретно',
                'type': 'd',
                'permissions': '770',
                # 'owner': 'root',
                'group': 'secret_users',
                'privacy_label': 'Секретно',
                # 'integrity': 'Низкий',
                'categories': [],
                'flags': ['ccnr']
            }
        ]
    },
    {
        'id': '4',
        'conditions': [
            {
                'path': '/Совершенно_секретно/Секретно/Секретно.txt',
                'type': 'f',
                'permissions': '770',
                # 'owner': 'root',
                'group': 'secret_users',
                'privacy_label': 'Секретно',
                # 'integrity': 'Низкий',
                'categories': [],
                'flags': []
            }
        ]
    },
    {
        'id': '5',
        'conditions': [
            {
                'path': '/Совершенно_секретно/Секретно/Новый файл.txt',
                'type': 'f',
                # 'permissions': '770',
                'owner': 'user1',
                # 'group': 'secret_users',
                'privacy_label': 'Секретно',
                # 'integrity': 'Низкий',
                'categories': [],
                'flags': []
            }
        ]
    },
    {
        'id': '6',
        'conditions': [
            {
                'path': '/Совершенно_секретно/Новый файл.txt',
                'type': 'f',
                # 'permissions': '770',
                'owner': 'user2',
                # 'group': 'secret_users',
                'privacy_label': 'Совершенно_секретно',
                # 'integrity': 'Низкий',
                'categories': [],
                'flags': []
            }
        ]
    },
]

hw_variant = [
    {
        'id': '1',
        'conditions': [
            {
                'path': '/ОсобойВажности_SURNAME',
                'type': 'd',
            },
            {
                'path': '/ОсобойВажности_SURNAME/Рапорт_SURNAME',
                'type': 'f',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ЗаявкаОбслуживаниеБСП_SURNAME',
                'type': 'f',
            },
            {
                'path': '/ОсобойВажности_SURNAME/РасписаниеПроверок',
                'type': 'f',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME',
                'type': 'd',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Отпускные',
                'type': 'f',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Форма4_SURNAME',
                'type': 'f',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME',
                'type': 'd',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Дежурства',
                'type': 'f',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Шифровка',
                'type': 'f',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Смета_SURNAME',
                'type': 'f',
            }
        ]
    },
    {
        'id': '2',
        'conditions': [
            {
                'path': '/ОсобойВажности_SURNAME',
                'permissions': '755',
            },
            {
                'path': '/ОсобойВажности_SURNAME/Рапорт_SURNAME',
                'permissions': '600',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ЗаявкаОбслуживаниеБСП_SURNAME',
                'permissions': '600',
            },
            {
                'path': '/ОсобойВажности_SURNAME/РасписаниеПроверок',
                'permissions': '600',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME',
                'permissions': '755',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Отпускные',
                'permissions': '640',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Форма4_SURNAME',
                'permissions': '640',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME',
                'permissions': '755',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Дежурства',
                'permissions': '644',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Шифровка',
                'permissions': '644',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Смета_SURNAME',
                'permissions': '644',
            }
        ]
    },
    {
        'id': '3',
        'conditions': [
            {
                'path': '/ОсобойВажности_SURNAME',
                'owner': 'SURNAME3',
            },
            {
                'path': '/ОсобойВажности_SURNAME/Рапорт_SURNAME',
                'owner': 'SURNAME3',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ЗаявкаОбслуживаниеБСП_SURNAME',
                'owner': 'SURNAME3',
            },
            {
                'path': '/ОсобойВажности_SURNAME/РасписаниеПроверок',
                'owner': 'SURNAME3',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME',
                'owner': 'SURNAME2',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Отпускные',
                'owner': 'SURNAME2',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Форма4_SURNAME',
                'owner': 'SURNAME2',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME',
                'owner': 'SURNAME1',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Дежурства',
                'owner': 'SURNAME1',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Шифровка',
                'owner': 'SURNAME1',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Смета_SURNAME',
                'owner': 'SURNAME1',
            }
        ]
    },
    {
        'id': '4',
        'conditions': [
            {
                'path': '/ОсобойВажности_SURNAME',
                'owner': 'SURNAME3',
            },
            {
                'path': '/ОсобойВажности_SURNAME/Рапорт_SURNAME',
                'owner': 'SURNAME3',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ЗаявкаОбслуживаниеБСП_SURNAME',
                'owner': 'SURNAME3',
            },
            {
                'path': '/ОсобойВажности_SURNAME/РасписаниеПроверок',
                'owner': 'SURNAME3',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME',
                'owner': 'SURNAME2',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Отпускные',
                'owner': 'SURNAME2',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Форма4_SURNAME',
                'owner': 'SURNAME2',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME',
                'owner': 'SURNAME1',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Дежурства',
                'owner': 'SURNAME1',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Шифровка',
                'owner': 'SURNAME1',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Смета_SURNAME',
                'owner': 'SURNAME1',
            }
        ]
    },
    {
        'id': '5',
        'conditions': [
            {
                'path': '/ОсобойВажности_SURNAME',
                'privacy_label': 'ОсобойВажности',
            },
            {
                'path': '/ОсобойВажности_SURNAME/Рапорт_SURNAME',
                'privacy_label': 'ОсобойВажности',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ЗаявкаОбслуживаниеБСП_SURNAME',
                'privacy_label': 'ОсобойВажности',
            },
            {
                'path': '/ОсобойВажности_SURNAME/РасписаниеПроверок',
                'privacy_label': 'ОсобойВажности',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME',
                'privacy_label': 'СовершенноСекретно',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Отпускные',
                'privacy_label': 'СовершенноСекретно',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Форма4_SURNAME',
                'privacy_label': 'СовершенноСекретно',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME',
                'privacy_label': 'Секретно',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Дежурства',
                'privacy_label': 'Секретно',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Шифровка',
                'privacy_label': 'Секретно',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Смета_SURNAME',
                'privacy_label': 'Секретно',
            }
        ]
    },
    {
        'id': '6',
        'conditions': [
            {
                'path': '/ОсобойВажности_SURNAME',
                'integrity': 'Низкий',
            },
            {
                'path': '/ОсобойВажности_SURNAME/Рапорт_SURNAME',
                'integrity': 'Низкий',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ЗаявкаОбслуживаниеБСП_SURNAME',
                'integrity': 'Низкий',
            },
            {
                'path': '/ОсобойВажности_SURNAME/РасписаниеПроверок',
                'integrity': 'Низкий',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME',
                'integrity': 'Низкий',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Отпускные',
                'integrity': 'Низкий',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Форма4_SURNAME',
                'integrity': 'Низкий',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME',
                'integrity': 'Низкий',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Дежурства',
                'integrity': 'Низкий',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Шифровка',
                'integrity': 'Низкий',
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Смета_SURNAME',
                'integrity': 'Низкий',
            }
        ]
    },
    {
        'id': '7',
        'conditions': [
            {
                'path': '/ОсобойВажности_SURNAME',
                'categories': ['Связь', 'Управление', 'ЛичныйСостав', 'Боевое'],
            },
            {
                'path': '/ОсобойВажности_SURNAME/Рапорт_SURNAME',
                'categories': ['ЛичныйСостав'],
            },
            {
                'path': '/ОсобойВажности_SURNAME/ЗаявкаОбслуживаниеБСП_SURNAME',
                'categories': ['Боевое'],
            },
            {
                'path': '/ОсобойВажности_SURNAME/РасписаниеПроверок',
                'categories': ['Боевое'],
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME',
                'categories': ['Связь', 'Управление', 'ЛичныйСостав'],
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Отпускные',
                'categories': ['ЛичныйСостав'],
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Форма4_SURNAME',
                'categories': ['ЛичныйСостав', 'Управление'],
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME',
                'categories': ['Связь', 'Управление'],
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Дежурства',
                'categories': ['Управление'],
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Шифровка',
                'categories': ['Связь'],
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Смета_SURNAME',
                'categories': ['Управление'],
            }
        ]
    },
    {
        'id': '8',
        'conditions': [
            {
                'path': '/ОсобойВажности_SURNAME',
                'flags': ['ccnr']
            },
            {
                'path': '/ОсобойВажности_SURNAME/Рапорт_SURNAME',
                'flags': []
            },
            {
                'path': '/ОсобойВажности_SURNAME/ЗаявкаОбслуживаниеБСП_SURNAME',
                'flags': []
            },
            {
                'path': '/ОсобойВажности_SURNAME/РасписаниеПроверок',
                'flags': []
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME',
                'flags': ['ccnr']
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Отпускные',
                'flags': []
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Форма4_SURNAME',
                'flags': []
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME',
                'flags': ['ccnr']
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Дежурства',
                'flags': []
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Шифровка',
                'flags': []
            },
            {
                'path': '/ОсобойВажности_SURNAME/СовершенноСекретно_SURNAME/Секретно_SURNAME/Смета_SURNAME',
                'flags': []
            }
        ]
    },
]

exam_variant = [
    {
        'id': '1',
        'conditions': [
            {
                'path': '/Секретно_SURNAME',
                'type': 'd',
            },
            {
                'path': '/Секретно_SURNAME/Шифровка',
                'type': 'f',
            },
            {
                'path': '/Секретно_SURNAME/Смета_SURNAME',
                'type': 'f',
            },
            {
                'path': '/СовершенноСекретно_SURNAME',
                'type': 'd',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ЛичноеДело_SURNAME',
                'type': 'f',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/Дежурства',
                'type': 'f',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ВременныеПропуска',
                'type': 'f',
            },
            {
                'path': '/ОсобойВажности_SURNAME',
                'type': 'd',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ПланОхраныИОбороны_SURNAME',
                'type': 'f',
            },
            {
                'path': '/ОсобойВажности_SURNAME/КомандованиеВЧ',
                'type': 'f',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ВооружениеВЧ',
                'type': 'f',
            }
        ]
    },
    {
        'id': '2',
        'conditions': [
            {
                'path': '/Секретно_SURNAME',
                'permissions': '755',
            },
            {
                'path': '/Секретно_SURNAME/Шифровка',
                'permissions': '644',
            },
            {
                'path': '/Секретно_SURNAME/Смета_SURNAME',
                'permissions': '644',
            },
            {
                'path': '/СовершенноСекретно_SURNAME',
                'permissions': '755',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ЛичноеДело_SURNAME',
                'permissions': '640',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/Дежурства',
                'permissions': '640',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ВременныеПропуска',
                'permissions': '640',
            },
            {
                'path': '/ОсобойВажности_SURNAME',
                'permissions': '755',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ПланОхраныИОбороны_SURNAME',
                'permissions': '600',
            },
            {
                'path': '/ОсобойВажности_SURNAME/КомандованиеВЧ',
                'permissions': '600',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ВооружениеВЧ',
                'permissions': '600',
            },
        ]
    },
    {
        'id': '3',
        'conditions': [
            {
                'path': '/Секретно_SURNAME',
                'owner': 'SURNAME1',
            },
            {
                'path': '/Секретно_SURNAME/Шифровка',
                'owner': 'SURNAME1',
            },
            {
                'path': '/Секретно_SURNAME/Смета_SURNAME',
                'owner': 'SURNAME1',
            },
            {
                'path': '/СовершенноСекретно_SURNAME',
                'owner': 'SURNAME2',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ЛичноеДело_SURNAME',
                'owner': 'SURNAME2',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/Дежурства',
                'owner': 'SURNAME2',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ВременныеПропуска',
                'owner': 'SURNAME2',
            },
            {
                'path': '/ОсобойВажности_SURNAME',
                'owner': 'SURNAME3',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ПланОхраныИОбороны_SURNAME',
                'owner': 'SURNAME3',
            },
            {
                'path': '/ОсобойВажности_SURNAME/КомандованиеВЧ',
                'owner': 'SURNAME3',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ВооружениеВЧ',
                'owner': 'SURNAME3',
            },
        ]
    },
    {
        'id': '4',
        'conditions': [
            {
                'path': '/Секретно_SURNAME',
                'group': 'SURNAME1',
            },
            {
                'path': '/Секретно_SURNAME/Шифровка',
                'group': 'SURNAME1',
            },
            {
                'path': '/Секретно_SURNAME/Смета_SURNAME',
                'group': 'SURNAME1',
            },
            {
                'path': '/СовершенноСекретно_SURNAME',
                'group': 'SURNAME2',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ЛичноеДело_SURNAME',
                'group': 'SURNAME2',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/Дежурства',
                'group': 'SURNAME2',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ВременныеПропуска',
                'group': 'SURNAME2',
            },
            {
                'path': '/ОсобойВажности_SURNAME',
                'group': 'SURNAME3',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ПланОхраныИОбороны_SURNAME',
                'group': 'SURNAME3',
            },
            {
                'path': '/ОсобойВажности_SURNAME/КомандованиеВЧ',
                'group': 'SURNAME3',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ВооружениеВЧ',
                'group': 'SURNAME3',
            },
        ]
    },
    {
        'id': '5',
        'conditions': [
            {
                'path': '/Секретно_SURNAME',
                'privacy_label': 'Секретно',
            },
            {
                'path': '/Секретно_SURNAME/Шифровка',
                'privacy_label': 'Секретно',
            },
            {
                'path': '/Секретно_SURNAME/Смета_SURNAME',
                'privacy_label': 'Секретно',
            },
            {
                'path': '/СовершенноСекретно_SURNAME',
                'privacy_label': 'СовершенноСекретно',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ЛичноеДело_SURNAME',
                'privacy_label': 'СовершенноСекретно',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/Дежурства',
                'privacy_label': 'СовершенноСекретно',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ВременныеПропуска',
                'privacy_label': 'СовершенноСекретно',
            },
            {
                'path': '/ОсобойВажности_SURNAME',
                'privacy_label': 'ОсобойВажности',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ПланОхраныИОбороны_SURNAME',
                'privacy_label': 'ОсобойВажности',
            },
            {
                'path': '/ОсобойВажности_SURNAME/КомандованиеВЧ',
                'privacy_label': 'ОсобойВажности',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ВооружениеВЧ',
                'privacy_label': 'ОсобойВажности',
            },
        ]
    },
    {
        'id': '6',
        'conditions': [
            {
                'path': '/Секретно_SURNAME',
                'integrity': 'Низкий',
            },
            {
                'path': '/Секретно_SURNAME/Шифровка',
                'integrity': 'Низкий',
            },
            {
                'path': '/Секретно_SURNAME/Смета_SURNAME',
                'integrity': 'Низкий',
            },
            {
                'path': '/СовершенноСекретно_SURNAME',
                'integrity': 'Низкий',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ЛичноеДело_SURNAME',
                'integrity': 'Низкий',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/Дежурства',
                'integrity': 'Низкий',
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ВременныеПропуска',
                'integrity': 'Низкий',
            },
            {
                'path': '/ОсобойВажности_SURNAME',
                'integrity': 'Низкий',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ПланОхраныИОбороны_SURNAME',
                'integrity': 'Низкий',
            },
            {
                'path': '/ОсобойВажности_SURNAME/КомандованиеВЧ',
                'integrity': 'Низкий',
            },
            {
                'path': '/ОсобойВажности_SURNAME/ВооружениеВЧ',
                'integrity': 'Низкий',
            },
        ]
    },
    {
        'id': '7',
        'conditions': [
            {
                'path': '/Секретно_SURNAME',
                'categories': ['Связь', 'Управление'],
            },
            {
                'path': '/Секретно_SURNAME/Шифровка',
                'categories': ['Связь'],
            },
            {
                'path': '/Секретно_SURNAME/Смета_SURNAME',
                'categories': ['Управление'],
            },
            {
                'path': '/СовершенноСекретно_SURNAME',
                'categories': ['ЛичныйСостав', 'Управление'],
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ЛичноеДело_SURNAME',
                'categories': ['ЛичныйСостав'],
            },
            {
                'path': '/СовершенноСекретно_SURNAME/Дежурства',
                'categories': ['Управление'],
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ВременныеПропуска',
                'categories': ['Управление'],
            },
            {
                'path': '/ОсобойВажности_SURNAME',
                'categories': ['ЛичныйСостав', 'Боевое'],
            },
            {
                'path': '/ОсобойВажности_SURNAME/ПланОхраныИОбороны_SURNAME',
                'categories': ['Боевое'],
            },
            {
                'path': '/ОсобойВажности_SURNAME/КомандованиеВЧ',
                'categories': ['ЛичныйСостав'],
            },
            {
                'path': '/ОсобойВажности_SURNAME/ВооружениеВЧ',
                'categories': ['Боевое'],
            },
        ]
    },
    {
        'id': '8',
        'conditions': [
            {
                'path': '/Секретно_SURNAME',
                'flags': ['ccnr']
            },
            {
                'path': '/Секретно_SURNAME/Шифровка',
                'flags': []
            },
            {
                'path': '/Секретно_SURNAME/Смета_SURNAME',
                'flags': []
            },
            {
                'path': '/СовершенноСекретно_SURNAME',
                'flags': ['ccnr']
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ЛичноеДело_SURNAME',
                'flags': []
            },
            {
                'path': '/СовершенноСекретно_SURNAME/Дежурства',
                'flags': []
            },
            {
                'path': '/СовершенноСекретно_SURNAME/ВременныеПропуска',
                'flags': []
            },
            {
                'path': '/ОсобойВажности_SURNAME',
                'flags': ['ccnr']
            },
            {
                'path': '/ОсобойВажности_SURNAME/ПланОхраныИОбороны_SURNAME',
                'flags': []
            },
            {
                'path': '/ОсобойВажности_SURNAME/КомандованиеВЧ',
                'flags': []
            },
            {
                'path': '/ОсобойВажности_SURNAME/ВооружениеВЧ',
                'flags': []
            },
        ]
    },
]

variants = {
    'pz': pz_variant,
    'hw': hw_variant,
    'exam': exam_variant
}
