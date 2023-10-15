3# UTS-PBP F03

## Anggota Kelompok :
- Dhafin Fadhlan Kamal
- Athira Reika
- Thaariq Kurnia Spama
- Kevin Ignatius Wijaya
- Melvara Zafirah Ramsi

## Cerita aplikasi yang diajukan serta manfaatnya
Readitique adalah sebuah aplikasi perpustakaan digital yang memungkinkan pengguna untuk mengakses koleksi buku digital yang kaya. Aplikasi ini menawarkan fitur Reading List, yang memungkinkan pengguna untuk mengatur dan melacak buku-buku yang sudah mereka baca, ingin mereka baca, serta buku favorit. Pengguna dapat memberikan rating dan ulasan melalui fitur Review, serta membaca ulasan dari pengguna lain. "Book of the Month" menawarkan rekomendasi buku bulanan yang berbeda untuk pengguna yang sudah masuk dan yang belum login. Profil pengguna memiliki peran yang berbeda, termasuk Admin, Reader, dan Writer, dengan hak akses yang sesuai. Fitur Add Buku memungkinkan pengguna untuk mengusulkan dan memberikan suara pada buku yang ingin mereka lihat ditambahkan ke dalam koleksi. Dengan aplikasi ini, pengguna dapat menjalani pengalaman membaca yang terorganisir dan berinteraktif, serta berpartisipasi dalam komunitas literatur yang dinamis.

## Daftar modul yang akan diimplementasikan
1. Autentikasi pengguna (tiap orang)
2. Reading list (read only/favorite, mark finished, etc) (Melvara)
3. Review (read rating/a few reviews only/add) (Dhafin)
4. Book of the month (beda untuk user yg sudah login/belum login) (Thariq)
5. Profile (Admin/Reader/Writer) (Kevin)
6. Add buku (guest: lihat usulan terbaru, non-admin: usulkan dan voting buku, admin: terima dan tambah buku) (Reika)


## Sumber dataset katalog buku
https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data

## Peran Pengguna
- Login (Reader): Pengguna dapat menyimpan buku yang akan dibaca atau memasukkan ke dalam list favorit buku. Pengguna dapat membuka reading list pengguna lain dan melihat buku yang sudah dibaca, sedang dibaca, dan ingin dibaca pengguna tersebut. Mereka juga bisa membuat dan memodifikasi reading list yang mereka buat sendiri. Selain itu, pengguna dapat melihat semua review suatu buku dan bisa memberikan rating dan review pada buku tersebut. Pengguna juga bisa memberikan usulan terbaru mengenai buku yang akan ditambahkan dan melakukan voting buku yang akan diusulkan tersebut.
- Login (Writer) : Writer dapat melihat semua review yang diberikan pada buku-buku karya writernya.
- Tidak Login : Pengguna yang belum login atau bahkan belum memiliki akun hanya dapat mengakses beberapa fitur pada website ini seperti, hanya bisa membaca buku tanpa menyimpan ke favorite atau menandai bahwa buku itu belum selesai. Pengguna hanya bisa melihat buku yang sudah dibaca pengguna yang sudah login di reading list mereka dan tidak bisa membuat atau memodifikasi reading list tersebut. Pengguna juga tidak bisa melihat review full dan memberikan review pada suatu buku. Pengguna juga hanya bisa melihat usulan buku baru yang ingin ditambahkan tanpa melakukan voting pada usulan tersebut. Jika pengguna belum memiliki akun, pengguna dapat membuat akun baru dengan membuat username dan password baru pada website tersebut. 
- Admin : Menerima usulan voting kemudian menambahkan buku baru sesuai usulan voting tersebut. 



