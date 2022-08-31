#KALKULATOR
#Irenne Dwita Natalia 71210752
#Unguided 1


while True:
    print("KALKULATOR")
    print("=" * 20)
    print("A. Penjumlahan")
    print("B. Pengurangan")
    print("C. Perkalian")
    print("D. Pembagian")
    print("Q. Quit")

    pilih = str(input("Masukkan pilihan Anda: "))

    if pilih == "Q":
        break
    elif pilih == "A":
        bil1 = int(input("Masukkan bilangan pertama: "))
        bil2 = int(input("Masukkan bilangan kedua: "))
        print("hasil penjumlahan adalah", bil1 + bil2)
    elif pilih == "B":
        bil1 = int(input("Masukkan bilangan pertama: "))
        bil2 = int(input("Masukkan bilangan kedua: "))
        print("hasil pengurangan adalah", bil1 - bil2)
    elif pilih == "C":
        bil1 = int(input("Masukkan bilangan pertama: "))
        bil2 = int(input("Masukkan bilangan kedua: "))
        print("hasil perkalian adalah", bil1 * bil2)
    else:
        bil1 = int(input("Masukkan bilangan pertama: "))
        bil2 = int(input("Masukkan bilangan kedua: "))
        print("hasil pembagian adalah", bil1 / bil2)
