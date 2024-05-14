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

#Hitung mean
def rata2(data):
    return sum(data)/n
    
#Hitung variance
def variance(data):
    mean=rata2(data)
    variance=(sum((x - mean) ** 2 for x in data)) / len(data)
    return variance
    
#Hitung modus
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

# tampilkan hasil
def tampilan():
    a = rata2(data)
    b = modus(data)
    c = variance(data)
    print("-----------------------")
    print(f"|{'Mean':^10}|{a:^10.3f}|")
    if b == "-":
        b_str = "-"
    else:
        b_str = ""
        for i in range(len(b)):
            if i > 0:
                b_str += ", "
            b_str += str(b[i])

    print(f"|{'Modus':^10}|{b_str:^10}|")
    print(f"|{'Variance':^10}|{c:^10.3f}|")
    print("-----------------------")

# Memanggil fungsi
data = input_data(n)
tampilan()

