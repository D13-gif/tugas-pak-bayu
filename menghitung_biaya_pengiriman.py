# menghitung biaya pengiriman
## masukan berat paket dan tarif pengiriman
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))
## menghitung biaya pengiriman
shipping_cost = weight * rate
## menampilkan hasil
print(f"Shipping Cost: {shipping_cost} IDR")
