class A:
    def hablar(self):
        print('Hola desde A')

class F:
    def hablar(self):
        print('Hola desde F')

class B(A):
    def hablar(self): 
        print('Hola desde B')

class C(F):
    def hablar(self):
        print('Hola desde C')

class D(B,C):
    def hablar(self):
        print('Hola desde D')

d = D()

#utiliza la funcion que corresponda jerarquicamente
d.hablar()

#utilizando la funcion que yo elija (B)
B.hablar(d)

#muestar la jerarquia
print(D.mro())