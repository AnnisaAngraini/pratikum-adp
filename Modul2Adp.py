print("Selamat datang di Resto Kami")
print("============================")
print("Daftar Menu:")
print("--------------------------")
print("|    Paket   |    Harga  |")
print("|  Paket A   | Rp25.000  |")
print("|  Paket B   | Rp30.000  |")
print("|  Paket C   | Rp45.000  |")
print("--------------------------")
print("Harga ongkir:")
print("---------------------------------")
print("|    Jarak          |    Harga  |")
print("|Kurang dari 500m   | Gratis    |")
print("|500 - 1500 m       | Rp10.000  |")
print("|Lebih dari 1500 m  | Rp20.000  |")
print("---------------------------------")
print()
print ("FORMAT PESANAN")
print ("----------------------------------")
nama = input("Nama Pelanggan            : ")
p = input("Paket makanan (A/B/C)     : ").upper()

if p == 'A':
    print('Paket A                   Rp25.000')
    harga_paket = 25000
elif p == 'B':
    print('Paket B                   Rp30.000')
    harga_paket = 30000
elif p == 'C':
    print('Paket C                   Rp45.000')
    harga_paket = 45000
else:
    print('Paket yang Anda pilih tidak valid.')

jumlah_pesanan = int(input("Jumlah pesanan            : "))
s = float(input("Jarak rumah ke resto  (m) : "))

if s < 500:
    ongkir = 0
elif 500 <= s <= 1500:
    ongkir = 10000
else:
    ongkir = 20000

total_harga = (harga_paket * jumlah_pesanan) + ongkir
print("Total harga               Rp", total_harga)
print("------------Terima kasih----------")