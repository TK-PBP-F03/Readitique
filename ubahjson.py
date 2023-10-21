import requests
from bs4 import BeautifulSoup
import json

# Baca dataset JSON Anda
with open('dataset_with_images.json', 'r') as json_file:
    data = json.load(json_file)

counter = 0
for book_info in data[:100]:
    if 'Image_URL' not in book_info:
        book_url = book_info['URL']
        print(book_url)
        # Akses halaman web buku
        response = requests.get(book_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Cari elemen gambar
            img_element = soup.find("img", class_="ResponsiveImage")  # Sesuaikan dengan struktur halaman web
            if img_element:
                img_url = img_element["src"]
                book_info['Image_URL'] = img_url
                print("URL Gambar Buku:", img_url)
            else:
                counter+=1
                print(counter)
                print("Gambar buku tidak ditemukan di halaman Goodreads.")

            # Simpan URL gambar ke dalam dataset

# Simpan dataset yang telah diperbarui
with open('dataset_with_images.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
