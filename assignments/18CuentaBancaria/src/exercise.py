def main():
   saldoa = float(input("Dame el saldo del mes anterior:"))
   ingresos = float(input("Dame los ingresos:"))
   egresos = float(input("Dame los egresos:"))
   cheque = float(input("Dame el número de cheques:"))

   saldop = float(saldoa-egresos+ingresos-(cheque*13))
   saldot = float(saldop-(saldop*7.5/100))

   print("El saldo final de la cuenta es:",saldot)

if __name__ == '__main__':
    main()
