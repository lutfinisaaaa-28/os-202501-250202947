import time

print("Memulai komputasi CPU...")
x = 0
for i in range(10**7):
    x += i

print("Selesai komputasi CPU")

print("Memulai alokasi memori...")
data = []
try:
    for i in range(50):
        data.append("X" * 10**6)  # 1 MB
        print(f"Alokasi memori: {len(data)} MB")
        time.sleep(0.1)
except MemoryError:
    print("MemoryError: batas memori tercapai")

print("Program selesai")

