import json
import codecs
import os
import django

# Replace 'your_project' with your project's name
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Readitique.settings")
django.setup()

from main.models import Book


with codecs.open('C:\\Users\\Dhafin\\Documents\\pelajaran\\kel_pbp\\Readitique\\dataset_with_images.json', 'r', encoding='utf-8') as json_file:
    datas = json.load(json_file)
for data in datas:
    # nyari data
    index_key = data['']
    title = data['Book']
    author = data['Author']
    description = data['Description']
    genre = data['Genres']
    rating = data['Avg_Rating']
    image_link = data['Image_URL']

    if len(Book.objects.filter(index_key=index_key)) == 0:
        new_book = Book(index_key=index_key,
                        title=title,
                        author=author,
                        description=description,
                        genre=genre,
                        rating=rating,
                        image_link=image_link,
                        )
        new_book.save()