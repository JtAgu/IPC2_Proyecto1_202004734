from Nodo import Nodos
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
    
def Leer(ruta):
    #C:\Users\justin\Downloads\terrenos.xml
    mytree = ET.parse(ruta)
    myroot = mytree.getroot()
    print(myroot.tag)
    return myroot  

if __name__ == '__main__':    
    ruta =input()
    Leer(ruta)
    """opcion=0
    codigo=""
    while opcion !=6:
        imprimir()
        opcion=int(input())
        if opcion==1:
            Leer()
        elif opcion==2:
            print("")
        elif opcion==3:
            print("")
        elif opcion==5:
            print("")
        elif opcion==4:
            print("Justin Josue Aguirre Román\n202004734\nIntrucción a la Programación y Computación 2 sección A\nIngenieria en Ciencias y Systemas\n4to Semestre")
        elif opcion==6:
            exit()
        else:
            print("ENTRADA INCORRECTA INGRESE UNA OPCION VALIDA")
"""