def main():
  import math
  m = float(input("Escribe el numero de mensajes enviados durante el mes"))
  i = float(input("Escribe el numemro de megas utilizados durante el mes"))
  t = float(input("Escribe el numero de minutos usados durante el mes"))

  precio = float(m*0.8)+(i*0.8)+(t*0.8)
  print("El costo total gastado en el mes fue de",precio,"pesos")

