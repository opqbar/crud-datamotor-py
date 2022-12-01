import csv
import os

csv_filename = 'Motor.csv'

'''
clear_scr untuk menghapus yang ada di terminal.
'''
def clear_scr():
    os.system('cls' if os.name == 'nt' else 'clear')

'''
Menampilkan fungsi Menu pada terminal
'''
def tampil_menu():

    clear_scr()
# Menghitung jumlah row data pada csv
    Motor = []
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Motor.append(row)
    row_count = sum(1 for row in Motor)

    print("============= Showroom Motor Berkah =============")
    print("== Aplikasi Sederhana Pendataan Showroom Motor ==\n")
    print("===================== Menu ======================")
    print("-> Stok Motor : ",row_count)  
    print("=================================================")
    print("[1] Tambah Stok Motor")
    print("[2] Lihat Stok Motor")
    print("[3] Edit Stok Motor")
    print("[4] Hapus Stok Motor")
    print("[5] Cari Motor")
    print("[0] Keluar Aplikasi \n")
    print("=================================================")
    pilih_menu = input("Pilih menu > ")
    
    # Memilih menu dalam percabangan
    if(pilih_menu == "1"):
        tambah_motor()
    elif(pilih_menu == "2"):
        lihat_motor()
    elif(pilih_menu == "3"):
        edit_motor()
    elif(pilih_menu == "4"):
        hapus_motor()
    elif(pilih_menu == "5"):
        cari_motor()
    elif(pilih_menu == "0"):
        exit()
    else:
        print("Menu tidak tersedia!")
        balik_menu()

# Fungsi untuk Menambah stok Motor (Create)
def tambah_motor():
    clear_scr()
    with open(csv_filename, mode='a',newline='') as csv_file:
        fieldnames = ['Kode', 'Model', 'Harga','Jumlah']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print("=================================================")
        print("================== Tambah Motor =================")
        print("=================================================\n")
        
        Kode = input("Kode Motor : ")
        Model = input("Model Motor : ")
        Harga = input("Harga Motor : ")
        Jumlah = input("Stok Motor : ")

        print("=================================================")


        writer.writerow({'Kode': Kode, 'Model': Model, 'Harga': Harga, 'Jumlah': Jumlah})    
    
    balik_menu()

# Fungsi untuk Melihat stok Motor (Read)
def lihat_motor():
    clear_scr()
    Motor = []
    
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Motor.append(row)

    row_count = sum(1 for row in Motor)

    print("-" * 50)
    print("\t\tDaftar Stok Motor")
    print("-" * 50)

    print("Kode \t Model \t\t Harga \t\t Jumlah")
    print("-" * 50)

    # Mengambil datanya dengan looping
    for data in Motor:
        print(f"{data['Kode']} \t {data['Model']} \t Rp.{data['Harga']} \t {data['Jumlah']} \t |")
    print("-" * 50)
    print("Total Data: ",row_count)
    print("-" * 50)
    
    balik_menu()

# Fungsi untuk Mengubah data stok Motor (Edit)
def edit_motor():
    clear_scr()
    Motor = []

    with open(csv_filename, mode="r",newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Motor.append(row)
    row_count = sum(1 for row in Motor)

    print("-" * 50)
    print("\t\tDaftar Stok Motor")
    print("-" * 50)

    print("Kode \t Model \t\t Harga \t\t Jumlah")
    print("-" * 50)

    for data in Motor:
        print(f"{data['Kode']} \t {data['Model']} \tRp.{data['Harga']} \t{data['Jumlah']}")

    print("-" * 50)
    print("Total Data :",row_count)
    print("-" * 50,"\n")
    kode = input("Pilih Kode Motor : ")
    model = input("Model Baru: ")
    harga = input("Harga Baru: ")
    Jumlah = input("Stok Baru: ")

# Mencari indeks di setiap csv dan mengubah datanya dari input
    indeks = 0
    for data in Motor:
        if (data['Kode'] == kode):
            Motor[indeks]['Model'] = model
            Motor[indeks]['Harga'] = harga
            Motor[indeks]['Jumlah'] = Jumlah
        indeks = indeks + 1

# Me-replace data yang baru ke file csv
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['Kode', 'Model', 'Harga','Jumlah']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Motor:
            writer.writerow({'Kode': new_data['Kode'], 'Model': new_data['Model'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']}) 

    balik_menu()

# Fungsi untuk menghapus stok Motor
def hapus_motor():
    clear_scr()
    Motor = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Motor.append(row)

    print("Kode \t Model \t\t Harga \t Jumlah")
    print("-" * 50)

    for data in Motor:
        print(f"{data['Kode']} \t {data['Model']} \t {data['Harga']} \t {data['Jumlah']}")

    print("-" * 50,"\n")
    kode = input("Masukkan Kode Motor yang ingin dihapus : ")

    indeks = 0
    for data in Motor:
        if (data['Kode'] == kode):
            Motor.remove(Motor[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['Kode', 'Model', 'Harga', 'Jumlah']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Motor:
            writer.writerow({'Kode': new_data['Kode'], 'Model': new_data['Model'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']}) 

    print("Data Motor Telah terhapus.")
    balik_menu()

#Fungsi untuk mencari data Stok Motor
def cari_motor():
    clear_scr()
    Motor = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Motor.append(row)

    kode = input("Mencari motor dengan Kode : ")

    data_motor = []

    indeks = 0
    for data in Motor:
        if (data['Kode'] == kode):
            data_motor = Motor[indeks]
            
        indeks = indeks + 1

    if len(data_motor) > 0:
        print("Data Ditemukan dengan rincian :")
        print(f"Model : {data_motor['Model']}")
        print(f"Harga : Rp.{data_motor['Harga']}")
        print(f"Jumlah :{data_motor['Jumlah']}")
    else:
        print("Data tidak ditemukan.")
    balik_menu()

# Fungsi untuk kembali ke Pilih Menu
def balik_menu():
    print("\n")
    input("Tekan Enter untuk kembali ke Menu...")
    tampil_menu()

if __name__ == "__main__":
    while True:
        tampil_menu()