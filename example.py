import re #para usar expresiones regulares
def main():
    # ord() regresa el valor en ascii   
    s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
    lst = re.findall('\\S+@\\S+', s)
    print(lst)
    big = max("Aa123456789") #max regresa el caracter mayor en la numeracion ASCII
    print(big)
    while True:
        line = input("> ")
        if line[0] == "#":
            continue #Regresa al inicio del ciclo
        elif line == "done":
            break   #Termina el ciclo
        print(line)
    print("Done..!")
    print(0 == 0.0)
    print(0 is 0.0) #is, es similar al == pero es más fuerte
    word = "Valkyrion" #in es una operador lógico
    print('v' in word) #False
    print("Valk" in word) #True
    print(type(word)) #Muestra el tipo de variable
    #print(dir(word)) #Muestra los metodos disponibles para ese tipo de variable
    #lstrip->quita espacios a la izquierda, rstrip->derecha, strip-> ambos
    #diccionarios
    dic = dict()
    otro = {"Ed":5,"Edu":2,"Eddy":3}
    print(type(otro))
    print(type(dic))
    dic["money"]= 30
    dic["other"]= 7
    print(dic)
    dic["name"]= "Valkyrion"
    dic["xd"]=0
    print(dic, otro)
    if "Eddy" in otro:
        x=otro["Eddy"]
    else:
        x=0
    print(x)
    x = otro.get("Edgar",0) #Hace lo mismo que las 4 lineas anteriores
    print(x)

    for key,value in dic.items():
        print(key,value)

if __name__ == "__main__":
    main()