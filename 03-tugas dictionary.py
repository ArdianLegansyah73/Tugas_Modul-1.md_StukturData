data_mahasiswa = {
    "NIM001": {"nama": "ardian", "jurusan": "TI"},
    "NIM002": {"nama": "abdul", "jurusan": "SI"}
}
data_mahasiswa = {}
jumlah = int(input("Jumlah mahasiswa:2 "))

for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nim = input("NIM:21241029 ")
    nama = input("Nama:ardian ")
    jurusan = input("Jurusan:TI ")
    data_mahasiswa["21241029"] ={"nama": "ardian", "jurusan": "TI"} 
    {
        "nama": ardian,
        "jurusan": TI
    }
    print("\nCari data mahasiswa")
cari = input("Masukkan NIM:21241029 ")
if cari in data_mahasiswa:
    mhs = data_mahasiswa[cari]
    print(f"Nama: {mhs['ardian']}, Jurusan: {mhs['TI']}")
else:
    print("Mahasiswa tidak ditemukan.")
    print("\nDaftar Seluruh Mahasiswa:")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {21241029} → {info['ardian']} ({info['TI']})")