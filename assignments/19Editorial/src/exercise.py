def main():
   a = float(input("Dame el número de palabras:"))
   b = (a//475)*60
   c = a%475
   if 1<=c:
       d=60
   x = (b+d)
   total = (x-(x*10/100))
   print("El costo de la publicación es:",total)

if __name__ == '__main__':
    main()