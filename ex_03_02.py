def main():
    print("Ejercicio Condicionales")
    sh = input("Enter hours: ")
    sr = input("Enter rate: ")
    try:
        fh = float(sh)
        fr = float(sr)
    except:
        print("Error, please enter numeric input")
        quit()
    if(fh>40):
        #print("Overtime")
        reg = fh * fr
        otp = (fh-40) * (fr * .5)
        xp = reg + otp
    else:
        #print("Regular")
        xp = fh * fr
    print("Pay:", xp)

if __name__ == "__main__":
    main()