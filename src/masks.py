import logging


logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/masks.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number: str) -> str:
    """Function for masking cart number"""

    if number != "":
        logger.info(f'Строка не пустая: {number}')
        if len(number) == 16:
            logger.info('Длинна равна 16')
            number_replace = "** ****"
            modify_number = f"{number[0:4]} {number[4:6]}{number_replace} {number[12:]}"
            logger.info(f'Замаскировали пришедший номер карты: {modify_number}')
            return modify_number
        elif len(number) < 16:
            logger.error(f'Произошла ошибка: слишком короткая строка')
            return "Ошибка ввода, мало символов"
        else:
            logger.error(f'Произошла ошибка: слишком длинная строка')
            return "Ошибка ввода, много символов"
    logger.error(f'Произошла ошибка: пустая строка')
    return "Вы ничего не ввели"


def get_mask_account(account_number: str) -> str:
    """Function for masking bank account"""
    if account_number != "":
        logger.info(f"Введенный номер не пустой: {account_number}")
        if len(account_number) == 20:
            logger.info(f"Замаскированный номер: **{account_number[16:]}")
            return f"**{account_number[16:]}"
        elif len(account_number) < 20:
            logger.error(f"Ошибка ввода: мало символов")
            return "Ошибка ввода, мало символов"
        else:
            logger.error(f"Ошибка ввода: много символов")
            return "Ошибка ввода, много символов"
    else:
        logger.error(f"Ошибка ввода: вы ничего не ввели")
        return "Вы ничего не ввели"


if __name__ == "__main__":
    card_result = get_mask_card_number("1234567812345678")
    mask_account = get_mask_account("12345678900987654321")
    print(f"Маска карты: {card_result} \n Маска счета: {mask_account}")

