from typing import Union


def filter_by_currency(transactions: list[dict], val: Union[str] ="USD"):
    try:
        for i in range(len(transactions) + 1):
            if transactions[i]["operationAmount"]["currency"]["name"] == val:
                yield transactions[i]
            else:
                yield f"Нет информации по операциям с этой валютой"
    except KeyError:
        yield f"Вы пытаетесь обработать пустой словарь"


def transaction_descriptions(transactions: list[dict]) -> str:
    for transaction in transactions:
        if transaction != {}:
            result = transaction['description']
            yield result
        else:
            yield f'Вы пытаетесь обработать пустой словарь'


def card_number_generator(start: int, finish: int):
    if start < 1 or finish > 9999999999999999:
        yield f"Ошибка ввода, недопустимый диапазон"
    else:
        result = [i for i in range(start, finish + 1)]
        str_0 = '000'
        for resul in result:
            total = str_0 + str(resul)
            total_sum = str_0 + str_0 + str_0 + str_0 + total
            yield f"{total_sum[-16:-12]} {total_sum[-12:-8]} {total_sum[-8:-4]} {total_sum[-4:]}"
