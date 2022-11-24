import out_Aforizm
import out_quotation
import out_riddles

def out_shape(container, j):
    if container[j].index=='0':
        type='цитата'
        out_Aforizm.out_aforizm(container,j,type)

    elif container[j].index=='1':
        type ='афоризм'
        out_quotation.out_quot(container,j,type)

    elif container[j].index=='2':
        type ='загадка'
        out_riddles.out_riddle(container,j,type)