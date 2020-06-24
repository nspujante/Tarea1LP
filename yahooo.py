import re
import postfix
import postfixLog

#Expresiones regulares
addPlayer=re.compile("Add Player "+r"([a-zA-Z]([a-z0-9A-Z])*)")
took=re.compile(r"([a-zA-Z]([a-z0-9A-Z])*)"+" took "+r"([0-9]+|-[1-9][0-9]*)")
needsPower=re.compile(r"([a-zA-Z]([a-z0-9A-Z])*)"+" needs a power up")
show=re.compile("show "+r"([a-zA-Z]([a-z0-9A-Z])*|[0-9]+|-[1-9][0-9]*)")
jump=re.compile(r"([a-zA-Z]([a-z0-9A-Z])*)"+" jumps to ")
variableRegex=re.compile(r"([a-zA-Z]([a-z0-9A-Z])*)")
operators=re.compile(r"\+|\-|\*|\/")
conditional=re.compile("It's a me a conditional "+r".+"+" Yahoo")
comparators=re.compile(r"==|<|>|=<|=>")
logicOpRegex=re.compile(r"and|or")
cicleRe=re.compile("YA MA "+r".+"+" YAHOO!")
function=re.compile("Secret Level "+r"[a-zA-Z]+"+" "+r"(([a-zA-Z]([a-z0-9A-Z])*)-*)+")
freturn=re.compile("Return to Level "+r"(([a-zA-Z]([a-z0-9A-Z])*)|[0-9]+)")
callFunction=re.compile(r"([a-zA-Z]([a-z0-9A-Z])*)"+" enters "+r"[a-zA-Z]+"+" "+r"(([a-zA-Z]([a-z0-9A-Z])*|[0-9]+)\-?)+")

#Funciones
"""
Nombre de la funcion: setVariable
--------------------------------------
Parametros:
line= string
variableDict= diccionario
--------------------------------------
Ingresa al diccionario de variables una nueva variable creada por el usuario como llave y valor None, no tiene retorno.
"""
def setVariable(line,variableDict):
    variableDict[re.split(r"\s",line)[2]]=None
"""
Nombre de la funcion: setValue
--------------------------------------
Parametros:
line= string
variableDict= diccionario
--------------------------------------
Ingresa al diccionario de variables el valor de la variable que pidio el usuario, no retorna nada.
"""
def setValue(line, variableDict):
    variableDict[re.split(r"\s",line)[0]]=int(re.split(r"\s",line)[2])
"""
Nombre de la funcion: errorVerification
--------------------------------------
Parametros:
functionDict= diccionario
--------------------------------------
Recorre el archivo verificando posibles errores de sintaxis, si encuentra uno se encarga de printearlo, retorna True o False dependiendo de si encontro errores.
"""
def errorVerification(functionDict):
    code= open("yahooo.txt","r")
    trash=True
    verification=True
    mainCont=0
    funcName=""
    funcCont=0
    count=1
    for line in code:
        lineStrip=line.strip()
        if funcCont==1:
            functionDict[funcName].append(lineStrip)
        if re.fullmatch("Start Game",lineStrip):
            mainCont+=1
            if mainCont!=1:
                print("woooooooohhhh! "+str(count)+": "+lineStrip)
                count+=1
                verification=False
            else:
                trash=False
                continue
        elif re.fullmatch("Game Over",lineStrip) and trash==False:
            mainCont+=1
            if mainCont!=2:
                print("woooooooohhhh! "+str(count)+": "+lineStrip)
                count+=1
                verification=False
            else:
                trash=True
                continue
        elif addPlayer.fullmatch(lineStrip) != None and trash==False:
            continue
        elif  took.fullmatch(lineStrip) != None and trash==False:
            continue
        elif needsPower.fullmatch(lineStrip) != None and trash==False:
            continue
        elif show.fullmatch(lineStrip) != None and trash==False:
            continue
        elif jump.match(lineStrip) != None and trash==False:
            split=re.split(r"\s",lineStrip)
            if len(split) == 4:
                expression=split[3]
                if postfix.toPostfix(expression)!="Error":
                    continue
                else:
                    print("woooooooohhhh! "+str(count)+": "+lineStrip)
                    count+=1
                    verification=False
            else:
                print("woooooooohhhh! "+str(count)+": "+lineStrip)
                count+=1
                verification=False
        elif conditional.fullmatch(lineStrip)!=None and trash==False:
            split=re.split(r"\s",lineStrip)
            if len(split)==7:
                expression=split[5]
                if postfixLog.toPostfix(expression)!="Error":
                    continue
                else:
                    print("woooooooohhhh! "+str(count)+": "+lineStrip)
                    verification=False
            else:
                print("woooooooohhhh! "+str(count)+": "+lineStrip)
                verification=False
        elif re.fullmatch("Mamma Mia...",lineStrip) and trash==False:
            continue
        elif re.fullmatch("Let's Go!",lineStrip) and trash==False:
            continue
        elif cicleRe.fullmatch(lineStrip)!=None and trash==False:
            continue
        elif re.fullmatch("AH HA!",lineStrip)!=None and trash==False:
            continue
        elif function.fullmatch(lineStrip)!=None and trash==True:
            funcCont+=1
            if funcCont!=1:
                print("woooooooohhhh! "+str(count)+": "+lineStrip)
                count+=1
                verification=False
            else:
                funcName=re.split(r"\s",line)[2]
                functionDict[funcName]=[]
                trash=False
                continue
        elif freturn.fullmatch(lineStrip)!=None and trash==False:
            funcCont+=1
            if funcCont!=2:
                print("woooooooohhhh! "+str(count)+": "+lineStrip)
                count+=1
                verification=False
            else:
                trash=True
                funcCont=0
                continue
        elif callFunction.fullmatch(lineStrip)!=None:
            continue
        else:
            print("woooooooohhhh! "+str(count)+": "+lineStrip)
            count+=1
            verification=False
    code.close()
    if verification==False:
        return False
    else:
        return True
"""
Nombre de la funcion: userInput
--------------------------------------
Parametros:
line= string
variableDict= diccionario
--------------------------------------
Ingresa al diccionario de variables el valor de la variable que pidio el usuario por consola, no retorna nada.
"""
def userInput(line, variableDict):
    variableDict[re.split(r"\s",line)[0]]=int(input("Input: "))
"""
Nombre de la funcion: userOutput
--------------------------------------
Parametros:
line= string
variableDict= diccionario
--------------------------------------
Printea el valor de una variable o un entero, no retorna nada.
"""
def userOutput(line, variableDict):
    if variableRegex.fullmatch(re.split(r"\s",line)[1])!=None:
        print(variableDict[re.split(r"\s",line)[1]])
    elif re.fullmatch(r"([0-9]+|-[1-9][0-9]+)",re.split(r"\s",line)[1])!=None:
        print(re.split(r"\s",line)[1])
"""
Nombre de la funcion: mathOperations
--------------------------------------
Parametros:
line= string
variableDict= diccionario
--------------------------------------
Calcula una operacion matematica y le asigna el valor a una variable del diccionario de variables, no retorna nada.
"""
def mathOperations(line,variableDict):
    operation=postfix.toPostfix(re.split(r"\s",line)[3])
    operationList=re.split(r"\s",operation)
    i=0
    for item in operationList:
        if variableRegex.fullmatch(item)!=None:
            operationList[i]=str(variableDict[item])
        i+=1
    i=0
    while len(operationList)!=1:
        if operators.fullmatch(operationList[i+2])!=None:
            if operationList[i+2]=='+':
                operationList[i]=str(float(operationList[i])+float(operationList[i+1]))
                operationList.pop(i+1)
                operationList.pop(i+1)
                i=0
            elif operationList[i+2]=='-':
                operationList[i]=str(float(operationList[i])-float(operationList[i+1]))
                operationList.pop(i+1)
                operationList.pop(i+1)
                i=0
            elif operationList[i+2]=='*':
                operationList[i]=str(float(operationList[i])*float(operationList[i+1]))
                operationList.pop(i+1)
                operationList.pop(i+1)
                i=0
            elif operationList[i+2]=='/':
                operationList[i]=str(float(operationList[i])/float(operationList[i+1]))
                operationList.pop(i+1)
                operationList.pop(i+1)
                i=0
        else:
            i+=1
    variableDict[re.split(r"\s",line)[0]]=round(float(operationList[0]))
"""
Nombre de la funcion: logicValue
--------------------------------------
Parametros:
line= string
variableDict= diccionario
pos= int
--------------------------------------
Calcula una operacion logica y retorna si es True o False.
"""
def logicValue(line,variableDict,pos):
    logicOp=postfixLog.toPostfix(re.split(r"\s",line)[pos])
    logicOpList=re.split(r"\s",logicOp)
    i=0
    for item in logicOpList:
        if logicOpList[i]=="":
            logicOpList.pop(i)
        elif variableRegex.fullmatch(item)!=None and logicOpRegex.fullmatch(item)==None:
            logicOpList[i]=str(variableDict[item])
        elif item in "<>=" and logicOpList[i+1] in "<>=":
            logicOpList[i]=logicOpList[i]+logicOpList[i+1]
            logicOpList.pop(i+1)
        i+=1
    i=0
    for item in logicOpList:
        if logicOpList[i]=="":
            logicOpList.pop(i)
        i+=1
    i=0
    for item in logicOpList:
        if comparators.fullmatch(str(logicOpList[i+2]))!=None:
            if logicOpList[i+2]=="==":
                logicOpList[i]=int(logicOpList[i])==int(logicOpList[i+1])
                logicOpList.pop(i+1)
                logicOpList.pop(i+1)
            elif logicOpList[i+2]==">":
                logicOpList[i]=int(logicOpList[i])>int(logicOpList[i+1])
                logicOpList.pop(i+1)
                logicOpList.pop(i+1)
            elif logicOpList[i+2]=="<":
                logicOpList[i]=int(logicOpList[i])<int(logicOpList[i+1])
                logicOpList.pop(i+1)
                logicOpList.pop(i+1)
            elif logicOpList[i+2]=="=<":
                logicOpList[i]=int(logicOpList[i])<=int(logicOpList[i+1])
                logicOpList.pop(i+1)
                logicOpList.pop(i+1)
            elif logicOpList[i+2]=="=>":
                logicOpList[i]=int(logicOpList[i])>=int(logicOpList[i+1])
                logicOpList.pop(i+1)
                logicOpList.pop(i+1)
        else:
            i+=1
    if "and" in logicOpList or "or" in logicOpList:
        i=0
        while len(logicOpList)>1:
            if logicOpRegex.fullmatch(str(logicOpList[i+2]))!=None:
                if logicOpList[i+2]=="and":
                    logicOpList[i]=logicOpList[i] and logicOpList[i+1]
                    logicOpList.pop(i+1)
                    logicOpList.pop(i+1)
                    i=0
                elif logicOpList[i+2]=="or":
                    logicOpList[i]=logicOpList[i] or logicOpList[i+1]
                    logicOpList.pop(i+1)
                    logicOpList.pop(i+1)
                    i=0
            else:
                i+=1
    return logicOpList[0]
"""
Nombre de la funcion: userInput
--------------------------------------
Parametros:
cicleLine= string
cicleList= Lista
variableDict= diccionario
pos= int
--------------------------------------
Ejecuta de forma recursiva el codigo dentro de los while, no retorna nada.
"""
def recursiveCicle(cicleLine,cicleList,variableDict,pos):
    Clist=[]
    reCondCheck=0
    recCicleLine=""
    recCicleCheck=0
    true=logicValue(cicleLine,variableDict,pos)
    while true:
        for item in cicleList:
            if re.fullmatch("AH HA!",item)!=None and reCondCheck==0: #fin del ciclo
                if recCicleCheck>=0:
                    recCicleCheck-=1
                    if recCicleCheck==0:
                        recursiveCicle(recCicleLine,Clist,variableDict,2)
                    else:
                        Clist.append(item)
                else:
                    recCicleCheck=0
            elif cicleRe.fullmatch(item)!=None and reCondCheck==0: #inicio ciclo
                if logicValue(item,variableDict,2) and recCicleCheck==0:
                    recCicleLine=item
                    recCicleCheck+=1
                elif recCicleCheck>0:
                    recCicleCheck+=1
                    Clist.append(item)
                else:
                    recCicleCheck=-1
            elif recCicleCheck>=1 or recCicleCheck==-1 and reCondCheck==0: #ciclo corriendo
                if recCicleCheck>=1:
                    Clist.append(item)
                elif recCicleCheck==-1:
                    continue
            elif jump.match(item) != None and reCondCheck==0: #operacion matematica
                mathOperations(item,variableDict)
            elif show.fullmatch(item) != None and reCondCheck==0: #print
                userOutput(item,variableDict)
            elif took.fullmatch(item) != None and reCondCheck==0: #took
                setValue(item, variableDict)
            elif needsPower.fullmatch(item) != None and reCondCheck==0: #Input
                userInput(item,variableDict)
            elif conditional.fullmatch(item)!=None: #inicio condicional
                if logicValue(item,variableDict,5):
                    continue
                else:
                    reCondCheck=1
            elif re.fullmatch("Mamma Mia...",item)!=None: #else
                if reCondCheck==1:
                    reCondCheck=0
                else:
                    reCondCheck=1
            elif re.fullmatch("Let's Go!",item): # fin condicional
                reCondCheck=0
        true=logicValue(cicleLine,variableDict,pos)

variableDict={}
functionDict={}
cicleList=[]
funVariablesList=[]
condCheck=0
cicleCheck=0
functionCheck=False
cicleLine=""
if(errorVerification(functionDict)==True):
    print("Ejecutando codigo...")
    code= open("yahooo.txt","r")
    for line in code:
        lineStrip=line.strip()
        if functionCheck==False:
            if re.fullmatch("Start Game",lineStrip) and condCheck==0: #Start Game
                continue
            elif re.fullmatch("Game Over",lineStrip) and condCheck==0: #Game Over
                continue
            elif re.fullmatch("AH HA!",lineStrip)!=None and condCheck==0: #Termino de ciclo
                if cicleCheck>=0:
                    cicleCheck-=1
                    if cicleCheck==0:
                        recursiveCicle(cicleLine,cicleList,variableDict,2)
                    else:
                        cicleList.append(lineStrip)
                else:
                    cicleCheck=0
            elif cicleRe.fullmatch(lineStrip)!=None and condCheck==0: #Inicio de ciclo
                if logicValue(lineStrip,variableDict,2) and cicleCheck==0:
                    cicleLine=lineStrip
                    cicleCheck+=1
                elif cicleCheck>0:
                    cicleCheck+=1
                    cicleList.append(lineStrip)
                else:
                    cicleCheck=-1
            elif cicleCheck>=1 or cicleCheck==-1 and condCheck==0: #Durante ciclo
                if cicleCheck>=1:
                    cicleList.append(lineStrip)
                elif cicleCheck ==-1:
                    continue
            elif addPlayer.fullmatch(lineStrip) != None and condCheck==0: #addPLayer
                setVariable(lineStrip, variableDict)  
            elif took.fullmatch(lineStrip) != None and condCheck==0: #took
                setValue(lineStrip, variableDict)
            elif needsPower.fullmatch(lineStrip) != None and condCheck==0: #Input
                userInput(lineStrip,variableDict)
            elif show.fullmatch(lineStrip) != None and condCheck==0: #print
                userOutput(lineStrip,variableDict)
            elif jump.match(lineStrip) != None and condCheck==0: #expresion matematica
                mathOperations(lineStrip,variableDict)
            elif conditional.fullmatch(lineStrip)!=None and condCheck==0: #inicio condicional
                if logicValue(lineStrip,variableDict,5):
                    continue
                else:
                    condCheck=1
            elif re.fullmatch("Mamma Mia...",lineStrip)!=None: #else
                if condCheck==1:
                    condCheck=0
                else:
                    condCheck=1
            elif re.fullmatch("Let's Go!",lineStrip): # fin condicional
                condCheck=0
            elif function.fullmatch(lineStrip) and condCheck==0:
                functionCheck=True
                funVariablesList=re.split(r"\-",re.split(r"\s",lineStrip)[3])
            elif callFunction.fullmatch(lineStrip) and condCheck==0:
                i=0
                while i<len(funVariablesList):
                    if re.split(r"\-",re.split(r"\s",lineStrip)[3])[i] in variableDict:
                        variableDict[funVariablesList[i]]=variableDict[re.split(r"\-",re.split(r"\s",lineStrip)[3])[i]]
                    else:
                        variableDict[funVariablesList[i]]=re.split(r"\-",re.split(r"\s",lineStrip)[3])[i]
                    i+=1
                funList=functionDict[re.split(r"\s",lineStrip)[2]]
                for funLine in funList:
                    if re.fullmatch("AH HA!",funLine)!=None and condCheck==0: #Termino de ciclo
                        if cicleCheck>=0:
                            cicleCheck-=1
                            if cicleCheck==0:
                                recursiveCicle(cicleLine,cicleList,variableDict,2)
                            else:
                                cicleList.append(funLine)
                        else:
                            cicleCheck=0
                    elif cicleRe.fullmatch(funLine)!=None and condCheck==0: #Inicio de ciclo
                        if logicValue(funLine,variableDict,2) and cicleCheck==0:
                            cicleLine=funLine
                            cicleCheck+=1
                        elif cicleCheck>0:
                            cicleCheck+=1
                            cicleList.append(funLine)
                        else:
                            cicleCheck=-1
                    elif cicleCheck>=1 or cicleCheck==-1 and condCheck==0: #Durante ciclo
                        if cicleCheck>=1:
                            cicleList.append(funLine)
                        elif cicleCheck ==-1:
                            continue
                    elif addPlayer.fullmatch(funLine) != None and condCheck==0: #addPLayer
                        setVariable(funLine, variableDict)  
                    elif took.fullmatch(funLine) != None and condCheck==0: #took
                        setValue(funLine, variableDict)
                    elif needsPower.fullmatch(funLine) != None and condCheck==0: #Input
                        userInput(funLine,variableDict)
                    elif show.fullmatch(funLine) != None and condCheck==0: #print
                        userOutput(funLine,variableDict)
                    elif jump.match(funLine) != None and condCheck==0: #expresion matematica
                        mathOperations(funLine,variableDict)
                    elif conditional.fullmatch(funLine)!=None and condCheck==0: #inicio condicional
                        if logicValue(funLine,variableDict,5):
                            continue
                        else:
                            condCheck=1
                    elif re.fullmatch("Mamma Mia...",funLine)!=None: #else
                        if condCheck==1:
                            condCheck=0
                        else:
                            condCheck=1
                    elif re.fullmatch("Let's Go!",funLine): # fin condicional
                        condCheck=0
                    elif freturn.fullmatch(funLine) and condCheck==0:
                        if re.split(r"\s",funLine)[3] in variableDict:
                            variableDict[re.split(r"\s",lineStrip)[0]]=variableDict[re.split(r"\s",funLine)[3]]
                        else:
                            variableDict[re.split(r"\s",lineStrip)[0]]=re.split(r"\s",funLine)[3]
        elif freturn.fullmatch(lineStrip):
            functionCheck=False
    code.close()
    print("Termino la ejecucion")