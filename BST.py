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