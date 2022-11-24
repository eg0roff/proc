import punc_marks
def sort(container):
    razmernost=0
    for i in range(len(container)):
        if container[i] == "":
            razmernost = i
            break

    for i in range(0,razmernost-1):
        for j in range(0,razmernost - i -1):
            if punc_marks.count_for_sort(container,j)<punc_marks.count_for_sort(container,j+1):
                container[j],container[j+1]=container[j+1],container[j]