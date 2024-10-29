from src.Users import number, status, ad_questions, result_main


def main():
    modul = number()
    print(modul)
    modul_transaction = status(modul)
    print(modul_transaction)
    final = ad_questions(modul_transaction)
    if not final:
        return []
    else:
        a = result_main(final)
        if len(final) == 0:
            return 'Не найдено ни одной транзакции, подходящей под ваши условия фильтрации'
        else:
            print('Распечатываю итоговый список транзакций...')
            print(f'Всего банковских операций в выборке: {len(final)}')
            for i in range(len(final)):
                print(f'{a[0]} {a[1]}')
                if a[1] == "Открытие вклада":
                    print(f'{a[2]}')
                    print(f'Сумма: {a[3]} {a[4]}\n')
                else:
                    print(f'{a[2]} -> {a[3]}')
                    print(f'Сумма: {a[4]} {a[5]}\n')
            return "конец"


if __name__ == '__main__':
    print(main())
