#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import json
import random

with open('data.json') as json_file:
    data = json.load(json_file)

def todosJE():
    while 1:
        tipo =random.choice(list(dic.keys()))
        esp, jap = random.choice(list(dic.get(tipo).items()))
        print(jap)
        res=input()
        if(res.upper()==esp.upper()):
            print("CORRECTO")
        else:
            print("INCORRECTO, la resupuesta correcta es "+ esp)
        print("----------")

def todosEJ():
    while 1:
        tipo =random.choice(list(dic.keys()))
        esp, jap = random.choice(list(dic.get(tipo).items()))
        print(esp)
        res=input()
        if(res==jap):
            print("CORRECTO")
        else:
            print("INCORRECTO, la resupuesta correcta es "+ jap)
        print("----------")

def concretoJE(op):
    while 1:
        esp, jap = random.choice(list(dic.get(op).items()))
        print(jap)
        res=input()
        if(res.upper()==esp.upper()):
            print("CORRECTO")
        else:
            print("INCORRECTO, la resupuesta correcta es "+ esp)
        print("----------") 

def concretoEJ(op):
    while 1:
        esp, jap = random.choice(list(dic.get(op).items()))
        print(esp)
        res=input()
        if(res==jap):
            print("CORRECTO")
        else:
            print("INCORRECTO, la resupuesta correcta es "+ jap)
        print("----------") 

def vocabulario(op):
    for par in dic.get(op):
        #print (par + "\t\t" +dic.get(op).get(par))
        print ('{0:30s} {1:10s}'.format(par, dic.get(op).get(par)))

if __name__ == "__main__":
    temas={ 1: "Sobre todo"}
    dic={}
    num=2
    for line in data:
        temas.update({num:line})
        dic.update({line:{}})
        num+=1

    for line in data:
        for palabra in data[line]:
            dic.get(line).update({palabra["ES"]:palabra["JA"]})

    while 1:
        print("---------")
        print("Que opcion quieres?")
        print("1. De japones a espanol")
        print("2. De espanol a japones")
        print("3. Mostrar vocabulario")
        le=input()
        print("---------")
        print("Sobre que quires repasar?")
        for key in temas:
            print(str(key)+" "+temas.get(key))
        op=input()
        print("---------")
        if(le=="1"):
            if(op=="1"):
                todosJE()
            else:
                concretoJE(temas.get(int(op)))
        elif(le=="2"):
            if(op=="1"):
                todosEJ()
            else:
                concretoEJ(temas.get(int(op)))
        elif(le=="3"):
            vocabulario(temas.get(int(op)))
    
 

