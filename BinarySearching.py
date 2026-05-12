def cari_sepatu(rak_sepatu, jumlah, ukuran_dicari):
    kiri = 0
    kanan = jumlah - 1
    posisi = -1

    while kiri <= kanan:
        tengah = kiri + (kanan - kiri) // 2
        print(f"Cek rak posisi {tengah}, ukuran sepatu: {rak_sepatu[tengah]}")

        if rak_sepatu[tengah] == ukuran_dicari:
            posisi = tengah
            break
        elif rak_sepatu[tengah] < ukuran_dicari:
            print("Cari di rak sebelah kanan (ukuran lebih besar)")
            kiri = tengah + 1
        else:
            print("Cari di rak sebelah kiri (ukuran lebih kecil)")
            kanan = tengah - 1
    return posisi


def main():
    try:
        jumlah = int(input("Masukkan jumlah sepatu di rak: "))
    except ValueError:
        print("Input salah, harus angka!")
        return

    rak_sepatu = []
    print("Masukkan ukuran sepatu (urut menaik):")
    for i in range(jumlah):
        while True:
            try:
                ukuran = int(input())
                rak_sepatu.append(ukuran)
                break
            except ValueError:
                print("Input salah, coba lagi!")

    print(f"Rak sepatu: {rak_sepatu}")

    while True:
        try:
            ukuran_dicari = int(input("Masukkan ukuran sepatu yang dicari: "))
            break
        except ValueError:
            print("Input salah, coba lagi!")

    posisi = cari_sepatu(rak_sepatu, jumlah, ukuran_dicari)
    if posisi != -1:
        print(f"Sepatu ukuran {ukuran_dicari} ditemukan di rak posisi ke-{posisi}")
    else:
        print("Sepatu dengan ukuran tersebut tidak ada di rak")


if __name__ == "__main__":
    main()