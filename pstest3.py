import os

os.system ("cls")
class AlatMusik:
    def __init__(self, nama, jenis, status):
        self.nama = nama
        self.jenis = jenis
        self.status = status
        self.next_alat = None

class DaftarAlatMusik:
    def __init__(self):
        self.head = None

    def tambah_alat(self, nama, jenis, status):
        alat_musik = AlatMusik(nama, jenis, status)
        alat_musik.next_alat = self.head
        self.head = alat_musik

    def tampilkan_daftar(self):
        current_alat = self.head
        while current_alat is not None:
            print("Nama Alat Musik:", current_alat.nama)
            print("Jenis Alat Musik:", current_alat.jenis)
            print("Status Alat Musik:", current_alat.status)
            print("-------------------------------")
            current_alat = current_alat.next_alat

    def cari_alat(self, nama):
        current_alat = self.head
        while current_alat:
            if current_alat.nama == nama:
                return current_alat
            current_alat = current_alat.next_alat
        return None

    def update_alat(self, nama, jenis, status):
        alat_musik = self.cari_alat(nama)
        if alat_musik:
            alat_musik.jenis = jenis
            alat_musik.status = status
        else:
            print("Alat musik tidak ditemukan")

    def hapus_alat(self, nama):
        current_alat = self.head
        previous_alat = None
        while current_alat:
            if current_alat.nama == nama:
                if previous_alat:
                    previous_alat.next_alat = current_alat.next_alat
                else:
                    self.head = current_alat.next_alat
                return
            previous_alat = current_alat
            current_alat = current_alat.next_alat
        print("Alat musik tidak ditemukan")

    def input_data_alat(self):
        nama = input("Masukkan nama alat musik: ")
        jenis = input("Masukkan jenis alat musik: ")
        status = input("Masukkan status alat musik: ")
        self.tambah_alat(nama, jenis, status)
        print("Alat musik telah ditambahkan ke dalam daftar")

def tampilkan_menu():
    print("=== MENU ===")
    print("1. Tambah Alat Musik")
    print("2. Tampilkan Daftar Alat Musik")
    print("3. Cari Alat Musik")
    print("4. Update Alat Musik")
    print("5. Hapus Alat Musik")
    print("6. Keluar")

def jalankan_program():

    print ("Selamat datang di GGEZ Music Studio\n")
    while True:
        tampilkan_menu()
        pilihan = int(input("Masukkan pilihan Anda: "))
        print()

        if pilihan == 1:
            os.system ("cls")
            daftar_alat_musik.input_data_alat()
        
        elif pilihan == 2:
            os.system ("cls")
            daftar_alat_musik.tampilkan_daftar()
        
        elif pilihan == 3:
            os.system ("cls")
            nama = input("Masukkan nama alat musik yang ingin dicari: ")
            alat_musik = daftar_alat_musik.cari_alat(nama)
            if alat_musik:
                print("Nama Alat Musik:", alat_musik.nama)
                print("Jenis Alat Musik:", alat_musik.jenis)
                print("Status Alat Musik:", alat_musik.status)
            else:
                print("Alat musik tidak ditemukan")
        
        elif pilihan == 4:
            os.system ("cls")
            nama = input("Masukkan nama alat musik yang ingin diupdate: ")
            jenis = input("Masukkan jenis baru alat musik: ")
            status = input("Masukkan status baru alat musik: ")
            daftar_alat_musik.update_alat(nama, jenis, status)
            print("Data alat musik telah diupdate")
        
        elif pilihan == 5:
            os.system ("cls")
            nama = input("Masukkan nama alat musik yang ingin dihapus: ")
            daftar_alat_musik.hapus_alat(nama)
            print("Data alat musik telah dihapus")
        
        elif pilihan == 6:
            os.system ("cls")
            print("Terima Kasih telah berkunjung :)")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


daftar_alat_musik = DaftarAlatMusik()

daftar_alat_musik.tambah_alat("Gitar", "Senar", "Tersedia")
daftar_alat_musik.tambah_alat("Drum", "Pukul", "Tidak Tersedia")
daftar_alat_musik.tambah_alat("Bass", "Senar", "Tersedia")
daftar_alat_musik.tambah_alat("Keyboard", "Elektronik", "Tidak Tersedia")


jalankan_program()