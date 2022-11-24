import punc_marks
def out_aforizm(container,j,type, filename='out.txt'):
    with open(filename, "a", encoding='utf-8') as fout:
        fout.write(f'\n{j}: Это {type}: {container[j].country} - {container[j].content} Субъективная оценка данного изречения = {container[j].mark}. А знаков припинания тут {punc_marks.count_for_sort(container,j)}')