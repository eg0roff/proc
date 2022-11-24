import out_Aforizm
import out_quotation
import out_riddles

def out_shape(container, j,filename):
    if container[j].index=='0':
        type='цитата'
        out_Aforizm.out_aforizm(container,j,type,filename)

    elif container[j].index=='1':
        type ='афоризм'
        out_quotation.out_quot(container,j,type,filename)


    elif container[j].index=='2':
        type ='загадка'
        out_riddles.out_riddle(container,j,type,filename)


def filtered_shape(container,j,label,filename):
    if label == '0':
        if container[j].index == '0':
            type = 'цитата'
            out_Aforizm.out_aforizm(container, j, type, filename)


    elif label== '1':
        if container[j].index == '1':
            type = 'афоризм'
            out_quotation.out_quot(container, j, type, filename)

