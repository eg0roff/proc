import cont_construct
import container_in
import container_out
import container_clean
import sort
import multimethod

container = cont_construct.container_construct()
flag = container_in.container_filling(container)
multimethod.multik(container)

if flag[1] == 0:
    container_out.print_container(container)
    sort.sort(container)
    container_out.print_container(container)
    container_out.print_filtered_container(container, '0')
    container_clean.container_delete(container)
    container_out.print_container(container)
