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
    
    def recorrer(self,Ydimension):
        aux=self.First
        impresion=""
        while aux:
            print(aux.nombre)
            nodo=aux.Nodo1
            while nodo:
                print(str(nodo.Id)+".\tgas:"+str(nodo.Value)+"  x:"+str(nodo.X)+"   y:"+str(nodo.Y))
                nodo=nodo.Next
            nodo=aux.Nodo1
            print(" ")
            print("Mapa de nodos para: "+aux.nombre)
            """while nodo:
                impresion+="["+str(nodo.Value)+"] "
                if nodo.Id%int(aux.Ydimension)==0:
                    impresion+="\n"
                nodo=nodo.Next
            """
            nodo=aux.Nodo1
            while nodo.Abajo:
                impresion+="["+str(nodo.Value)+"] "
                nodo=nodo.Abajo
                cod=int(nodo.Y)
                if nodo.X==aux.Xdimension:
                    impresion+="["+str(nodo.Value)+"]\n"
                    if nodo.Y<aux.Ydimension:
                        nodo=aux.Nodo1
                        while int(cod)>int(0):
                            nodo=nodo.Next
                            cod-=int(1)

            print(impresion)
            impresion=""
            print("--------------------------------------")
            print(" ")
            aux=aux.Next
        

    def BuscarInicio(self,nombre):
        aux=self.First
        while aux.nombre!=nombre:
            aux=aux.Next
        Actual=aux.Nodo1

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
        print("Posicion Inicio:\t"+ Actual.X+" - "+Actual.Y)
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
        
        print("Posicion Final:\t"+ Actual.X+" - "+Actual.Y)
        print("Mapa de la Ruta elegida para: "+aux.nombre)
        Actual=aux.Nodo1
        impresion=""
        while Actual.Abajo:
            if Actual.Camino==True:
                impresion+="[1] "
            else:
                impresion+="[0] "
            Actual=Actual.Abajo
            cod=int(Actual.Y)
            if Actual.X==aux.Xdimension:
                if Actual.Camino==True:
                    impresion+="[1]\n"
                else:
                    impresion+="[0]\n"
                if Actual.Y<aux.Ydimension:
                    Actual=aux.Nodo1
                    while int(cod)>int(0):
                        Actual=Actual.Next
                        cod-=int(1)
        print(impresion)
        impresion=""

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
            try:
                arbol.write(aux.nombre+".xml")
                print("ARCHIVO XML GENERADO")
            except IOError as exc:
                print(exc)

        else:
            print("No ha seleccionado un terreno analizado...")
            
            
    def Grafico(self):
        
        cod=int(0)
        aux=self.First
        print("Elija una de los siguientes terrenos:")
        while aux:
            if aux.Analizado==True:
                print("1."+aux.nombre)
            aux=aux.Next
        nombre=input("Ingrese el nombre del terreno:\n")

        aux=self.First
        while aux.nombre!=nombre:
            aux=aux.Next
        archivo=open(aux.nombre+".dot","w")
        archivo.write("digraph "+aux.nombre+"{\n")
        Actual=aux.Nodo1
        while Actual:
            if Actual.Camino==True:
                archivo.write(str(Actual.Id)+"[color=blue label="+str(Actual.Value)+"]\n")
            else:
                archivo.write(str(Actual.Id)+"[label="+str(Actual.Value)+"]\n")
            Actual=Actual.Next
        Actual=aux.Nodo1
        """while Actual.Abajo!=None:
            archivo.write(str(Actual.Id)+"->"+str(Actual.Abajo.Id)+"[arrowhead = none]\n")
            #[arrowhead = none]
            Actual=Actual.Abajo
            cod=int(Actual.Y)
            if Actual.X==aux.Xdimension and Actual.Y<aux.Ydimension:
                Actual=aux.Nodo1
                while int(cod)>int(0):
                    Actual=Actual.Next
                    cod-=int(1)
        Actual=aux.Nodo1"""
        while Actual.Abajo!=None:
            archivo.write("rank = same{"+str(Actual.Id)+"->"+str(Actual.Abajo.Id)+"[arrowhead = none]}\n")
            #[arrowhead = none]
            Actual=Actual.Abajo
            cod=int(Actual.Y)
            if Actual.X==aux.Xdimension and Actual.Y<aux.Ydimension:
                Actual=aux.Nodo1
                while int(cod)>int(0):
                    Actual=Actual.Next
                    cod-=int(1)
        Actual=aux.Nodo1
        while Actual:
            if Actual.Y<aux.Ydimension:
                archivo.write(str(Actual.Id)+"->"+str(Actual.Next.Id)+"[arrowhead = none]\n")
            Actual=Actual.Next
        
        """while Actual:
            if Actual.Y<aux.Ydimension:
                archivo.write("rank = same{"+str(Actual.Id)+"->"+str(Actual.Next.Id)+"[arrowhead = none]}\n")
            Actual=Actual.Next
        """         


        archivo.write("}")
        archivo.close()
        #os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng '+aux.nombre+'.dot -o '+aux.nombre+'.png')
        print("Grafico generado :)")

        
    #def Valuar
    def recorrerFin(self):
        aux=self.Ultimo
        while aux:
            print(aux.Value)
            aux=aux.Anterior
    