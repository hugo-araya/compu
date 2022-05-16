# Entero cap_inv
# Real p_interes, interes_calculado, saldo
p_interes = input("Porcentaje de interes: ")
cap_inv = input("Capital a invertir: ")
saldo = cap_inv
interes_calculado = cap_inv * p_interes
if interes_calculado  > 7000:
	saldo = cap_inv + interes_calculado
print "Saldo en mi cuenta: ",saldo
