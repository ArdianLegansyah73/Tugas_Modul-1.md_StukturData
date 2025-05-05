data_Mahasiswa = []
jumlah = int(input("Input jumlah Mahasiswa:2 "))


for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nama = input("Nama:ardian ")
    nilai = list(map(int, input("Masukkan 3 nilai dipisahkan spasi:80 85 90 ").split()))
    rata2 = sum(nilai) / len(nilai)
    data_Mahasiswa.append([nama, nilai, rata2])
  
print("\nData Mahasiswa:")
print("Nama\tNilai\t\tRata-rata")
for Mahasiswa in data_Mahasiswa:
    print(f"{Mahasiswa[nama]}\t{Mahasiswa[nilai]}\t{Mahasiswa[rata2]:.2f}")

   
print("\nMahasiswa Lulus (>= 75):")
for Mahasiswa in data_Mahasiswa:
    if Mahasiswa[2] >= 75:
        print(f"{Mahasiswa[0]} - {Mahasiswa[2]:.2f}")