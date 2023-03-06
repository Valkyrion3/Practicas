import pickle
variableglobal = None
def main():
  global variableglobal
  print("Diccionario")
  nombre = input("Ingresa el nombre:\n")
  numero = input("Ingresa el número:\n")
  edad = input("Ingresa la edad:\n")
  contacto = {
    "Nombre": nombre,
    "Número": numero,
    "Edad": edad
  }
  print(type(contacto))
  #Para acceder a los valores del diccionario
  print(contacto["Nombre"])    
  with open("contacto.bin","ab") as f:
    pickle.dump(contacto,f)    
  Lista =[]
  with open("contacto.bin","rb") as f:
    while True:
      try:
        registro = pickle.load(f)
      except EOFError:
        break
      Lista.append(registro)
    print(Lista)
if __name__ == "__main__":
  main()