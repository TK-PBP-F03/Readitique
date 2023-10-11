# UTS-PBP F03

## Anggota Kelompok :
- Dhafin Fadhlan Kamal
- Athira Reika
- Thaariq Kurnia Spama
- Kevin Ignatius Wijaya
- Melvara Zafirah Ramsi

## Cerita aplikasi yang diajukan serta manfaatnya
Book Club: Ada library buku dari database yg ada, terus setiap pengguna bisa nambahin ke Read, To Be Read, Favorites, book of the month


## Daftar modul yang akan diimplementasikan
1. Autentikasi pengguna
2. Reading list (read only/favorite, mark finished, etc)
3. Review (read rating/a few reviews only/add)
4. Book of the month (beda untuk user yg sudah login/belum login)
5. Profile (Admin/Reader/Writer)
6. Add buku (guest: lihat usulan terbaru, non-admin: usulkan dan voting buku, admin: terima dan tambah buku)


## Sumber dataset katalog buku
https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data

## Peran Pengguna
Login (Reader): Pengguna dapat menyimpan buku yang akan dibaca atau memasukkan ke dalam list favorit buku . Selain itu, pengguna dapat melihat semua review suatu buku dan bisa memberikan rating dan review pada buku tersebut. Pengguna juga bisa memberikan usulan terbaru mengenai buku yang akan ditambahkan dan melakukan voting buku yang akan diusulkan tersebut.
Login (Writer) : 
Tidak Login : Pengguna yang belum login atau bahkan belum memiliki akun hanya dapat mengakses beberapa fitur pada website ini seperti, hanya bisa membaca buku tanpa menyimpan ke favorite atau menandai bahwa buku itu belum selesai. Pengguna juga tidak bisa melihat review full dan memberikan review pada suatu buku. Pengguna juga hanya bisa melihat usulan buku baru yang ingin ditambahkan tanpa melakukan voting pada usulan tersebut. Jika pengguna belum memiliki akun, pengguna dapat membuat akun baru dengan membuat username dan password baru pada website tersebut. 
Admin : Menerima usulan voting kemudian menambahkan buku baru sesuai usulan voting tersebut. 

