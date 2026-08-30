koleksi_lagu = []

def tambah_lagu():
    judul = input("Masukkan judul lagu: ")
    penyanyi = input("Masukkan nama penyanyi: ")

    lagu = {
        "judul": judul,
        "penyanyi": penyanyi
    }

    koleksi_lagu.append(lagu)
    print("Lagu berhasil ditambahkan!")

def tampilkan_lagu():
    if len(koleksi_lagu) == 0:
        print("Koleksi lagu masih kosong.")
    else:
        print("\n=== KOLEKSI LAGU ===")
        for i, lagu in enumerate(koleksi_lagu, 1):
            print(f"{i}. {lagu['judul']} - {lagu['penyanyi']}")

def hapus_lagu():
    judul = input("Masukkan judul lagu yang ingin dihapus: ")

    for lagu in koleksi_lagu:
        if lagu["judul"].lower() == judul.lower():
            koleksi_lagu.remove(lagu)
            print("Lagu berhasil dihapus!")
            return

    print("Lagu tidak ditemukan.")

def cari_lagu():
    penyanyi = input("Masukkan nama penyanyi: ")

    ditemukan = False

    for lagu in koleksi_lagu:
        if lagu["penyanyi"].lower() == penyanyi.lower():
            print(f"{lagu['judul']} - {lagu['penyanyi']}")
            ditemukan = True

    if not ditemukan:
        print("Lagu dari penyanyi tersebut tidak ditemukan.")

while True:
    print("\n=== MENU KOLEKSI LAGU ===")
    print("1. Tambah lagu")
    print("2. Tampilkan semua lagu")
    print("3. Hapus lagu")
    print("4. Cari lagu berdasarkan penyanyi")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_lagu()
    elif pilihan == "2":
        tampilkan_lagu()
    elif pilihan == "3":
        hapus_lagu()
    elif pilihan == "4":
        cari_lagu()
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")