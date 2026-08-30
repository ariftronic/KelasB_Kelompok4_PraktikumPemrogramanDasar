class Dosen:
    def __init__(self, nama, nidn, mata_kuliah):
        self.nama = nama
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

    def info(self):
        print("Nama Dosen     :", self.nama)
        print("NIDN           :", self.nidn)
        print("Mata Kuliah    :", self.mata_kuliah)

    def update_mata_kuliah(self, mk_baru):
        self.mata_kuliah = mk_baru

dosen1 = Dosen("Budi Santoso", "0123456789", "Pemrograman Python")
dosen2 = Dosen("Siti Aminah", "0234567890", "Basis Data")
dosen3 = Dosen("Andi Wijaya", "0345678901", "Jaringan Komputer")

print("=== DATA DOSEN 1 ===")
dosen1.info()

print("=== DATA DOSEN 2 ===")
dosen2.info()

print("=== DATA DOSEN 3 ===")
dosen3.info()

print("=== SETELAH UPDATE MATA KULIAH ===")
dosen1.update_mata_kuliah("Pemrograman Berorientasi Objek")
dosen1.info()
