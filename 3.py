import csv

#считывание данных
file = open('space.csv', encoding='utf8')
ans = list(csv.reader(file, delimiter=',', quotechar='"'))[1:]
file.close()

#поиск расстояния до Земли данного корабля
a = input()
while a != 'stop':
    f = 1
    for i in ans:
        if i[0] == a:
            coord_x = int(i[2].split(' ')[0])
            coord_y = int(i[2].split(' ')[1])
            p = (((coord_x - 0)**2) + ((coord_y - 0)**2))**(0.5)
            print(f'Корабль {i[0]} последний раз был на связи по координатам: {i[2]}, что составляет: {round(p, 3)} космических единиц.')
            f = 0
            break
    if f:
        print('error.. er.. ror..')
    a = input()