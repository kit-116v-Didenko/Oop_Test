

def vlogen(cla, count):
    print('.'*count,cla.__name__)

    for clsa in cla.__bases__:
        vlogen(clsa,count+3)

def instance(inst):
    print('Ren off',inst)
    vlogen(inst.__class__,3)


if __name__ == "__main__":
    class A:
        pass
    class B(A):
        pass
    class D(B,A):
        pass

    #logen(A().__class__,3)
    #instance(D())
    #print(list(A().__class__.__bases__).__class__.__name__)
    #print(A().__class__.__bases__.__class__ !=True)

    instance(D())

    