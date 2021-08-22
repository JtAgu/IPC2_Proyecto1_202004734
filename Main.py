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
    #C:\Users\justin\Downloads\terrenos.xml
    mytree = ET.parse(ruta)
    myroot = mytree.getroot()
    c=int(0)
    for x in myroot.findall('terreno'):
        print(x.attrib["nombre"])
        print("inicio en: " +x[1][0].text+" , "+ x[1][1].text)
        print("finalizo en: " +x[2][0].text+" , "+ x[2][1].text)
        Lista.AñadirTerreno(x.attrib["nombre"], x[0][0].text, x[0][1].text, x[1][0].text, x[1][1].text, x[2][0].text, x[2][1].text)

        for terreno in x.findall('posicion'):
            c+=1
            equis=str(terreno.attrib["x"])
            yes=str(terreno.attrib["y"])
            gas=terreno.text                    
            Lista.AñadirPosiciones(x.attrib["nombre"],gas,equis,yes,c,x[0][0].text)
        c=int(0)
    Lista.recorrer()
    return myroot

def procesar(myroot):
    nombre=input("Escribe el nombre del terreno a procesar:\n")
    for x in myroot.findall('terreno'):
        if str(x.attrib["nombre"])==nombre:
            Lista.BuscarInicio(nombre)

def Xml(myroot):
    nombre=input("Escribe el nombre del terreno a procesar:\n")
    for x in myroot.findall('terreno'):
        if str(x.attrib["nombre"])==nombre:
            Lista.BuscarInicio(nombre)
            break


if __name__ == '__main__':    
    
    opcion=0
    codigo=""
    arbol=""
    while opcion !=6:
        imprimir()
        opcion=int(input())
        if opcion==1:
            ruta =input("Ingresa la ruta del archivo:")
            arbol=Leer(ruta)
        elif opcion==2:
            procesar(arbol)
        elif opcion==3:
            Xml(arbol)
            
            
        elif opcion==5:

            ruta =input("Ingresa la ruta del archivo:")
            mytree = ET.parse(ruta)
            myroot = mytree.getroot()
            c=int(0)
            for x in myroot.findall('terreno'):
                print(x[0][0].tag)
        elif opcion==4:
            print("Justin Josue Aguirre Román\n202004734\nIntrucción a la Programación y Computación 2 sección A\nIngenieria en Ciencias y Systemas\n4to Semestre")
        elif opcion==6:
            exit()
        else:
            print("ENTRADA INCORRECTA INGRESE UNA OPCION VALIDA")
