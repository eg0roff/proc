import punc_marks
def out_quot(container,j,type):
    with open("out.txt", "a", encoding='utf-8') as fout:
        fout.write(f'\n{j}: Это {type}: {container[j].name} - {container[j].content} Субъективная оценка данного изречения = {container[j].mark}. А знаков припинания тут {punc_marks.count_for_sort(container,j)}')