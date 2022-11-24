from cont_construct import container_construct
from container_in import *
from container_out import *
from sort import sort
from container_clean import container_delete

def test_container_constructor():
    assert len(container_construct())==100

def test_container_in():
    container=container_construct()
    assert container_filling(container, 'cont_in_1.txt')==3
    assert container_filling(container, 'cont_in_2.txt')==100

def test_container_out():
    container=container_construct()
    container_filling(container, 'cont_in_1.txt')
    print_container(container,'test_container_out.txt')
    flag=open(r'D:\pythonProject\timp\labMudrostProc\test_container_out.txt', encoding='utf-8').read() == open(
        r'D:\pythonProject\timp\labMudrostProc\standart_container_out.txt', encoding='utf-8').read()
    assert flag==True


def test_sort():
    container=container_construct()
    container_filling(container, 'in_test_sort_function.txt')
    sort(container)
    print_container(container, 'test_sort_out.txt')
    flag = open(r'D:\pythonProject\timp\labMudrostProc\test_sort_out.txt', encoding='utf-8').read() == open(
        r'D:\pythonProject\timp\labMudrostProc\standart_test_sort_out.txt', encoding='utf-8').read()
    assert flag == True


def test_filtered_output():
    container = container_construct()
    container_filling(container, 'in_test_filter.txt')
    print_filtered_container(container,'0','test_filtered_output.txt')
    flag = open(r'D:\pythonProject\timp\labMudrostProc\test_filtered_output.txt', encoding='utf-8').read() == open(
        r'D:\pythonProject\timp\labMudrostProc\standart_filtered_output.txt', encoding='utf-8').read()
    assert flag == True


def test_container_clean():
    container=container_construct()
    container_filling(container, 'in_test_filter.txt')
    container_delete(container)
    print_container(container,'test_delete.txt')
    flag = open(r'D:\pythonProject\timp\labMudrostProc\test_delete.txt', encoding='utf-8').read() == open(
        r'D:\pythonProject\timp\labMudrostProc\standart_test_delete.txt', encoding='utf-8').read()
    assert flag == True


