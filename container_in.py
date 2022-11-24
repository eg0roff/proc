import input_shape

def container_filling(container, filename="in.txt"):
    i=0
    with open(filename, "r", encoding='utf-8') as fin:
        with open("out.txt", "w", encoding='utf-8') as fout:
            for line in fin.readlines():
                if i==100:
                    break
                else:
                    part=line.split("|")

                    input_shape.fill_container(container,i,part)
                    i=i+1
            fout.write('Контейнер заполнен')

    return i