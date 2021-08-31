def main():
  import math
  m = float(input("Dame el número de mensajes:"))
  i = float(input("Dame el número de megas:"))
  t = float(input("Dame el número de minutos:"))

  precio = float(m*0.8)+(i*0.8)+(t*0.8)
  print("El costo mensual es:",precio)

if __name__ == '__main__':
    main()
