def main():
saldoa = float(input("Ingrese el saldo anterior de la cuenta"))
egresos = float(input("Ingrese los egresos de la cuenta"))
ingresos = float(input("Ingrese los ingresos de la cuenta"))
cheque = float(input("Ingrese la cantidad de cheques expedidos"))

saldop = float(saldo-egresos+ingresos-(cheque*13))
saldot = float(saldot-(saldot*7.5/100))

print("El saldo total es de:",saldot,"pesos")

