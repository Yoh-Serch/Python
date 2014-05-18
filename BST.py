class Nodo:
    parent = None
    valor = None
    izq = None
    der = None
    
    def __init__(self, valor):
        self.valor = valor
        
    def __str__(self):
        return str(self.valor)
    
    
class BST:
    raiz = None
    
    def __init__(self):
        pass
    
    
    def insertar(self, valor):
        n = Nodo(valor)
        if self.raiz == None:
            self.raiz = n
        else:
            temporal = self.raiz
            while temporal != None:
                n.p = temporal
                if n.valor >= temporal.valor:
                    temporal = temporal.der
                else:
                    temporal = temporal.izq
            
            if n.valor < n.p.valor:
                n.p.izq = n
            else:
                n.p.der = n
                
    
    def inorden(self,nodo):
        if nodo != None:
            self.inorden(nodo.izq)
            print(nodo.valor)
            self.inorden(nodo.der)
    
    
    def preorden(self,nodo):
        if nodo != None:
            print(nodo.valor)
            self.preorden(nodo.izq)
            self.preorden(nodo.der)
            
            
    def postorden(self,nodo):
        if nodo != None:
            self.postorden(nodo.izq)
            self.postorden(nodo.der)
            print(nodo.valor)
            

if __name__ == "__main__":
    #Prueba de escritorio
    arbol = BST() 
    arbol.insertar(7)
    arbol.insertar(2)
    arbol.insertar(5)
    arbol.insertar(2)
    arbol.insertar(6)
    arbol.insertar(9)
    arbol.insertar(5)
    arbol.insertar(11)
    arbol.insertar(4)
    arbol.insertar(10)
    arbol.insertar(11)
    print("Imprimiendo en orden")
    arbol.inorden(arbol.raiz)
    print("Imprimiendo en pre-orden")
    arbol.preorden(arbol.raiz)
    print("Imprimiendo en post-orden")
    arbol.postorden(arbol.raiz)
    