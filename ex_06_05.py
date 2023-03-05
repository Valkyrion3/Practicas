def main():
    print("Ejercicio Operaciones con string")
    str = "X-DSPAM-Confidence: 0.8475"
    ipos = str.find(':')
    #print(ipos)
    piece = str[ipos+2:]
    #print(piece)
    value = float(piece)
    print(value)


if __name__ == "__main__":
    main()