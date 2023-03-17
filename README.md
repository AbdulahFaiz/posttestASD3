# posttestASD3

Nama  : Abdulah Faiz Tedjo Putro

NIM   : 2209116026

Kelas : Sistem Infromasi A 2022


**Penjelasan**

![image](https://user-images.githubusercontent.com/121870536/225684561-d91c98e4-e620-4389-ae49-064474131589.png)

class AlatMusik: adalah definisi kelas AlatMusik yang akan digunakan untuk membuat objek-objek alat musik.

def __init__(self, nama, jenis, status): adalah method __init__() yang merupakan constructor atau method yang dipanggil saat objek dibuat. self merujuk pada objek yang akan dibuat, sedangkan nama, jenis, dan status adalah parameter yang harus diberikan nilai saat objek dibuat.

self.nama = nama adalah atribut nama pada objek yang baru dibuat diinisialisasi dengan nilai nama yang diberikan saat objek dibuat.

self.jenis = jenis adalah atribut jenis pada objek yang baru dibuat diinisialisasi dengan nilai jenis yang diberikan saat objek dibuat.

self.status = status adalah atribut status pada objek yang baru dibuat diinisialisasi dengan nilai status yang diberikan saat objek dibuat.

self.next_alat = None adalah atribut next_alat pada objek yang baru dibuat diinisialisasi dengan nilai None. Atribut ini akan digunakan untuk menghubungkan objek AlatMusik satu dengan objek AlatMusik lainnya pada saat kita membuat suatu struktur data seperti linked list atau stack.

![image](https://user-images.githubusercontent.com/121870536/225685706-356f6054-7ec0-461b-b79b-fa62013b4241.png)


class DaftarAlatMusik: adalah definisi kelas DaftarAlatMusik yang akan digunakan untuk membuat sebuah daftar (list) alat musik.

def __init__(self): adalah method __init__() yang merupakan constructor atau method yang dipanggil saat objek dibuat. self merujuk pada objek yang akan dibuat.

self.head = None adalah atribut head pada objek yang baru dibuat diinisialisasi dengan nilai None. Atribut ini akan digunakan untuk menunjukkan elemen pertama pada daftar alat musik yang terdiri dari objek AlatMusik.

![image](https://user-images.githubusercontent.com/121870536/225685876-08cd3884-2689-4902-b43f-60b9995673d7.png)

def tambah_alat(self, nama, jenis, status): adalah definisi method tambah_alat() yang akan digunakan untuk menambahkan objek AlatMusik baru ke dalam daftar alat musik.

alat_musik = AlatMusik(nama, jenis, status) adalah membuat objek AlatMusik baru dengan memanggil constructor pada kelas AlatMusik dan melewatkan parameter nama, jenis, dan status yang diterima dari method tambah_alat().

alat_musik.next_alat = self.head adalah mengatur nilai atribut next_alat dari objek alat_musik menjadi self.head. Hal ini dilakukan untuk menghubungkan objek alat_musik dengan elemen pertama pada daftar alat musik.

self.head = alat_musik adalah mengatur nilai atribut head dari objek self menjadi alat_musik. Hal ini dilakukan untuk menunjukkan bahwa elemen pertama pada daftar alat musik adalah alat_musik.

![image](https://user-images.githubusercontent.com/121870536/225686267-55dc1502-3733-4743-a4de-9ae632b662fe.png)

def tampilkan_daftar(self): adalah definisi method tampilkan_daftar() yang akan digunakan untuk menampilkan daftar alat musik.

current_alat = self.head adalah menginisialisasi variabel current_alat dengan nilai atribut head dari objek self. Variabel ini akan digunakan untuk menyimpan posisi saat ini dalam daftar alat musik.

while current_alat is not None: adalah sebuah perulangan yang akan dilakukan selama current_alat bukan None. Hal ini dilakukan untuk menampilkan setiap elemen pada daftar alat musik.

print("Nama Alat Musik:", current_alat.nama) adalah mencetak nama alat musik yang disimpan pada atribut nama dari objek current_alat.

print("Jenis Alat Musik:", current_alat.jenis) adalah mencetak jenis alat musik yang disimpan pada atribut jenis dari objek current_alat.

print("Status Alat Musik:", current_alat.status) adalah mencetak status alat musik yang disimpan pada atribut status dari objek current_alat.

print("-------------------------------") adalah mencetak garis pemisah antara setiap elemen pada daftar alat musik.

current_alat = current_alat.next_alat adalah mengatur nilai current_alat menjadi nilai atribut next_alat dari objek current_alat. Hal ini dilakukan untuk memindahkan posisi saat ini pada daftar alat musik ke elemen berikutnya.

![image](https://user-images.githubusercontent.com/121870536/225687168-e2ca2d7c-e4f9-4aad-8abb-bb43e8f869b0.png)

def cari_alat(self, nama): adalah definisi method cari_alat() yang akan digunakan untuk mencari alat musik berdasarkan nama.

current_alat = self.head adalah menginisialisasi variabel current_alat dengan nilai atribut head dari objek self. Variabel ini akan digunakan untuk menyimpan posisi saat ini dalam daftar alat musik.

while current_alat: adalah sebuah perulangan yang akan dilakukan selama current_alat bukan None. Hal ini dilakukan untuk mencari alat musik dengan nama yang dicari.

if current_alat.nama == nama: adalah melakukan pengecekan apakah nilai atribut nama dari objek current_alat sama dengan nilai nama yang dicari.

return current_alat adalah mengembalikan objek current_alat jika nama yang dicari ditemukan.

current_alat = current_alat.next_alat adalah mengatur nilai current_alat menjadi nilai atribut next_alat dari objek current_alat. Hal ini dilakukan untuk memindahkan posisi saat ini pada daftar alat musik ke elemen berikutnya.

return None adalah mengembalikan nilai None jika nama yang dicari tidak ditemukan pada daftar alat musik. Kode ini akan dieksekusi ketika perulangan selesai dijalankan dan tidak ada objek AlatMusik yang memiliki nilai atribut nama sama dengan nilai yang dicari.

![image](https://user-images.githubusercontent.com/121870536/225688102-5c53a0af-b061-4076-b257-a97052c36b42.png)

def update_alat(self, nama, jenis, status): adalah definisi method update_alat() yang akan digunakan untuk memperbarui informasi jenis dan status dari sebuah alat musik dengan nama tertentu.

alat_musik = self.cari_alat(nama) adalah memanggil method cari_alat() dengan parameter nama dan mengembalikan objek AlatMusik dengan nama yang sesuai. Objek ini akan disimpan di dalam variabel alat_musik.

if alat_musik: adalah sebuah kondisi yang memeriksa apakah alat_musik memiliki nilai yang tidak None. Jika iya, maka perintah pada blok berikutnya akan dieksekusi, yaitu memperbarui informasi jenis dan status dari alat musik.

alat_musik.jenis = jenis adalah mengatur nilai atribut jenis dari objek alat_musik dengan nilai parameter jenis.

alat_musik.status = status adalah mengatur nilai atribut status dari objek alat_musik dengan nilai parameter status.

else: adalah sebuah blok yang akan dieksekusi jika objek alat_musik bernilai None. Blok ini akan mencetak pesan "Alat musik tidak ditemukan".

![image](https://user-images.githubusercontent.com/121870536/225688532-0b19739f-0c0b-4a62-bdfb-aca5a7a9f41d.png)

def hapus_alat(self, nama): : method untuk menghapus alat musik dari daftar berdasarkan nama alat musik

current_alat = self.head : inisialisasi current_alat dengan head dari objek DaftarAlatMusik yang sedang dioperasikan

previous_alat = None : inisialisasi previous_alat dengan nilai None, yang akan menjadi penunjuk node sebelum current_alat saat melakukan iterasi pada linked list

while current_alat: : melakukan perulangan selama current_alat tidak bernilai None

if current_alat.nama == nama: : memeriksa apakah nama pada current_alat sama dengan nama yang diberikan pada method hapus_alat

if previous_alat: : memeriksa apakah previous_alat memiliki nilai selain None

previous_alat.next_alat = current_alat.next_alat : menghapus node dari linked list dengan mengubah nilai pointer next_alat dari previous_alat menjadi node setelah current_alat

else: : jika previous_alat bernilai None, maka node yang dihapus adalah head dari linked list sehingga head diubah menjadi node setelah current_alat

return : menghentikan method setelah node berhasil dihapus

previous_alat = current_alat : menyimpan current_alat sebagai previous_alat untuk iterasi selanjutnya

current_alat = current_alat.next_alat : mengubah current_alat menjadi node setelah current_alat untuk iterasi selanjutnya

print("Alat musik tidak ditemukan") : jika nama alat musik yang dicari tidak ditemukan pada linked list, maka akan mencetak pesan "Alat musik tidak ditemukan".

![image](https://user-images.githubusercontent.com/121870536/225689625-b90dea59-90a2-4f6b-9bef-a2cc56c351e1.png)

Fungsi input_data_alat() digunakan untuk meminta input dari pengguna untuk menambahkan data alat musik baru ke dalam daftar.

nama = : Meminta pengguna untuk memasukkan nama alat musik.
jenis = : Meminta pengguna untuk memasukkan jenis alat musik.
status = : Meminta pengguna untuk memasukkan status alat musik.
self.tambah_alat(nama, jenis, status) : Menambahkan alat musik baru ke dalam daftar menggunakan metode tambah_alat().
print("Alat musik telah ditambahkan ke dalam daftar") : Menampilkan pesan bahwa alat musik telah ditambahkan ke dalam daftar.

![image](https://user-images.githubusercontent.com/121870536/225691544-78107830-5880-4c0a-8211-cf17f79f4d32.png)

def tampilkan_menu(): adalah sebuah function dengan nama tampilkan_menu().
print("=== MENU ===") adalah sebuah perintah untuk menampilkan teks "=== MENU ===".
print("1. Tambah Alat Musik") adalah sebuah perintah untuk menampilkan teks "1. Tambah Alat Musik".
print("2. Tampilkan Daftar Alat Musik") adalah sebuah perintah untuk menampilkan teks "2. Tampilkan Daftar Alat Musik".
print("3. Cari Alat Musik") adalah sebuah perintah untuk menampilkan teks "3. Cari Alat Musik".
print("4. Update Alat Musik") adalah sebuah perintah untuk menampilkan teks "4. Update Alat Musik".
print("5. Hapus Alat Musik") adalah sebuah perintah untuk menampilkan teks "5. Hapus Alat Musik".
print("6. Keluar") adalah sebuah perintah untuk menampilkan teks "6. Keluar".

![image](https://user-images.githubusercontent.com/121870536/225693751-1cf8bb37-f146-40c8-b007-bc1f1e0a31b6.png)

def jalankan_program(): : ini adalah sebuah function dengan nama jalankan_program

print ("Selamat datang di GGEZ Music Studio\n") : ini adalah sebuah print statement yang mencetak string "Selamat datang di GGEZ Music Studio" dan membuat baris baru di akhirnya.

while True: : ini adalah sebuah while loop yang akan dijalankan terus menerus selama kondisi True terpenuhi.

tampilkan_menu() : ini adalah sebuah function call yang memanggil function tampilkan_menu()

pilihan = int(input("Masukkan pilihan Anda: ")) : ini adalah sebuah input statement yang meminta user untuk memasukkan pilihan mereka dan kemudian mengkonversi input tersebut ke tipe data integer.

print() : ini adalah sebuah print statement yang hanya membuat baris baru.

if pilihan == 1: : ini adalah sebuah if statement yang akan mengevaluasi apakah pilihan yang dimasukkan sama dengan angka 1.

os.system ("cls") : ini adalah sebuah system call yang akan membersihkan tampilan console.

daftar_alat_musik.input_data_alat() : ini adalah sebuah function call yang memanggil method input_data_alat() dari objek daftar_alat_musik.

elif pilihan == 2: : ini adalah sebuah elif statement yang akan mengevaluasi apakah pilihan yang dimasukkan sama dengan angka 2.

os.system ("cls") : ini adalah sebuah system call yang akan membersihkan tampilan console.

daftar_alat_musik.tampilkan_daftar() : ini adalah sebuah function call yang memanggil method tampilkan_daftar() dari objek daftar_alat_musik.

elif pilihan == 3: : ini adalah sebuah elif statement yang akan mengevaluasi apakah pilihan yang dimasukkan sama dengan angka 3.

os.system ("cls") : ini adalah sebuah system call yang akan membersihkan tampilan console.

nama = input("Masukkan nama alat musik yang ingin dicari: ") : ini adalah sebuah input statement yang meminta user untuk memasukkan nama alat musik yang ingin dicari.

alat_musik = daftar_alat_musik.cari_alat(nama) : ini adalah sebuah assignment statement yang akan menyimpan objek alat musik yang dicari ke dalam variabel alat_musik dengan memanggil method cari_alat(nama) dari objek daftar_alat_musik.

if alat_musik: : ini adalah sebuah if statement yang akan mengevaluasi apakah variabel alat_musik memiliki nilai yang truthy (tidak False, None, atau 0).

print("Nama Alat Musik:", alat_musik.nama) : ini adalah sebuah print statement yang akan mencetak nama alat musik yang ditemukan bersama dengan atribut nama dari objek alat_musik.

print("Jenis Alat Musik:", alat_musik.jenis) : ini adalah sebuah print statement yang akan mencetak jenis alat musik yang ditemukan bersama dengan atribut jenis dari objek alat_musik.

print("Status Alat Musik:", alat_musik.status) : ini adalah sebuah print statement yang akan mencetak status alat musik yang ditemukan bersama dengan atribut jenis dari objek alat_musik.

else : jika alat musik yang dicari tidak ada maka akan print "alat musik tidak ditemukan"

![image](https://user-images.githubusercontent.com/121870536/225698419-58c44995-ac0c-4326-bcf4-f17798f9f996.png)


elif pilihan == 4: ini adalah sebuah elif statement yang akan mengevaluasi apakah pilihan yang dimasukkan sama dengan angka 4.
os.system ("cls") : ini adalah sebuah system call yang akan membersihkan tampilan console.
nama = adalah inputan nama alat mausik yang akan di ubah
jenis = adalah inputan jenis alat musik yang diubah
status = adalah inputan status alat musik yang akan diubah
daftar_alat_musik.update_alat(nama, jenis, status) Memanggil metode "update_alat" pada objek "daftar_alat_musik" dan meneruskan nama, jenis, dan status sebagai parameter.
print Mencetak pesan "Data alat musik telah diupdate" sebagai umpan balik untuk pengguna.

elif pilihan == 5: merupakan kondisi jika pilihan yang diinputkan pengguna adalah 5, maka kode pada blok ini akan dieksekusi.

os.system("cls") digunakan untuk membersihkan tampilan layar terminal.

nama = input("Masukkan nama alat musik yang ingin dihapus: ") meminta pengguna untuk memasukkan nama alat musik yang ingin dihapus.

daftar_alat_musik.hapus_alat(nama) memanggil method hapus_alat dari objek daftar_alat_musik dengan argumen nama, sehingga data alat musik dengan nama tersebut akan dihapus dari daftar.

print("Data alat musik telah dihapus") menampilkan pesan bahwa data alat musik telah dihapus.

Jika pilihan pengguna adalah 6, maka layar terminal akan dibersihkan dan pesan "Terima Kasih telah berkunjung :)" akan ditampilkan. Selanjutnya perulangan while akan dihentikan menggunakan perintah break.

else "Pilihan tidak valid. Silakan coba lagi." akan ditampilkan untuk memberitahu pengguna bahwa pilihan yang dimasukkan tidak sesuai dengan opsi yang tersedia.

![image](https://user-images.githubusercontent.com/121870536/225699286-1e5c7259-1436-449b-80ba-f3fb5a6d1434.png)

daftar_alat_musik = DaftarAlatMusik() - Membuat objek DaftarAlatMusik baru dengan nama daftar_alat_musik. DaftarAlatMusik() adalah constructor untuk kelas DaftarAlatMusik.
daftar_alat_musik.tambah_alat("Gitar", "Senar", "Tersedia") - Memanggil metode tambah_alat() pada objek daftar_alat_musik untuk menambahkan alat musik baru dengan nama "Gitar", jenis "Senar", dan status "Tersedia".
daftar_alat_musik.tambah_alat("Drum", "Pukul", "Tidak Tersedia") - Memanggil metode tambah_alat() pada objek daftar_alat_musik untuk menambahkan alat musik baru dengan nama "Drum", jenis "Pukul", dan status "Tidak Tersedia".
daftar_alat_musik.tambah_alat("Bass", "Senar", "Tersedia") - Memanggil metode tambah_alat() pada objek daftar_alat_musik untuk menambahkan alat musik baru dengan nama "Bass", jenis "Senar", dan status "Tersedia".
daftar_alat_musik.tambah_alat("Keyboard", "Elektronik", "Tidak Tersedia") - Memanggil metode tambah_alat() pada objek daftar_alat_musik untuk menambahkan alat musik baru dengan nama "Keyboard", jenis "Elektronik", dan status "Tidak Tersedia".
jalankan_program() - Memanggil fungsi jalankan_program() yang menjalankan program utama.


**Output**

Menu Utama :
![image](https://user-images.githubusercontent.com/121870536/225836450-75d57293-9852-47bb-9d71-870dc42871f3.png)

Fungsi tambah :
![image](https://user-images.githubusercontent.com/121870536/225836677-33c748b6-85fc-4e8e-998c-b70b4707483a.png)

Fungsi tampil :
![image](https://user-images.githubusercontent.com/121870536/225836896-5f14d09b-86be-4c9f-a481-96b49ca787a0.png)

Fungsi search :
![image](https://user-images.githubusercontent.com/121870536/225837201-e15417f6-e010-4023-a7df-0f79f59eed00.png)

Fungsi update :
![image](https://user-images.githubusercontent.com/121870536/225837372-f40d05b0-8f55-4312-942e-80036c37dca8.png)

Fungsi hapus :
![image](https://user-images.githubusercontent.com/121870536/225837513-8d541f32-8843-4952-82aa-f3fbdce3bd1e.png)

Keluar :
![image](https://user-images.githubusercontent.com/121870536/225837573-6ef7e1ee-ba51-4dbd-a259-6086f462feb7.png)

