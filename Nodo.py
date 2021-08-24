class Nodos:
    def __init__(self, Value,X,Y,Id):
        self.Value=int(Value)
        self.Id=Id
        self.X=X
        self.Y=Y
        self.Next=None
        self.Sig=None
        self.Anterior=None
        self.Arriba=None
        self.Abajo=None
        self.Camino=False #Pertenece o no pertenece al camino 
    def __str__(self):
        return str(self.Value)

class NodoTerreno:
    def __init__(self, nombre,Xdimension,Ydimension,Xinicio,Yinicio,XFinal,YFinal):
        self.nombre=nombre
        self.Xdimension=Xdimension
        self.Ydimension=Ydimension
        self.Xinicio=Xinicio
        self.Xfinal=XFinal
        self.YInicio=Yinicio
        self.Yfinal=YFinal
        self.Analizado=False
        self.combustible=int(0)
        self.Next=None
        self.Nodo1=None

    