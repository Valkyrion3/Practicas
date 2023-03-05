def main():
    print("Ejercicio Manejo Archivos")
    with open("mbox-short.txt","r") as f:
        for line in f:
            line = line.rstrip()
            wds = line.split()
            if (len(wds)<3 or wds[0] != "From"):
                continue
            print(wds[2])
if __name__ == "__main__":
    main()