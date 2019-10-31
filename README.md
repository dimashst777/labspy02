# labspy02

##pengertian if
struktuf if dalam Python dijalankan untuk memeriksa apakah kondisi ini adalah bernilai benar atau salah.
Jika kondisi ini bernilai true, maka python akan menjalankan statemen didalam blok kondisi tersebut 
dan sebaliknya jika kondisi bernilai false maka statemen didalam blok tersebut tidak akan dijalankan.contoh seperti dibawah: 


![iftrue/false](https://github.com/dimashst777/labspy02/blob/master/gambar/phycarm%20yang%20salah.png)


![iftrue/false](https://github.com/dimashst777/labspy02/blob/master/gambar/phycharm%20yang%20benar.png)


Bil1 = int(input("Masukkan Bilangan 1:"))  
Bil2 = int(input("Masukkan Bilangan 2:"))  
Bil3 = int(input("Masukkan Bilangan 3:"))  

if int(Bil1 > Bil2) and (Bil1 > Bil3):

    Terbesar = Bil1
    BigBil = "Bilangan1"

setelah kita memasukkan nilai bilangan dan perbandingan 1,2 dan 3.apabila program kita salah maka tidak akan 
menghasilkan outpu.dan apabila progaram yang kita buat benar maka otomatis mengeluarkan output sesuai dengan 
statemen kita.

###pengertian if else

Jika struktur if sebelumnya hanya menjalankan statemen didalam blok kondisi jika bernilai true, maka
struktur if-else adalah membuat statement untuk kondisi yang bernilai true dan false. Contoh :

elif (Bil2 > Bil3) and (Bil2 > Bil1):

    Terbesar = Bil2
    BigBil = "Bilangan2"



![ifelse/ifelse](https://github.com/dimashst777/labspy02/blob/master/gambar/else.png)



Maka Python menjalankan statemen yang terdapat dalam blok else:
yang berarti bahwa kondisi tersebut bernilai false. 
Intinya struktur ini adalah jika kondisi bernilai true maka statemen didalam if akan 
dieksekusi dan jika bernilai false maka statemen yang dieksekusi adalah statemen didalam else

####pengertian elif  
Struktur else if hampir sama dengan struktur if else, ketika kalian menggunakan struktur 
if else secara berulang harus menggunakan struktur esle if.

else:
    Terbesar = Bil3
    BigBil = "Bilangan3"



![elif/elif](https://github.com/dimashst777/labspy02/blob/master/gambar/elif.png)


contoh statement if else dan elif


![statementifelse](https://github.com/dimashst777/labspy02/blob/master/gambar/statement%20if%20else%2Cel%20if.png)


contoh output statment


![outputstatement](https://github.com/dimashst777/labspy02/blob/master/gambar/output%20staement%20if%20else%2Cel%20if.png)





