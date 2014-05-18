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