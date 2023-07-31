import json
from datetime import date, datetime


def load_operation():
    '''Загружает данные из json файла'''
    with open("operations.json", 'r', encoding="utf-8") as file:
        data = json.load(file)

    return data


def get_filtered_operation(data):
    """Фильтрует получиный список на наличие 'EXECUTED'"""
    filrered_operations = []
    for d in data:
        if 'state' in d:
            if d['state'] == 'EXECUTED':
                filrered_operations.append(d)

    return filrered_operations


def key_date(d):
    """Возвращает ключ 'date'"""
    return d['date']


def get_last_operation(filrered_operations):
    """Получаем 5 последних операций"""
    filrered_operations = sorted(filrered_operations, key=key_date, reverse=True)
    sort_operation = filrered_operations[:5]
    return sort_operation


def get_formatted_date(get_last_operation):
    """Изменяет дату"""
    format_date = []
    for item in get_last_operation:
        time = datetime.strptime(item['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')
        format_date.append(time)

    return format_date


def get_hidden_num_check_and_cart(payment):
    """Получаем скрытые даннее карт и счетов"""
    hidden_num_check = []
    for item in payment:
        if not item:
            hidden_num_check.append('')
        elif item.split()[0] == 'Счет':
            hidden_num_check.append(f"Счет **{item[-4:]}")
        else:
            hidden_num_check.append(f"{item[:-12]} {item[-12:-10]}** **** {item[-4:]}")

    return hidden_num_check


def get_to_list(get_last_operation):
    """Создает списки с 'To and From'"""
    list_to = []
    list_from = []
    for operation in get_last_operation:
        list_to.append(operation['to'])
        if "from" in operation:
            list_from.append(operation['from'])
        else:
            list_from.append('')
    return list_to, list_from


def get_description(get_last_operation):
    """Выводит описание операции"""
    description = []
    for item in get_last_operation:
        description.append(item['description'])

    return description


def get_amount(get_last_operation):
    """Выводит сумму"""
    amount = []
    for item in get_last_operation:
        amount.append(item['operationAmount']['amount'])

    return amount


def get_currency(get_last_operation):
    """Выводит валюту"""
    currency = []
    for item in get_last_operation:
        currency.append(item['operationAmount']['currency']['name'])

    return currency
