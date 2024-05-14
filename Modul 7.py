print("Program Pengolahan Data dengan Fungsi")
print("-------------------------------------")
n = int(input("Banyak n data: "))

# input data
def input_data(n):
    data = []
    for i in range(n):
        nilai = int(input(f"Masukkan data ke-{i+1} : "))
        data.append(nilai)
    return data

# Hitung rata-rata
def rata2(data):
    return sum(data) / n
    
# Mengurutkan data
def urutan(data):
    p = len(data)
    for i in range(p):
        for j in range(0, p - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

# Cari median
def median(data):
    urutan(data)  
    p = len(data)
    if p % 2 == 0:
        return (data[p // 2 - 1] + data[p // 2]) / 2
    else:
        return data[p // 2]

# Cari modus
def modus(data):
    x = [0] * len(data)  
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] == data[j]:
                x[i] += 1

    max_x = max(x)
    if max_x == 1:
        return "-"
    else:
        modus = []
        for i in range(len(data)):
            if x[i] == max_x and data[i] not in modus:
                modus.append(data[i])
        return modus

# Tampilkan hasil
def tampilan(data):
    print("-----------------------")
    print(f"|{'Rata-rata':^10}|{rata2(data):^10.3f}|")
    print(f"|{'Median':^10}|{median(data):^10}|")
    print(f"|{'Modus':^10}|{', '.join(map(str, modus(data))) if modus(data) != '-' else '-':^10}|")
    print("-----------------------")

# Panggil fungsi
data = input_data(n)
tampilan(data)
