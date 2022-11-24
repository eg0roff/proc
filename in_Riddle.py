import class_construct
def riddle_in(container,i,part):
    container[i] = class_construct.riddles()
    container[i].index = part[0]
    container[i].answer = part[1]
    container[i].content = part[2]
    container[i].mark=part[3]