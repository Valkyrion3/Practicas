def computepay(hours, rate):
    #print("In computepay", hours, rate)
    if(hours>40):
        #print("Overtime")
        reg = hours * rate
        otp = (hours-40) * (rate * .5)
        pay = reg + otp
    else:
        #print("Regular")
        pay = hours * rate
    #print("Returning pay",pay)
    return pay
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
    xp = computepay(fh,fr)
    print("Pay:", xp)

if __name__ == "__main__":
    main()