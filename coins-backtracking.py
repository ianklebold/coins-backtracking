from random import randint

class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato
 
def insertar(raiz, nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None:
                raiz.derecha = nodo
                
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.dato > nodo.dato:
                if raiz.izquierda is None:
                    raiz.izquierda = nodo
                   
                else:
                    insertar(raiz.izquierda, nodo)
            else:
                print("Lo sentimos no se permiten valores iguales : " + str(nodo.dato))

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.dato)
        inorden(raiz.derecha)

def eliminacion(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        inorden(raiz.derecha)
        del raiz

def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izquierda)
        postorden(raiz.derecha)
        print(raiz.dato)

#Lo que pasamos es una lista, la cual es mutable
#Su funcion será permitirle al jugador y a la computadora elegir los elementos del arbol
#Los valores guardados en el arbol no se repiten y la idea es siempre mandar una cantidad par
lista = []
cont = 0
while(cont <= 100):
    valor = randint(1,1000)
    if(len(lista) == 0):
        lista.append(valor)
        cont = cont + 1
    else:
        if(valor not in lista):
            lista.append(valor)
            cont = cont + 1 

raiz = Nodo(lista[0]) #Gurdamos primer elemento

#Recorremos la lista y vamos guardando el arbol
for index in range(1,len(lista)):
    insertar(raiz, Nodo(lista[index]))



