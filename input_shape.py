import in_Aforizm
import in_Quot
import in_Riddle

def fill_container(container,i,part):
    if part[0] == '0':
        in_Aforizm.aforizm_in(container,i,part)

        i += 1
    elif part[0] == '1':
        in_Quot.qout_in(container,i,part)
        i += 1

    elif part[0]=='2':
        in_Riddle.riddle_in(container,i,part)
        i+=1