import input_shape


def container_filling(container, filename="in.txt"):
    flag = 0
    i = 0
    try:
        with open(filename, "r", encoding='utf-8') as fin:
            with open("out.txt", "w", encoding='utf-8') as fout:
                for line in fin.readlines():
                    if i == 100:
                        break
                    else:
                        part = line.split("|")
                        if len(part) == 4:
                            if (part[0] == '1') | (part[0] == '0') | (part[0] == '2'):
                                if ((part[3] == '0\n') | (part[3] == '1\n') | (part[3] == '2\n') |
                                        (part[3] == '3\n') | (part[3] == '4\n') | (part[3] == '5\n') |
                                        (part[3] == '6\n') | (part[3] == '7\n') | (part[3] == '8\n') |
                                        (part[3] == '9\n') | (part[3] == '10\n')):
                                    input_shape.fill_container(container, i, part)
                                    i = i+1
                                else:
                                    flag = 1
                                    print('неверная субъективная оценка')
                            else:
                                flag = 1
                                print('неверная типизация')
                        else:
                            flag = 1
                            print('неверное количество ключевых моментов')
                fout.write('Контейнер заполнен')
    except FileNotFoundError:
        flag = 1
        print('такого файла не существует!')
    if i == 0:
        flag = 1
        print('файл пустой')
    return i, flag
