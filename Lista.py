from Nodo import Nodos
class Listas:
    def __init__(self):
        self.First=None
        self.Size=0
    def Append(self, Value):
        NewNodo=Nodos(Value)
        if self.Size==0:
            self.First=NewNodo
        else:
            ActaulNodo=self.First
            while ActaulNodo.Next!=None:
                ActaulNodo=ActaulNodo.Next
            ActaulNodo.Next=NewNodo

        self.Size+=1
        return NewNodo
    def Remove(self, value):
        if self.Size==0:
            return False
        else:
            ActualNodo=self.First
            while ActualNodo.Value!=value:
                if ActualNodo.Next==None:
                    return False
                else:
                    ActualNodo=ActualNodo.Next
            EliminNodo=ActualNodo.Next
            ActualNodo.Next=EliminNodo.Next
            self.Size-=1
            return EliminNodo

    def __len__(self):
        return self.Size
    
    def __str__(self):
        cadena ="["
        ActualNodo=self.First
        while ActualNodo!=None:
            cadena+=str(ActualNodo)
            if ActualNodo.Next!=None:
                cadena+=str(",")
            ActualNodo=ActualNodo.Next
        cadena+="]"
        return cadena
