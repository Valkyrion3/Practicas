import pickle
def main():
  print("Serialización de datos")
  nombre = input("Ingresa tu nombre:\n")
  numero = input("Ingresa tu numero:\n")
  edad = int(input("Ingresa tu edad:\n"))
  lista = [nombre, numero, edad]
  print(lista)
  with open("serial.bin","wb") as f:
    pickle.dump(lista,f)
  with open("serial.bin","rb") as f:
    obvar= pickle.load(f)
  print(obvar)
  for dato in obvar:
    print("dato: ",dato)
if __name__ == "__main__":
  main()