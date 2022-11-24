import cont_construct
import container_in
import container_out
import container_clean
import sort

container=cont_construct.container_construct()
flag=container_in.container_filling(container, 'in_5.txt')
if flag[1]==0:
    container_out.print_container(container)
    #punc_marks.print_punc_marks_count(container)
    sort.sort(container)
    container_out.print_container(container)
    container_out.print_filtered_container(container,'0')
    container_clean.container_delete(container)
    container_out.print_container(container)
