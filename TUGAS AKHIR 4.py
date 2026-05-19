class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top_ptr = None

    def is_empty(self):
        return self.top_ptr is None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top_ptr
        self.top_ptr = new_node
        print(f"Piring {x} telah ditambahkan ke rak")

    def pop(self):
        if self.is_empty():
            print("Piring di rak kosong")
            return
        temp = self.top_ptr
        print(f"Piring {temp.data} telah diambil dari rak")
        self.top_ptr = self.top_ptr.next

    def peek(self):
        if self.is_empty():
            print("Rak kosong")
            return
        print(f"Piring teratas: {self.top_ptr.data}")

    def display(self):
        if self.is_empty():
            print("Rak kosong")
            return
        print("Isi piring dirak (atas ke bawah): ", end="")
        current = self.top_ptr
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


def main():
    stack = StackLinkedList()
    pilih = 0
    while pilih != 6:
        print("\n=== STACK (Linked List) ===")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Tampilkan")
        print("5. Hitung Total Piring")
        print("6. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                val = (input("Warna piring: "))
                stack.push(val)
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            stack.pop()
        elif pilih == 3:
            stack.peek()
        elif pilih == 4:
            stack.display()
        elif pilih == 5:
            count = 0
            current = stack.top_ptr
            while current is not None:
                count += 1
                current = current.next
            print(f"Total piring di rak: {count}")
        elif pilih == 6:
            while not stack.is_empty():
                stack.pop()
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
