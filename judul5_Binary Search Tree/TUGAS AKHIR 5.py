class Buku:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.kiri = None
        self.kanan = None


class LemariBuku:
    def __init__(self):
        self.root = None

    def tambah_buku_node(self, root, id_buku, judul):
        if root is None:
            return Buku(id_buku, judul)
        if id_buku < root.id_buku:
            root.kiri = self.tambah_buku_node(root.kiri, id_buku, judul)
        elif id_buku > root.id_buku:
            root.kanan = self.tambah_buku_node(root.kanan, id_buku, judul)
        return root

    def tambah_buku(self, id_buku, judul):
        self.root = self.tambah_buku_node(self.root, id_buku, judul)

    def cari_buku_terkecil(self, root):
        current = root
        while current is not None and current.kiri is not None:
            current = current.kiri
        return current

    def hapus_buku_node(self, root, id_buku):
        if root is None:
            return None
        if id_buku < root.id_buku:
            root.kiri = self.hapus_buku_node(root.kiri, id_buku)
        elif id_buku > root.id_buku:
            root.kanan = self.hapus_buku_node(root.kanan, id_buku)
        else:
            if root.kiri is None and root.kanan is None:
                return None
            elif root.kiri is None:
                return root.kanan
            elif root.kanan is None:
                return root.kiri
            else:
                pengganti = self.cari_buku_terkecil(root.kanan)
                root.id_buku = pengganti.id_buku
                root.judul = pengganti.judul
                root.kanan = self.hapus_buku_node(root.kanan, pengganti.id_buku)
        return root

    def hapus_buku(self, id_buku):
        self.root = self.hapus_buku_node(self.root, id_buku)

    def tinggi_lemari(self, root):
        if root is None:
            return -1
        tinggi_kiri = self.tinggi_lemari(root.kiri)
        tinggi_kanan = self.tinggi_lemari(root.kanan)
        return 1 + max(tinggi_kiri, tinggi_kanan)

    def tampil_level_order(self, root):
        if root is None:
            print("(kosong)")
            return
        antrian = [root]
        while len(antrian) > 0:
            current = antrian.pop(0)
            print(f"{current.id_buku} - {current.judul}", end=" | ")
            if current.kiri is not None:
                antrian.append(current.kiri)
            if current.kanan is not None:
                antrian.append(current.kanan)
        print()

    def cari_successor(self, root, id_buku):
        current = root
        successor = None
        while current is not None:
            if id_buku < current.id_buku:
                successor = current
                current = current.kiri
            elif id_buku > current.id_buku:
                current = current.kanan
            else:
                break
        if current is None:
            return None, False
        if current.kanan is not None:
            successor = self.cari_buku_terkecil(current.kanan)
        if successor is None:
            return None, False
        return (successor.id_buku, successor.judul), True

    def cari_predecessor(self, root, id_buku):
        current = root
        predecessor = None
        while current is not None:
            if id_buku > current.id_buku:
                predecessor = current
                current = current.kanan
            elif id_buku < current.id_buku:
                current = current.kiri
            else:
                break
        if current is None:
            return None, False
        if current.kiri is not None:
            temp = current.kiri
            while temp.kanan is not None:
                temp = temp.kanan
            predecessor = temp
        if predecessor is None:
            return None, False
        return (predecessor.id_buku, predecessor.judul), True


def main():
    lemari = LemariBuku()
    pilih = 0
    while pilih != 7:
        print("\n=== Lemari Buku (BST Lanjutan) ===")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Tampilkan Level-order")
        print("4. Tinggi Lemari")
        print("5. Successor Buku")
        print("6. Predecessor Buku")
        print("7. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                x = int(input("Masukkan ID Buku: "))
                j = input("Masukkan Judul Buku: ")
                lemari.tambah_buku(x, j)
                print(f"Buku {j} (ID {x}) berhasil dimasukkan")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            try:
                x = int(input("Hapus ID Buku: "))
                lemari.hapus_buku(x)
                print(f"Buku dengan ID {x} berhasil dihapus")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 3:
            print("Level-order: ", end="")
            lemari.tampil_level_order(lemari.root)
        elif pilih == 4:
            print(f"Tinggi lemari: {lemari.tinggi_lemari(lemari.root)}")
        elif pilih == 5:
            try:
                x = int(input("Cari successor dari ID Buku: "))
                ans, found = lemari.cari_successor(lemari.root, x)
                if found:
                    print(f"Successor: ID {ans[0]} - {ans[1]}")
                else:
                    print("Tidak ada successor")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 6:
            try:
                x = int(input("Cari predecessor dari ID Buku: "))
                ans, found = lemari.cari_predecessor(lemari.root, x)
                if found:
                    print(f"Predecessor: ID {ans[0]} - {ans[1]}")
                else:
                    print("Tidak ada predecessor")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 7:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
