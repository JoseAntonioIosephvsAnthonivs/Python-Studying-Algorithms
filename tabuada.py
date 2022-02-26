tabuada = int(input("Digite um valor: "))
print("tabuada do numero:", tabuada)
for valor in range(1,11,1):
  print(str(tabuada) + "x" + str(valor) + "=" + str((tabuada*valor)))