from src.Users import number, status, ad_questions, result_main


def main():
    final = ad_questions(status(number()))
    print(final)
    a = result_main(ad_questions(status(number())))
    if a[1] == "Открытие вклада":
        print('Распечатываю итоговый список транзакций...')
        print(f'Всего банковских операций в выборке: {len(final)}')
        print(f'{a[0]} {a[1]}')
        print(f'{a[3]}')
        print(f'Сумма: {a[4]} {a[5]}')
    else:
        print('Распечатываю итоговый список транзакций...')
        print(f'Всего банковских операций в выборке: {len(final)}')
        print(f'{a[0]} {a[1]}')
        print(f'{a[2]} -> {a[2]}')
        print(f'Сумма: {a[4]} {a[5]}')


if __name__ == '__main__':
    print(main())
