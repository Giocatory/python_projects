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
