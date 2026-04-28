class PatientNode:
    def __init__(self, name):
        self.name = name
        self.next = None

class HospitalQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, name):
        new_patient = PatientNode(name)
        if self.rear is None:
            self.front = self.rear = new_patient
        else:
            self.rear.next = new_patient
            self.rear = new_patient

    def dequeue(self):
        if self.front is None:
            print("Antrian kosong, tidak ada pasien.")
            return None
        served = self.front.name
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print("Pasien dilayani:", served)
        return served

    def show_queue(self):
        current = self.front
        print("\nDaftar Antrian Pasien:")
        if current is None:
            print("Antrian kosong.")
        while current:
            print("-", current.name)
            current = current.next


queue = HospitalQueue()

n = int(input("Berapa banyak pasien yang ingin ditambahkan ke antrian? "))
for i in range(n):
    nama = input(f"Masukkan nama pasien ke-{i+1}: ")
    queue.enqueue(nama)

queue.show_queue()

print("\nProses pelayanan:")
queue.dequeue()
queue.show_queue()
