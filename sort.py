import punc_marks


def sort(container):
    filled_container_parts = 0
    for i in range(len(container)):
        if container[i] == "":
            filled_container_parts = i
            break

    for i in range(0, filled_container_parts - 1):
        for j in range(0, filled_container_parts - i - 1):
            if punc_marks.count_for_sort(container, j) < punc_marks.count_for_sort(container, j+1):
                container[j], container[j+1] = container[j+1], container[j]
