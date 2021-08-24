from Nodo import Nodos
from Nodo import NodoTerreno
import os,sys
import xml.etree.cElementTree as ET
class Listas:
    def __init__(self):
        self.First=None
        self.Ultimo=None
        self.Size=0

    def AñadirTerreno(self,nombre,Xdimension,Ydimension,Xinicio,Yinicio,XFinal,YFinal):
        NewNodo=NodoTerreno(nombre,Xdimension,Ydimension,Xinicio,Yinicio,XFinal,YFinal)
        if self.Size==0:
            self.First=NewNodo
            self.Ultimo=NewNodo
        else:
            ActaulNodo=self.First
            while ActaulNodo.Next!=None:
                ActaulNodo=ActaulNodo.Next
            ActaulNodo.Next=NewNodo
            self.Ultimo=NewNodo
        self.Size+=1
        return NewNodo

    def RecorrerTerreno(self,nombre):
        aux=self.First
        while aux.nombre!=nombre:
            aux=aux.Next
        return aux


    def AñadirPosiciones(self,nombre,Value,x,y,c,DimX):
        aux=self.First
        while aux.nombre!=nombre:
            aux=aux.Next
        
        NewNodo=Nodos(Value,x,y,c)
        if aux.Nodo1==None:
            aux.Nodo1=NewNodo
        else:
            ActaulNodo=aux.Nodo1
            while ActaulNodo.Next!=None:
                ActaulNodo=ActaulNodo.Next
            ActaulNodo.Next=NewNodo
            ActaulNodo.Sig=NewNodo
            NewNodo.Anterior=ActaulNodo
            print(str(NewNodo.Anterior.Id)+" es anterior de "+str(NewNodo.Id))
            if NewNodo.Id==(int(DimX)+1):

                ActaulNodo.Sig=None
            if NewNodo.Id>int(DimX):
                ActaulNodo=aux.Nodo1
                while ActaulNodo.Id!=(int(NewNodo.Id)-int(DimX)):
                    ActaulNodo=ActaulNodo.Next
                NewNodo.Arriba=ActaulNodo
                ActaulNodo.Abajo=NewNodo
                
        return NewNodo

    def __len__(self):
        return self.Size
    
    def __str__(self):
        cadena ="["
        ActualNodo=self.First
        while ActualNodo!=None:
            cadena+=str(ActualNodo.Value)
            if ActualNodo.Next!=None:
                cadena+=str(",")
            ActualNodo=ActualNodo.Next
        cadena+="]"
        return cadena
    
    def recorrer(self):
        aux=self.First
        while aux:
            print(aux.nombre)
            nodo=aux.Nodo1
            while nodo:
                print(str(nodo.Id)+".\tgas:"+str(nodo.Value)+"  x:"+str(nodo.X)+"   y:"+str(nodo.Y))
                nodo=nodo.Next
            print("--------------------------------------")
            aux=aux.Next
        

    def BuscarInicio(self,nombre):
        aux=self.First
        while aux.nombre!=nombre:
            aux=aux.Next
        Actual=aux.Nodo1
        print(aux.YInicio)
        print(aux.Xinicio)
        aux.Analizado=True
        if Actual.X<aux.YInicio:
            while Actual.X!=aux.Xinicio or Actual.Y!=aux.YInicio:
                Actual=Actual.Next
        elif Actual.X>aux.YInicio:
            while Actual.X!=aux.Xinicio or Actual.Y!=aux.YInicio:
                Actual=Actual.Anterior
        else:
            if Actual.Y>aux.Xinicio:
                while Actual.X!=aux.Xinicio or Actual.Y!=aux.YInicio:
                    Actual=Actual.Anterior
            else:
                while Actual.X!=aux.Xinicio or Actual.Y!=aux.YInicio:
                    Actual=Actual.Next
        #Recorrido de izquierda-Arriba hacia Abajo-Derecha
        print("Empece en: "+ Actual.X+" - "+Actual.Y)
        Actual.Camino=True
        aux.combustible+=Actual.Value
        if Actual.Y<aux.Yfinal and (Actual.X<aux.Xfinal):
            while (Actual.Y!=aux.Yfinal) and (Actual.X!=aux.Xfinal):
                
                if Actual.Abajo.Value<=Actual.Sig.Value:
                    Actual=Actual.Abajo
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
                else:
                    Actual=Actual.Sig
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
            if Actual.Y==aux.Yfinal:
                while Actual.X!=aux.Xfinal:
                    Actual=Actual.Abajo
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
            elif Actual.X==aux.Xfinal:
                while Actual.Y!=aux.Yfinal:
                    Actual=Actual.Sig
                    Actual.Camino=True
                    aux.combustible+=Actual.Value

        #Recorrido de Abajo-Izquierda hacia Arriba-Derecha
        elif (Actual.Y<aux.Yfinal) and (Actual.X>aux.Xfinal):
            while (Actual.Y!=aux.Yfinal) and (Actual.X!=aux.Xfinal):
                if Actual.Arriba.Value<=Actual.Sig.Value:
                    Actual=Actual.Arriba
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
                else:
                    Actual=Actual.Sig
                    Actual.Camino=True
                    aux.combustible+=Actual.Value

            if Actual.Y==aux.Yfinal:
                while Actual.X!=aux.Xfinal:
                    Actual=Actual.Arriba
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
            elif Actual.X==aux.Xfinal:
                while Actual.Y!=aux.Yfinal:
                    Actual=Actual.Sig
                    Actual.Camino=True
                    aux.combustible+=Actual.Value

        #Recorrido de Derecha-Abajo hacia Arriba-Izquierda
        elif Actual.Y>aux.Yfinal and (Actual.X>aux.Xfinal):
            while (Actual.Y!=aux.Yfinal) and (Actual.X!=aux.Xfinal):
                
                if Actual.Arriba.Value<=Actual.Anterior.Value:
                    Actual=Actual.Arriba
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
                else:
                    Actual=Actual.Anterior
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
            if Actual.Y==aux.Yfinal:
                while Actual.X!=aux.Xfinal:
                    Actual=Actual.Arriba
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
            elif Actual.X==aux.Xfinal:
                while Actual.Y!=aux.Yfinal:
                    Actual=Actual.Anterior
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
                    
        #Recorrido de Derecha-Arriba hacia Izquierda-abajo
        elif (Actual.Y>aux.Yfinal) and (Actual.X<aux.Xfinal):
            while (Actual.Y!=aux.Yfinal) and (Actual.X!=aux.Xfinal):
                print("Estoy en: "+ Actual.X+" - "+Actual.Y)
                if Actual.Abajo.Value<=Actual.Anterior.Value:
                    Actual=Actual.Abajo
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
                else:
                    Actual=Actual.Anterior
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
            if Actual.Y==aux.Yfinal:
                while Actual.X!=aux.Xfinal:
                    Actual=Actual.Abajo
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
            elif Actual.X==aux.Xfinal:
                while Actual.Y!=aux.Yfinal:
                    Actual=Actual.Anterior
                    Actual.Camino=True
                    aux.combustible+=Actual.Value


        elif (Actual.X!=aux.Yfinal) or (Actual.Y==aux.Yfinal):
            if Actual.X>aux.Xfinal:
                while Actual.X!=aux.Xfinal:
                    Actual=Actual.Abajo
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
            elif Actual.X<aux.Xfinal:
                while Actual.X!=aux.Xfinal:
                    Actual=Actual.Arriba
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
        elif (Actual.X==aux.Xfinal) or (Actual.Y!=aux.Yfinal):
            if Actual.Y>aux.Yfinal:
                while Actual.Y!=aux.Yfinal:
                    Actual=Actual.Anterior
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
            elif Actual.Y<aux.Yfinal:
                while Actual.Y!=aux.Yfinal:
                    Actual=Actual.Next
                    Actual.Camino=True
                    aux.combustible+=Actual.Value
        
        print("Estoy en: "+ Actual.X+" - "+Actual.Y)
        Actual=aux.Nodo1
        impresion=""
        while Actual:
            if Actual.Camino==True:
                impresion+="[1] "
            else:
                impresion+="[0] "
            if Actual.Id%int(aux.Ydimension)==0:
                impresion+="\n"
            Actual=Actual.Next
        print(impresion)

    def imprimirXML(self, nombre):
        aux=self.First
        while aux.nombre!=nombre:
            aux=aux.Next
        if aux.Analizado==True:
            ruut=ET.Element("terreno ",name=nombre)
            posicionIni=ET.SubElement(ruut,"posicioninicio")
            ET.SubElement(posicionIni,"x").text=str(aux.Xinicio)
            ET.SubElement(posicionIni,"y").text=str(aux.YInicio)
            posicionFin=ET.SubElement(ruut,"posicionfinal")
            ET.SubElement(posicionFin,"x").text=str(aux.Xfinal)
            ET.SubElement(posicionFin,"y").text=str(aux.Yfinal)
            gas=ET.SubElement(ruut,"gasolina")
            gas.text=str(aux.combustible)
            Actual=aux.Nodo1
            while Actual:
                if Actual.Camino==True:
                    nodo1=ET.SubElement(ruut,"posicion",x=str(Actual.X),y=str(Actual.Y))
                    nodo1.text=str(Actual.Value)
                Actual=Actual.Next
            arbol=ET.ElementTree(ruut)
            ruta=input("Ingrese la ruta:")            
            try:
                arbol.write(ruta)
            except IOError as exc:
                print(exc)
        else:
            print("No ha seleccionado un terreno analizado...")
            
            
    def Grafico(self,nombre):
        aux=self.First
        while aux.nombre!=nombre:
            aux=aux.Next
        archivo=open("C:/Users/justin/Desktop/USAC/Semestre 2 2021/IPC 2/Lab/IPC2_Proyecto1_202003734/IPC2_Proyecto1_202004734/"+aux.nombre+".dot","w")
        archivo.write("digraph "+aux.nombre+"{\n")
        Actual=aux.Nodo1
        while Actual:
            if Actual.Camino==True:
                archivo.write(str(Actual.Id)+"[color=blue label="+str(Actual.Value)+"]\n")
            else:
                archivo.write(str(Actual.Id)+"[label="+str(Actual.Value)+"]\n")
            Actual=Actual.Next
        archivo.write("}")
        archivo.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng terreno1.dot -o salida.png')

        
    #def Valuar
    def recorrerFin(self):
        aux=self.Ultimo
        while aux:
            print(aux.Value)
            aux=aux.Anterior
    