documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def show_names():
    try:
        for doc_search in documents:
            names = doc_search['name']
            print(f'{names}')
    except KeyError:
        print('Обнаружен документ без владельца!')


def search_name():
    '''Ищет человека по номеру документа'''
    number_input = input('Номер документа: ')

    found = 0
    for doc_search in documents:
        if number_input in doc_search.values():
            print(doc_search['name'])
            found += 1
    if found == 0:
        print('Документ с таким номером не обнаружен!')


def show_all_docs():
    '''Выводит перечень всех доментов'''
    for doc_search in documents:
        print('{}: "{}" "{}"'
            .format(
            doc_search['type'],
            doc_search['number'],
            doc_search['name']
        )
        )


def search_shelf():
    '''Ищет полку по номеру документа'''
    number_input = input('Номер документа: ')

    found = 0
    for shelf, doc in directories.items():
        if number_input in doc:
            print(shelf)
            found += 1

    if found == 0:
        print('Документ с таким номером не обнаружен!')


def add_doc():
    '''Добавляет новый документа в каталог и на полку'''
    type_input = input('Тип документа: ')
    number_input = input('Номер документа: ')
    name_input = input('Кому принадлежит: ')
    shelf_input = input('Куда кладём: ')

    found = 0
    for shelf, doc in directories.items():
        if shelf_input in shelf:
            doc.append(number_input)
            found += 1

    if found > 0:
        new_doc = {
            'type': type_input,
            'number': number_input,
            'name': name_input
        }
        documents.append(new_doc)
    else:
        print('Такой полки не существует. Сначала создайте её командой "as".')


def del_doc():
    '''Удаляет документ по номеру'''
    number_input = input('Номер документа: ')

    found = 0
    for doc_search in documents:
        if number_input in doc_search.values():
            dict.clear(doc_search)
            found =+ 1
            documents.remove({})

    if found > 0:
        for doc in directories.values():
            if number_input in doc:
                doc.remove(number_input)
    else:
        print('Документ с таким номером не обнаружен!')


def move_doc():
    '''Перемещает документ на выбранную полку'''
    number_input = input('Номер документа: ')

    found = 0
    for doc in directories.values():
        if number_input in doc:
            found += 1

    if found == 0:
        print('Документ с таким номером не обнаружен!')
        return TypeError
    else:
        shelf_input = input('Куда перекладываем: ')

        for shelf in directories.keys():
            if shelf_input in shelf:
                found += 1

        if found == 1:
            print('Такой полки не существует. Сначала создайте её командой "as".')
            return TypeError
        else:
            for shelf, doc in directories.items():
                if shelf_input in shelf:
                    doc.append(number_input)
                elif number_input in doc:
                    doc.remove(number_input)


def create_shelf():
    '''Спрашивает номер новой полки и создаёт её в перечне'''
    new_shelf_input = input('Идентификатор новой полки: ')

    found = 0
    dir_it = directories.copy()
    # Будем итерироваться по копии, чтобы поменять тело списка
    for shelf, doc in dir_it.items():
        if new_shelf_input in shelf:
            found += 1

    if found == 0:
        directories[new_shelf_input] = []
    else:
        print('Такая полка уже существует!')


def show():
    '''Вспомогательная функция для отладки'''
    print(directories)
    print(documents)


def main():
    print('p - найти человека по номеру документа')
    print('ap - показать все имена владельцев')
    print('l - вывести список всех документов')
    print('s - показать, где хранится документ')
    print('a - добавить новый документ')
    print('d - удалить документ')
    print('m - переместить документ на другую полку')
    print('as - добавить новую полку в перечень')
    print('q - выход')
    while True:
        print()
        user_input = input('Введите команду: ')
        if user_input == 'p':
            search_name()
        elif user_input == 'ap':
            show_names()
        elif user_input == 'l':
            show_all_docs()
        elif user_input == 's':
            search_shelf()
        elif user_input == 'a':
            add_doc()
        elif user_input == 'd':
            del_doc()
        elif user_input == 'm':
            move_doc()
        elif user_input == 'as':
            create_shelf()
        elif user_input == '1':
            show()
        elif user_input == 'q':
            print('До свидания!')
            break


if __name__ == "__main__":
    main()
