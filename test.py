
class A():
    aa=1
    aaa=2

class B():
    aa=3
    aaa=4

cont=['']*4
print(cont)
cont[0]=A()
cont[1]=B()
print(cont[0].aa,cont[1].aa)
temp=cont[0]
cont[0]=cont[1]
cont[1]=temp
print(cont[0].aa,cont[1].aa)

