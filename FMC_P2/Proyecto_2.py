# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:37:59 2021

@author: mcifu
"""

import sys
import re


"""
get_line (array, index)

array:  es el arreglo que guarda todo lo escrito en el documento txt (separa
        por renglón.
        
index:  indica en qué índice de array va.

line:   variable que regresa una línea del txt (toma un elemento de array
        donde se guardan todas las líneas).

Este método me permite obtener línea por línea de todo el documento txt.
"""
def get_line(array, index):

    #print(f"PRUEBA PRUEBA PRUEBA: {array[index]}")
    x = array[index]
    line = x.split()
    #print(line)

    return line


"""
check_line(linea, stack, count)

linea: variable en donde guardo la línea que estoy revisando

stack: pila con la que se hace el autómata

count: variable que guarda cuántas veces lee correctamente un while

Esta función nos permite leer, línea por línea. Regresa el número de whiles
que contiene el documento a revisar. 
"""
"""
def check_line(linea, stack, count):
    
    for element in linea:
        if linea[0] == "while" or re.findall("^\}$", element): 
            if re.findall("^\(", element):
                stack.append("(")
                print(f"PILAAAA:{stack}")
            elif re.findall("\{$", element):
                stack.append("{")
                print(f"PILAAAA:{stack}")
            elif re.findall("\)$", element):
                stack.pop()
                count += 1
                print(f"PILAAAA:{stack}")
            elif re.findall("^\}", element):
                stack.pop()
                count += 1
                print(f"PILAAAA:{stack}")
    
    print(count)
    #return stack
    return count
"""
def check_line(linea, array, stack, index, count):
    
    try:
        for element in array:
            linea = get_line(array, index)
            #print(f"LINEA{linea}")
            #print(f"ELEMENTO{element}")
            if linea[0] == "while" or re.findall("\}$", element): 
                if re.findall("^\(", element):
                    stack.append("(")
                    #print(f"PILAAAA:{stack}")
                elif re.findall("\{$", element):
                    stack.append("{")
                    #print(f"PILAAAA:{stack}")
                elif re.findall("\)$", element):
                    stack.pop()
                    #print(f"PILAAAA:{stack}")
                elif re.findall("^\}", linea[0]):
                    stack.pop()
                    count += 1
                    #print(f"PILAAAA:{stack}")    
            index += 1
    except:
        sys.exit("ERROR")
        
    if len(stack) == 1:
        print(f"Dentro del documento {Arch} existen: {count} whiles")
    else:
        sys.exit("ERROR")
        
            
"""
count_whiles(line, array, index, stack, resp, cont)

line:   línea del documento revisado

array:  arreglo donde se guardan todas las líneas del documento

index:  índice para realizar la recursividad

stack:  pila que se utiliza en el método check_line

resp:   pila resultante

cont:   regresa cuántos whiles, bien escritos, hay en el documento

"""

"""
def count_whiles(line, array, index, stack, resp, cont): #resp es la pila
    
    for element in array:
        resp = check_line(element, stack, array, index, cont)
        index += 1
        print(resp)
"""  
    #return print(resp)
"""
    if index != len(array):
        linea = get_line(array, index)
        print(linea)
        resp = check_line(linea, stack, cont)
        index += 1
        print(cont)
        return count_whiles(linea, array, index, stack, resp, cont)
"""
    
    #print(resp)
   
    
#----------------------------------------------------------------------------#
#                                   MAIN                                     #
#----------------------------------------------------------------------------#
Arch = 'test.txt'

def main():
    global Arch, arreglo, pila
    #Arch = input("Give the name of the file you want analyze: ") #Para correr el proyecto es necesario proporcionar un archivo .txt
    
    try:
        FN = open(Arch, "r")
        print(f'The file {Arch} was open succesfully\n')
    except:
        sys.exit("Something was wrong\n")
    
    array = []    
    lines = FN.readlines()
    file = open(Arch, "r")
    
    
    for i in range(len(lines)):
        x = file.readline()
        array.append(x.split('\n')[0])
        
        """
    # Lee linea del txt
    for i in range(len(array)):
        x = file.readline()
        line = x.split()
          """
          
    file.close()
    
    stack = ["init"]
    line = " "
    #count_whiles(line, array, 0, stack, [], 0)
    check_line(line, array, stack, 0, 0)
    
    
if __name__ == "__main__":
    main()

    
  