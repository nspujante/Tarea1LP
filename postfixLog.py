import re

# Clase Pila
class Stack:
    """
    Nombre de la funcion: __init__
    --------------------------------------
    Parametros:
    self= Stack
    --------------------------------------
    Inicia el objeto pila
    """
    def __init__(self):
        self.stack = []
    """
    Nombre de la funcion: push
    --------------------------------------
    Parametros:
    self= Stack
    item= string
    --------------------------------------
    Mete un string a la pila
    """
    def push(self, item):
        self.stack.append(item)   
    """
    Nombre de la funcion: pop
    --------------------------------------
    Parametros:
    self= Stack
    --------------------------------------
    Saca el string de la cima de la pila y lo retorna
    """        
    def pop(self):
        result = -1
        if self.stack != []:
            result = self.stack.pop()
        return result
    """
    Nombre de la funcion: isEmpy
    --------------------------------------
    Parametros:
    self= Stack
    --------------------------------------
    Retorno True si la pila esta vacia, False si no.
    """  
    def isEmpty(self):
        return self.stack == []
    """
    Nombre de la funcion: topChar
    --------------------------------------
    Parametros:
    self= Stack
    --------------------------------------
    retorna el string que esta en la cima de la pila
    """  
    def topChar(self):
        result = -1
        if self.stack != []:
            result = self.stack[len(self.stack) - 1]
        return result
# infix to postfix
"""
Nombre de la funcion: toPostfix
--------------------------------------
Parametros:
expression: string
--------------------------------------
Transforma una operacion logica de Infix a Postfix, retorna un string con la expresion transformada.
"""
def toPostfix(expression):
    result = ""
    var=""
    dOpen=0
    dClose=0
    operators=r"\>|\<|\=|\>\=|\<\=|\=\="
    opLog=r"and|or"
    variable=r"[a-zA-Z]([a-z0-9A-Z])*|[0-9]+"
    basicOperation=rf"(\({variable}(\+|\-|\*|\/){variable}\))"
    errorOperation=rf"(\(({variable})*\)|\(({variable})({operators})\)|\(({operators})({variable})\)|\(({operators})\)|({operators})\)|\(({operators}))"
    stack = Stack()
    if re.search(errorOperation,expression)!= None:
        print(1)
        return "Error"
    elif re.search(basicOperation,expression)!= None:
        charCont=0
        for char in expression:
            if re.fullmatch(r"[a-z0-9A-Z]",char)!=None: #verifica que el caracter sea correcto para una variable
                var+=char
            elif re.fullmatch(operators,char)!= None or re.fullmatch(opLog,var)!=None: #verifica que el caracter es un operador
                if re.fullmatch(r"[a-zA-Z]([a-z0-9A-Z])*|[0-9]*",var)!=None: #verifica que la variable antes del signo es correcta para agregarla IMPORTANTE
                    if re.fullmatch(opLog,var)==None:
                        result+=var+" " #agrega la variable
                        var="" #vacia la variable
                        topChar = stack.topChar() #obtiene el caracter de la pila
                    else:
                        stack.push(var)
                        var=""
                        dOpen+=1
                    if topChar == '(':
                        if char=="=" and expression[charCont+1]!="=":
                            return "Error"
                        else:
                            stack.push(char)
                    elif re.fullmatch(operators,topChar)!=None: #solo corre para un condicional de doble caracter
                        if topChar in "<>=" and char=="=" or char=="(":
                            if expression[charCont+1]=="=":
                                return "Error"
                            else:
                                stack.push(char)
                        else:
                            return "Error"
                    else: #si no hay una apertura de parentesis antes de un operador tira error
                        print(2)
                        return "Error"
                else:
                    print(3) #si se creo una variable con caracteres no admitidos tira error
                    return "Error"
            elif char == '(':
                dOpen+=1
                stack.push(char)
            elif char == ')':
                dClose+=1
                if re.fullmatch(r"[a-zA-Z]([a-z0-9A-Z])*|[0-9]+",var)!=None or var=="": #antes de cerrar el parentesis debe haber si o si una variable, por eso el +
                    result+=var+" "
                    var=""
                    if stack.isEmpty():
                        print(4)
                        return "Error"
                    else:
                        cpop = stack.pop()
                else:
                    print(5)
                    return "Error"
                while cpop != '(': #si antes se le hizo pop a un operador si busca hacer pop a un parentesis
                    #print(cpop)
                    result += cpop+" "
                    cpop = stack.pop()
            elif re.fullmatch(r"[a-z0-9A-Z]",char)==None: #verifica si hay algun caracter no valido
                print(6)
                return "Error"
            charCont+=1
        while not stack.isEmpty():
            cpop = stack.pop()
            result += cpop
        if dOpen==dClose:
            return result
        else:
            print(7)
            return "Error"
    else:
        print(8)
        return "Error"