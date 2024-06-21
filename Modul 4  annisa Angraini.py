#Program Toko Sembako
print("|-----------------------------------------------|")
print("|     Selamat datang di Toko Sembako ICHA       |")
print("|-----------------------------------------------|")
print("Daftar barang yang tersedia")
nama_barang = ["Beras ", "Telur ", "Gula  ", "Tepung", "Kopi  ", "Minyak"]
harga = [17000, 20000, 16000, 10000, 15000, 25000]
for i in range(len(nama_barang)):
    print(f"{i + 1}. {nama_barang[i]}          Rp{harga[i]}/kg")

print("|-----------------------------------------------|")
print("PROMO !!!!!")
print("Beli >= 2 kg kopi, DISKON 10%")
print("Total belanja diatas Rp250.000, DISKON 15%")
print("|-----------------------------------------------|")
nama = str(input("Nama pelanggan : "))
no_hp = (input("No Handphone   : "))
print("      Note : Ketik 0 untuk selesai")

total_belanja = 0
pesanan = {}
while True:
    no_barang = input("Barang yang dipesan (1-6)     : ")
    if no_barang == '0':
        break
    elif no_barang > '6':
        print ("Masukkan kode barang yang benar")
        break
    else:
        jumlah_kg = float(input("Jumlah kg yang ingin dipesan  : "))
        if jumlah_kg <= 0:
            print("Jumlah kg tidak boleh 0.")
            continue
        else:
            kode_barang = int(no_barang) - 1
            harga_barang = harga[kode_barang] * jumlah_kg
            pesanan [nama_barang[kode_barang]] = {'harga_per_kg': harga[kode_barang], 'jumlah_kg': jumlah_kg, 'harga_barang': harga_barang}
            total_belanja += harga_barang

# Hitung diskon
    diskon_kopi = 0
    diskon_total = 0
if 'Kopi  ' in pesanan and pesanan['Kopi  ']['jumlah_kg'] >= 2:
    diskon_kopi = pesanan['Kopi  ']['harga_barang'] * 0.1
if total_belanja > 250000:
    diskon_total = total_belanja * 0.15
total_pembayaran = total_belanja - diskon_kopi - diskon_total

print("|-----------------------------------------------|")
print("                Struck Pembayaran                ")
print("Nama Pelanggan   : ",nama)
print("No Handphone     : ",no_hp)
for barang, detail in pesanan.items():
    print(f"{barang} - {detail['jumlah_kg']} kg x Rp{detail['harga_per_kg']} = Rp{detail['harga_barang']}")
    
print(f"Total Belanja    : Rp{total_belanja}")
if diskon_kopi > 0:
    print(f"Diskon  Kopi     : Rp{diskon_kopi}")
if diskon_total > 0:
    print(f"Diskon Total Belanja: Rp{diskon_total}")
print(f"Total Pembayaran : Rp{total_pembayaran}")

jumlah_uang=float(input("Jumlah uang      : "))
kembalian = jumlah_uang-total_pembayaran
print("Kembalian        :", kembalian)
print("      Terima kasih telah berbelanja ^_^          ")

