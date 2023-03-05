def main():
    print("Ejercicio Diccionario con archivos")
    fname = input("Enter file name: ")
    if len(fname) < 1 : fname = "intro.txt"
    count = dict()
    with open(fname,"r") as f:
        for line in f:
            line = line.rstrip()
            wds = line.split()
            for w in wds:
                count[w]= count.get(w,0)+1
    largest = -1
    word = None
    for k,v in count.items():
        if v > largest:
            largest = v
            word = k
    
    temp = (sorted([(v,k) for k,v in count.items() ], reverse=True)) #Orden descendente

    for v,k in temp[:5]:
        print(k,v)


if __name__ == "__main__":
    main()