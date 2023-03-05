def main():
    print("Ejercicio Archivos")
    with open("mbox-short.txt","r") as f:
        print(f)
        for lx in f:
            ly = lx.rstrip()
            print(ly.upper())

if __name__ == "__main__":
    main()