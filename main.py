#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import json
import random

with open('datos.json') as json_file:
    data = json.load(json_file)


def concretoJE(op):
    while 1:
        if (op=="Sobre todo"):
            tipo =random.choice(list(dic.keys()))
            esp, jap = random.choice(list(dic.get(tipo).items()))
        else:
            esp, jap = random.choice(list(dic.get(op).items()))
        print(jap[0])
        res=input()
        if (res.upper=='STOP'):
            break
        if(res.upper()==esp.upper()):
            print("CORRECTO")
        else:
            print("INCORRECTO, la resupuesta correcta es "+ esp)
        print("----------") 

def concretoEJ(op):
    while 1:
        if (op=="Sobre todo"):
            tipo =random.choice(list(dic.keys()))
            esp, jap = random.choice(list(dic.get(tipo).items()))
        else:
            esp, jap = random.choice(list(dic.get(op).items()))
        print(esp)
        res=input()
        if (res.upper=='STOP'):
            break
        if(res==jap or (res==jap[1] and jap[1]!="")):
            print("CORRECTO")
        else:
            print("INCORRECTO, la resupuesta correcta es "+ jap)
        print("----------") 

def vocabulario(op):
    for par in dic.get(op):
        print ('{0:30s} {1:30s} {2:30s}'.format(par, dic.get(op).get(par)[0],dic.get(op).get(par)[1]))

def dicEJ():
    while 1:
        print("Palabra en esp:")
        pal=input()
        if (pal.upper=='STOP'):
            break
        for temas in dic:
            for palab in dic.get(temas):
                if(pal.upper()==palab.upper()):
                    print(dic.get(temas).get(palab)[0])
                    break
        print("----------")

def dicJE():
    while 1: 
        print("Palabra en jap:")
        pal=input()
        if (pal.upper=='STOP'):
            break
        for temas in dic:
            for palab in dic.get(temas):
                if(pal==dic.get(temas).get(palab)[0] or pal==dic.get(temas).get(palab)[1]):
                    print(palab)
                    break
        print("----------")

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
            dic.get(line).update({palabra["ES"]:[palabra["JA"],palabra["KA"]]})

    while 1:
        print("---------")
        print("Que opcion quieres?")
        print("1. De japones a espanol")
        print("2. De espanol a japones")
        print("3. Mostrar vocabulario")
        print("4. Diccionario Esp-Jap")
        print("5. Diccionario Jap-Esp")
        le=input()
        print("---------")
        if(le!='4' and le!='5'):
            print("Sobre que quires repasar?")
            for key in temas:
                print(str(key)+" "+temas.get(key))
            op=input()
            print("---------")

        if(le=="1"):
            concretoJE(temas.get(int(op)))
        elif(le=="2"):
            concretoEJ(temas.get(int(op)))
        elif(le=="3"):
            vocabulario(temas.get(int(op)))
        elif(le=="4"):
            dicEJ()
        elif(le=="5"):
            dicJE()
    