
def print_punc_marks_count(container):
    punc_marks='"",.;:!?\/-'
    for i in range(len(container)):
        if container[i] == "":
            razmernost = i
            break
    with open("out.txt", "a", encoding='utf-8') as fout:
        for i in range(0, razmernost):
            punc_count = 0
            for mark in punc_marks:
                str=container[i].content
                for j in range (len(str)):
                    if str[j].find(mark)!=-1:
                        punc_count+=1

            fout.write(f'\nВ строке {i}, содержится {punc_count} знаков препинания')


def count_for_sort(container1,i):
    punc_count = 0
    punc_marks = '"",.;:!?\/-'
    for mark in punc_marks:
        str = container1[i].content
        for j in range(len(str)):
            if str[j].find(mark) != -1:
                punc_count += 1

    return punc_count