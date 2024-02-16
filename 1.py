import csv

#считывание данных
f = open('space.csv', encoding='utf8')
ans = list(csv.reader(f, delimiter=',', quotechar='"'))[1:]
f.close()

#поиск кораблей с неизвестными координатами
new = []
for i in ans:
    if i[2] == '0 0':
        s_x = len(i[1]) - int(i[-1].split(' ')[0])
        s_y = len(i[1]) - int(i[-1].split(' ')[1])
        new.append(f'При получении данных о корабле {i[0]} возникли сбои. Предположительные координаты - {s_x}, {s_y}')

#запись данных в файл
f_write = open('space_new.txt', 'w', encoding='utf8')
for i in new:
    f_write.write(i + '\n')
f_write.close()
