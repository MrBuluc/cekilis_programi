import random

f1 = open("Cekilis_Sonuclari.txt", "w")

random_deg = []
random_de = ()
a = int(input("Kaç tane talihli istiyorsunuz?:"))
b = int(input("Katılımcıların başlangıç değeri:"))
c = int(input("Katılımcıların bitiş değeri:"))

while (len(random_de) < a):
    random_deg.append(random.randrange(b, c))
    random_de = set(random_deg)

for i in random_de:
    f1.write(str(i)+ ",")
