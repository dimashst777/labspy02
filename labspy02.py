Bil1 = int(input("Masukkan Bilangan 1:"))
Bil2 = int(input("Masukkan Bilangan 2:"))
Bil3 = int(input("Masukkan Bilangan 3:"))

if int(Bil1 > Bil2) and (Bil1 > Bil3):

    Terbesar = Bil1
    BigBil = "Bilangan1"
elif (Bil2 > Bil3) and (Bil2 > Bil1):

    Terbesar = Bil2
    BigBil = "Bilangan2"
else:
    Terbesar = Bil3
    BigBil = "Bilangan3"

print("Bilangan yang terbesar adalah", BigBil, "dengan nilai", Terbesar)

