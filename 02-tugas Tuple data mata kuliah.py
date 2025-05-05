matkul_list = []

jumlah = int(input("Input jumlah mata kuliah: 3 "))

for i in range(jumlah):
    print(f"\nMata kuliah ke-{i+1}:")
    kode = input("Kode:rpl01 ")
    nama = input("Nama:filsat ")
    sks = int(input("SKS:3 "))
    matkul = (kode, nama, sks)
    matkul_list.append(matkul)

    for i in range(jumlah):2
    print(f"\nMata kuliah ke-{i+2}:")
    kode = input("Kode:rpl02 ")
    nama = input("Nama:Algoritma ")
    sks = int(input("SKS:4 "))
    matkul = (kode, nama, sks)
    matkul_list.append(matkul)

    for i in range(jumlah):3
    print(f"\nMata kuliah ke-{i+3}:")
    kode = input("Kode:rpl03 ")
    nama = input("Nama:Basis data ")
    sks = int(input("SKS:3 "))
    matkul = (kode, nama, sks)
    matkul_list.append(matkul)

    print("\nDaftar Mata Kuliah:")
for m in matkul_list:
    print(m)

    total_sks = sum(m[2] for m in matkul_list)
print(f"\nTotal SKS: 10 {total_sks}")