# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:37:59 2021

@author: mcifu
"""

import sys
import re



"""
check_line(linea, stack, count)

linea: variable en donde guardo la línea que estoy revisando

stack: pila con la que se hace el autómata

count: variable que guarda cuántas veces lee correctamente un while

Esta función nos permite leer, línea por línea. Regresa el número de whiles
que contiene el documento a revisar. 
"""

def check_line(array):
    stack = []
    total_whiles = 0
    fail = False
    total_vars = 0
    total_opers = 0
    
    try:
        for element in array:
            #linea = re.split('\s',element) why is this necesary?
            #print(linea)
            if re.findall('^(\s|\t)*while',element): #quiero checar si está bien escrito
                variables = re.findall('\(((\w{1}|\d{1})\s*(>|=\s*=|<)\s*(\w{1}|\d{1}))\)',element)
                if not variables: #entonces los paréntesis no están bien, bye
                    fail = True
                    break
                else:
                    numvars, numops = count_vars_and_ops(variables)
                    total_opers += numops
                    total_vars += numvars
                
                matches = re.findall('(\{$|{}$)', element)
                if matches[0][0] == '{':
                    stack.append('{')
                elif matches[0][0] == '{}':
                    total_whiles += 1
                else:
                    sys.exit("ERROR") #Creo que aquí me falta tomar en cuenta el caso donde la llave se abra en una línea abajo pero no sé si importe
                    
            if re.findall('\}$', element):
                total_whiles += 1
                stack.pop()
                    
                
    except:
        sys.exit("ERROR")
        
    if len(stack) == 0 and not fail:
        print(f"Dentro del documento {Arch} existen: {total_whiles} whiles")
        print(f"Dentro del documento {Arch} existen: {total_vars} variables")
        print(f"Dentro del documento {Arch} existen: {total_opers} variables")
        
    else:
        sys.exit("ERROR")
        
def count_vars_and_ops(variables):
   numops = 0
   numvars = 0
   tokens = variables[0]
   i = 1
   while i < len(tokens):
       if re.findall('(=\s*=|>|<)',tokens[i]):
           numops += 1
       elif re.findall('\D',tokens[i]): #no lo cuentas como variable si es un dígito
           numvars += 1
       i+=1
   #print(tokens)
   return numvars, numops
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
    check_line(array)
    
    
if __name__ == "__main__":
    main()

    
  