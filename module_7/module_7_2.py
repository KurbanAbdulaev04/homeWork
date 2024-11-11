def custom_write(file_name: str, string: list):
    # использую режим редактирования write('w') что-бы файл автоматически создавался
    file_name = open(file_name, 'w', encoding='utf-8')

    strings_positions = {}

    # для отслеживания строки создадим переменную равную нулю, и в процессе будем добавлять 1
    # можно также импортировать fileinput, и через цикл проверять на какой строке находимся на момент добавления строки,
    # но для данной задачи, думаю так будет проще
    num = 0

    for i in string:
        num += 1
        strings_positions[(num, file_name.tell())] = f'{i}'
        file_name.write(f'{i}\n')

    file_name.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)