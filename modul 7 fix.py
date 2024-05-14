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

# Hitung Mean
def rata2(data):
    jumlah = 0
    for nilai in data:
        jumlah += nilai
    total = jumlah / n
    return total

# Hitung Variance   
def variance(data):
    mean = rata2(data)
    variance = 0
    for x in data:
        variance += (x - mean) ** 2
        total_variance= variance/n
    return total_variance

# Hitung modus
def modus(data):
    x = [0] * n  
    for i in range(n):
        for j in range(n):
            if data[i] == data[j]:
                x[i] += 1

    max_x = x[0]
    for y in x:
        if y > max_x:
            max_x = y

    if max_x == 1:
        return "-"
    else:
        modus = []
        for i in range(n):
            if x[i] == max_x and data[i] not in modus:
                modus.append(data[i])
        return modus

#tampilkan hasil
def tampilan(data):
    a = rata2(data)
    b = modus(data)
    c = variance(data)
    print("------------------------")
    print(f"|{'Mean':10}| {a:^10.2f}|")
    if b == "-":
        b_str = "-"
    else:
        b_str = ""
        for i in range(len(b)):
            if i > 0:
                b_str += ", "
            b_str += str(b[i])
    print(f"|{'Modus':10}| {b_str:^10}|")
    print(f"|{'Variance':10}| {c:^10.2f}|")
    print("------------------------")

# Panggil fungsi
data = input_data(n)
tampilan(data)
