import out_Aforizm
import out_quotation
import out_riddles


def out_shape(container, j, filename):
    if container[j].index == '0':
        class_type = 'цитата'
        out_Aforizm.out_aforizm(container, j, class_type, filename)

    elif container[j].index == '1':
        class_type = 'афоризм'
        out_quotation.out_quot(container, j, class_type, filename)

    elif container[j].index == '2':
        class_type = 'загадка'
        out_riddles.out_riddle(container, j, class_type, filename)


def filtered_shape(container, j, label, filename):
    if label == '0':
        if container[j].index == '0':
            class_type = 'цитата'
            out_Aforizm.out_aforizm(container, j, class_type, filename)

    elif label == '1':
        if container[j].index == '1':
            class_type = 'афоризм'
            out_quotation.out_quot(container, j, class_type, filename)
