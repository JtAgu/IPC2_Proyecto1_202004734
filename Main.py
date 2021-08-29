from Nodo import NodoTerreno
from Lista import Listas
from xml.dom import minidom
import xml.etree.ElementTree as ET


def imprimir():
    print("\n")
    print("=========================================")
    print("             MENÚ PRINCIPAL")
    print("=========================================")
    print("\nElija una de las siguientes opciones:")
    print("1. Cargar archivo")
    print("2. Procesar")
    print("3. Escribir salida")
    print("4. Mostrar Datos Estudiante")
    print("5. Generar Grafica")
    print("6. salir\n")
Lista=Listas()
def Leer(ruta):
    #C:\Users\justin\Desktop\USAC\Semestre 2 2021\IPC 2\Lab\IPC2_Proyecto1_202003734\prueba.xml
    #C:/Users/justin/Desktop/USAC/Semestre 2 2021/IPC 2/Lab/IPC2_Proyecto1_202003734/IPC2_Proyecto1_202004734/salida.xml
    #C:\Users\justin\Desktop\USAC\Semestre 2 2021\IPC 2\Lab\IPC2_Proyecto1_202003734\IPC2_Proyecto1_202004734\prueba1.xml
    mytree = ET.parse(ruta)
    myroot = mytree.getroot()
    
    for x in myroot.findall('terreno'):

        
        Lista.AñadirTerreno(x.attrib["nombre"], x[0][0].text, x[0][1].text, x[1][0].text, x[1][1].text, x[2][0].text, x[2][1].text)
        c=int(1)
        for terreno in x.findall('posicion'):
            equis=str(terreno.attrib["x"])
            yes=str(terreno.attrib["y"])
            gas=terreno.text
            Lista.AñadirPosiciones(x.attrib["nombre"],gas,equis,yes,c,x[0][1].text)
            c+=1

    Lista.recorrer(x[0][1])
    return myroot

def procesar(myroot):
    aux=Lista.First
    print("Lista de terrenos")
    while aux:
        print("1."+aux.nombre)
        aux=aux.Next
    nombre=input("Escribe el nombre del terreno a procesar:\n")
    for x in myroot.findall('terreno'):
        if str(x.attrib["nombre"])==nombre:
            Lista.BuscarInicio(nombre)

def Xml(myroot):
    aux=Lista.First
    print("Lista de terrenos procesados")
    while aux:
        if aux.Analizado:
            print("1."+aux.nombre)
        aux=aux.Next
    nombre=input("Escribe el nombre del terreno a procesar:\n")
    for x in myroot.findall('terreno'):
        if str(x.attrib["nombre"])==nombre:
            Lista.imprimirXML(nombre)
            break


if __name__ == '__main__':    
    
    opcion=""
    codigo=""
    arbol=""
    while opcion !=6:
        imprimir()
        opcion=input()
        if opcion=="1":
            ruta =input("Ingresa la ruta del archivo:")
            arbol=Leer(ruta)
        elif opcion=="2":
            procesar(arbol)
        elif opcion=="3":
            Xml(arbol)
        elif opcion=="5":
            
            Lista.Grafico()
        elif opcion=="4":
            print("Justin Josue Aguirre Román\n202004734\nIntrucción a la Programación y Computación 2 sección A\nIngenieria en Ciencias y Systemas\n4to Semestre")
        elif opcion=="6":
            exit()
        else:
            print("ENTRADA INCORRECTA INGRESE UNA OPCION VALIDA")
