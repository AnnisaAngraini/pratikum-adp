print("Program Data Film dengan Text File dan Dictionary")
print("-------------------------------------------------")

# Fungsi tambah data
def add(judul, penulis, sutradara, rilis):
    with open("film_data.txt", "a") as file:
        file.write(f"{judul},{penulis},{sutradara},{rilis}\n")
    print("Data film berhasil ditambahkan!")

# Fungsi hapus
def delete(judul):
    with open("film_data.txt", "r") as file:
      lines = file.readlines()
    with open("film_data.txt", "w") as file:
      for line in lines:
        if line.split(",")[0] != judul:
          file.write(line)
      print("Data film berhasil dihapus!")

# Fungsi edit data
def edit(judul, penulis, sutradara, rilis):
    with open("film_data.txt", "r") as file:
      lines = file.readlines()
    with open("film_data.txt", "w") as file:
      found = False
      for line in lines:
        if line.split(",")[0] == judul:
          file.write(f"{judul},{penulis},{sutradara},{rilis}\n")
          found = True
        else:
          file.write(line)
        if found:
            print("Data film berhasil diubah.")
        else:
            print("Judul film tidak ditemukan.")

# Fungsi menampilkan  data  
def show():
  with open("film_data.txt", "r") as file:
    data_film = file.readlines()
    if data_film:
        print("Database Film:")
        for data in data_film:
          print(data.strip())
    else:
      print("Database film tidak ada!")

print("Menu:")
print("1. Tambah Film")
print("2. Hapus Film")
print("3. Edit Film")
print("4. Tampilkan Semua Film")
print("5. Keluar")
print("--------------------------")
while True:    
    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        judul     = input("Judul film           : ")
        penulis   = input("Nama penulis skenario: ")
        sutradara = input("Nama sutradara       : ")
        rilis     = input("Tahun rilis          : ")
        add(judul, penulis, sutradara, rilis)
        print()
    elif pilihan == "2":
        judul = input("Judul film yang akan dihapus: ")
        delete(judul)
        print()
    elif pilihan == "3":
        judul     = input("Masukkan judul film yang akan diubah: ")
        penulis   = input("Nama penulis skenario baru          : ")
        sutradara = input("Nama sutradara baru                 : ")
        rilis     = input("Tahun rilis baru                    : ")
        edit(judul, penulis, sutradara, rilis)
        print()
    elif pilihan == "4":
        show()
        print()
    elif pilihan == "5":
        print("Terima kasih telah menggunakan program ini.")
        print()
        break
    else:
        print("Pilihan tidak valid")
