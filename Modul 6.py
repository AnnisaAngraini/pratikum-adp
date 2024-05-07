print("Program Operasi Matriks Dengan Array 2D")
print("----------------------------------------")
#input banyak kolom dan baris matriks
n = int(input("Masukkan ukuran Matriks n x n: "))

# Input dan cetak matriks  A dan B
print("Masukkan entri-entri Matriks A")
A = []
for i in range(n):
    baris = []
    for j in range(n):
        entri = int(input(f"Entri [{i+1},{j+1}]: ")) 
        baris.append(entri)
    A.append(baris)
print()    
print("Matriks A:")
for baris in A:
    print(baris)
print("----------------------------------------")

print("Masukkan entri-entri Matriks B")
B = []
for i in range(n):
    baris = []
    for j in range(n):
        entri = int(input(f"Entri [{i+1},{j+1}]: ")) 
        baris.append(entri)
    B.append(baris)
print()
print ("Matriks B:")
for baris in B:
    print(baris)

# Perkalian Matriks A dan B
print("----------------------------------------")
print("Perkalian Matriks A dan B")
print("Matriks C:")
C = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]
for baris in C:
    print(baris)

# Transposo A + Transpose B
print("----------------------------------------")
print("Penjumlahan Transpose A dan Transpose B:")
print("Matriks D:")
AT = [[A[j][i] for j in range(n)] for i in range(n)] 
BT = [[B[j][i] for j in range(n)] for i in range(n)]  
AT_BT=[[AT[i][j] + BT[i][j] for j in range(n)] for i in range(n)]  
for baris in AT_BT:  
    print(baris)
print("----------------------------------------")

