import random

f1 = open("Cekilis_Sonuclari2.txt", "w")

random_de = set(())
a = int(input("Kaç tane talihli istiyorsunuz?:"))
b = int(input("Katılımcıların başlangıç değeri:"))
c = int(input("Katılımcıların bitiş değeri:"))

while (len(random_de) < a):
    random_de.add(random.randrange(b, c))
    
for i in random_de:
    f1.write(str(i)+ ",")
