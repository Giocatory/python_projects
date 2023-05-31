########### dict methods ###########

##### dict.clear() - Очищение словаря
dict_to_clear = {'one': 1, 'two': 2}
dict_to_clear.clear()
print(dict_to_clear)  # {}

##### dict.copy() - Возвращение копии словаря
user = {
    'name': 'Admin',
    'IP-info': {
        'ip': '192.168.0.0',
        'gate': '192.168.1.1'
    }
}
admin_user = user.copy()
print(admin_user)  # {'name': 'Admin', 'IP-info': {'ip': '192.168.0.0', 'gate': '192.168.1.1'}}

##### dict.fromkeys(sequence, *value) - Создает словарь с ключами из sequence и значением value
# по умолчанию value = None
arr_to_key = ['one', 'two', 'three']
set_to_key = ('four', 'five', 'six')
first_dict = dict.fromkeys(arr_to_key, 33)
second_dict = dict.fromkeys(set_to_key)
print(first_dict)  # {'one': 33, 'two': 33, 'three': 33}
print(second_dict)  # {'four': None, 'five': None, 'six': None}

##### dict.get(key, *default) - возвращает кзначение ключа, но если ключа нет, то вместо исключения
# возвращает defaul (по умолчанию default = None)
user_info = {
    'name': 'Admin',
    'IP-info': {
        'ip': '192.168.0.0',
        'gate': '192.168.1.1'
    }
}
print(user_info.get("name", "not admin"))  # Admin
print(user_info.get("proxy", "computer with auto proxy"))  # computer with auto proxy

##### dict.items() - возвращает пары (ключ, значение)
##### dict.keys() - возвращает ключи словаря
##### dict.values() - возвращает значения ключей словаря
##### dict.pop(key, *default) - удаляет ключ и возвращает значение. Если ключа нет возвращает default
# по умолчанию (если default не указан) выбрасывает исключение
##### dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, то исключение
##### dict.setdefault(key, *default) - возвращает значение ключа, но если его нет, то не бросает
# исключение, а создает новый ключ со значением default (по умолчанию None)
##### dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other
# СУЩЕСТВУЮЩИЕ КЛЮЧИ ПЕРЕЗАПИСЫВАЮТСЯ!!!!
# Возвращает None (а не новый словарь!!!!)