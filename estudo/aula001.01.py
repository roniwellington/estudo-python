import random
#Gerando números aleatórios
print(random.random() * 100)
print(random.random() * 100)
print (int(random.random() * 100))


#formatação de strings
print("Tentativa {} de {}".format(3,10))
print("Tentativa {1} de {0}".format(3,10))
print("R$ {}".format(1.59))
print("R$ {:f} ".format(1.59))
print("R$ {:.2f}".format(1.59))
print("R$ {:.2f}".format(1.5))
print("R$ {:7.2f}".format(1.5))
print("R$ {:7.2f}".format(123.5))
print("R$ {:07.2f}".format(4.5))
print("R$ {:08.3f}".format(1.5))
print("R$ {:07d}".format(4))
print("R$ {:7d}".format(46))
print("Data {:2d}/{:2d}".format(9,4))
print("Data {:2d}/{:2d}".format(19,11))
print("R$ {:7.1f}".format(1000.12)),
print("R$ {:07.2f}".format(4.11))

