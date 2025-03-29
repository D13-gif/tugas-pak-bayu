# menghitung biaya pengiriman
## masukan berat paket dan tarif pengiriman
weight = float(input("Masukkan berat paket (kg): "))
rate = float(input("Masukkan tarif per kg: "))
## menghitung biaya pengiriman
shipping_cost = weight * rate
## menampilkan hasil
print(f"Shipping Cost: {shipping_cost} IDR")
