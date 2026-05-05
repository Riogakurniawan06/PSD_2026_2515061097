# Percobaan II-1: Bubble Sort (Implementasi Tinggi Badan Mahasiswa PSTI)

def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tukar(arr, j, j + 1)

def main():
    try:
        n = int(input("Masukkan jumlah mahasiswa: "))
    except ValueError:
        print("Input tidak valid!")
        return

    tinggi = []
    print("Masukkan tinggi badan mahasiswa (dalam cm):")
    for i in range(n):
        while True:
            try:
                nilai = int(input(f"Tinggi mahasiswa ke-{i+1}: "))
                tinggi.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")

    print(f"Data tinggi sebelum diurutkan: {tinggi}")
    bubble_sort(tinggi, n)
    print("Data tinggi setelah diurutkan (Bubble Sort):", end=" ")
    for i in range(n):
        print(tinggi[i], end=" ")
    print()

if __name__ == "__main__":
    main()
