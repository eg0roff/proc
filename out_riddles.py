import punc_marks
def out_riddle(container,j,type):
    with open("out.txt", "a", encoding='utf-8') as fout:
        fout.write(f'\n{j}: Это {type}: {container[j].content} - {container[j].answer} Субъективная оценка данного изречения = {container[j].mark}. А знаков припинания тут {punc_marks.count_for_sort(container,j)}')