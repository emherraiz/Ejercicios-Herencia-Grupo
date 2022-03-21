class A(object):
    def __init__(self,a):
        self.a = a
    @staticmethod
    def quienEs():
        return "Es A"

class B(A):

    def __init__(self,a, b):
        A.__init__(self,a)
        self.b = b
    @staticmethod
    def quienEs():
        return "Es B"

class C(A):

    def __init__(self,a,c):
        A.__init__(self,a)
        self.c = c
    @staticmethod
    def quienEs():
        return "Es C"

class D(B,C):
    def __init__(self,a,b,c,d):
        B.__init__(self,a,b)
        C.__init__(self,a,c)
        self.d = d
    @staticmethod
    def quienEs():
        return "Es D"

if __name__ == '__main__':
    ca = A("prueba de A")
    cb = B("prueba de B a A","prueba de B")
    cc = C("prueba de C a A","prueba de C")
    cd = D("prueba de D a A","prueba de D a B","prueba de D a C","prueba de D")
  
    print (ca.a)
    print (ca.quienEs())
    print (cb.b)
    print(cb.a)
    print (cb.quienEs())
    print (cc.c)
    print (cc.a)
    print (cc.quienEs())
    print (cd.d)
    print (cd.b)
    print (cd.c)
    print (cd.a)
    print(cd.quienEs())