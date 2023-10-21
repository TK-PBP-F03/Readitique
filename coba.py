import requests
from bs4 import BeautifulSoup

# URL halaman Goodreads
goodreads_url = "https://www.goodreads.com/book/show/2657.To_Kill_a_Mockingbird"

# Lakukan permintaan HTTP
response = requests.get(goodreads_url)

if response.status_code == 200:
    # Parsing HTML dengan BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Temukan elemen gambar
    img_element = soup.find("img", class_="ResponsiveImage")

    if img_element:
        # Dapatkan URL gambar dari atribut src
        img_url = img_element["src"]

        # Tampilkan URL gambar
        print("URL Gambar Buku:", img_url)
    else:
        print("Gambar buku tidak ditemukan di halaman Goodreads.")
else:
    print("Gagal mengakses halaman Goodreads.")
