n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1 + n2) / 2
print("Sua média foi {:.2f}.".format(media))
if media >=6:
    print("Parabens, você foi aprovado! ")
else:
    print("Você foi reprovado! ")
