largura = int(input("Qual a largura da parede em metros? "))
altura = int(input("Qual a altura da parede em metros? "))
area = largura * altura
tintanecessaria = area * 2
print("Vai ser preciso {}L de tinta para pintar {}m² de parede. ".format(tintanecessaria,area))

