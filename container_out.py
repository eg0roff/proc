import output_shape


def print_container(container, filename='out.txt'):
    filled_container_parts = 0
    for i in range(len(container)):
        if container[i] == "":
            with open(filename, "a", encoding='utf-8') as fileout:
                fileout.write(f'\n\nКонтейнер содержит {i} элементов:')
                filled_container_parts = i
            break

    with open(filename, "a", encoding='utf-8') as fileout:
        if filled_container_parts != 0:
            for j in range(0, filled_container_parts):
                output_shape.out_shape(container, j, filename)

        elif filled_container_parts == 0:
            fileout.write(f'\n\nКонтейнер содержит {filled_container_parts} элементов:')
            fileout.write(f'\nКонтейнер очень пуст')
    return container


def print_filtered_container(container, label, filename='out.txt'):
    filled_container_parts = 0
    for i in range(len(container)):
        if container[i] == "":
            with open(filename, "a", encoding='utf-8') as fileout:
                fileout.write(f'\nНачинаю сортировку по фильтру {label}')
                filled_container_parts = i
            break

    with open(filename, "a", encoding='utf-8'):
        if filled_container_parts != 0:
            for j in range(0, filled_container_parts):
                output_shape.filtered_shape(container, j, label, filename)
