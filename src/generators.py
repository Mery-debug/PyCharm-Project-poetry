from typing import Union


def filter_by_currency(transactions: list[dict], val: Union[str] ="USD"):
    try:
        for i in range(0, len(transactions) + 1):
            try:
                if transactions[i]["operationAmount"]["currency"]["name"] == val:
                    yield transactions[i]
            except IndexError or StopIteration:
                print("Количество итераций закончилось")
    except KeyError:
        yield f"Вы пытаетесь обработать пустой словарь"


def transaction_descriptions(transactions: list[dict]) -> str:
    result = list((transaction["description"] for transaction in transactions if transaction != [{}]))
    for i in range(0, len(result)):
        yield result[i]
        i += 1


def card_number_generator(start: int, finish: int):
    result = [i for i in range(start, finish + 1)]
    str_0 = '000'
    for resul in result:
        total = str_0 + str(resul)
        total_sum = str_0 + str_0 + str_0 + str_0 + total
        yield f"{total_sum[-16:-12]} {total_sum[-12:-8]} {total_sum[-8:-4]} {total_sum[-4:]}"
