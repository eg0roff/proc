import punc_marks
def sort(container):
    for i in range(len(container)):
        if container[i] == "":
            razmernost = i
            break

    for i in range(razmernost - 1):
        for j in range(razmernost - i - 1):
            if punc_marks.count_for_sort(container[i])>punc_marks.count_for_sort(container[j]):
                container[i],container[j]=container[j],container[i]