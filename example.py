def main():
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
    print(dir(word)) #Muestra los metodos disponibles para ese tipo de variable
    #lstrip->quita espacios a la izquierda, rstrip->derecha, strip-> ambos
if __name__ == "__main__":
    main()