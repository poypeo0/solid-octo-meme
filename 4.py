import csv

#функции
def message_generation(s):
    '''
    Описание функции message_generation:
    :param s: массив с информацией о корабле
    :return: сообщение вида '<код корабля> <координаты корабля>', закодированное кодом морзе
    '''
    file = open('morse_code.txt', encoding='utf8')
    morse = file.readlines()
    file.close()
    message_morse = ''
    ship_code = s[0].split('-')[0]
    coord = s[2]
    message = ship_code + ' ' + coord
    for i in message:
        for j in range(0, len(morse), 2):
            if i == morse[j][:-1]:
                message_morse += morse[j + 1][:-1]
    return message_morse


def message_write(file_path='space.csv'):
    '''
    Описание функции message_write:
    :param file_path - путь к файлу с данными о кораблях

    результатом работы функции является запись новых данных в файл message_for_ship.csv
    '''

    #считывание данных
    file = open(file_path, encoding='utf8')
    ans = list(csv.reader(file, delimiter=',', quotechar='"'))
    file.close()

    #запись сообщений для кораблей в массив
    ans[0].append('message')
    for i in ans[1:]:
        i.append(message_generation(i))
    
    #запись новых данных в файл
    file_write = open('message_for_ship.csv', 'w', encoding='utf8')
    for i in ans:
        file_write.write(', '.join(i) + '\n')
    file_write.close()

#генерация сообщений и запись их в файл
message_write()