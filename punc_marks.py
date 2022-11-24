def print_punc_marks_count(container):
    filled_container_parts = 0
    punctuation_marks = '"",.;:!?/-'
    for i in range(len(container)):
        if container[i] == "":
            filled_container_parts = i
            break

    with open("out.txt", "a", encoding='utf-8') as fout:
        for i in range(0, filled_container_parts):
            punctuation_signs_count = 0
            for mark in punctuation_marks:
                temp_str = container[i].content
                for j in range(len(temp_str)):
                    if temp_str[j].find(mark) != -1:
                        punctuation_signs_count += 1

            fout.write(f'\nВ строке {i}, содержится {punctuation_signs_count} знаков препинания')


def count_for_sort(container1, i):
    punctuation_signs_count = 0
    punctuation_marks = '"",.;:!?/-'
    for mark in punctuation_marks:
        temp_str = container1[i].content
        for j in range(len(temp_str)):
            if temp_str[j].find(mark) != -1:
                punctuation_signs_count += 1

    return punctuation_signs_count
