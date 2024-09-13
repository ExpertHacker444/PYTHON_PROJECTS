class A:
    def hablar(self):
        print("hola desde A")

class B(A):
    def hablar(self):
        print("hola desde B")

class C(A):
    def hablar(self):
        print("hola desde C")

class D(B,C):
    def hablar(self):
        print("hola desde D")

d = D() #le da prioridad a la clase D de hablar, por que hacemos el llamado a la misma

d.hablar()

#se puede llamar a una clase distinta de D

p = C()

B.hablar(p)

#muestra ña jerarquia de las clases
print(D.mro())