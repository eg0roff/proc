def out_riddle(container,j,type):
    with open("out.txt", "a", encoding='utf-8') as fout:
        fout.write(f'\n{j}: Это {type}: {container[j].content} - {container[j].answer}')