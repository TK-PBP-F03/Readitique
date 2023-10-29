from django.test import TestCase
from .models import NewBook, UserVote
from django.contrib.auth.models import User

class NewBookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='testuser', password='testpassword')

        cls.new_book = NewBook.objects.create(
            title='Some Book',
            author='Some Author',
            description='A description for the book.',
            genre='Fiction',
            rating=4.5,
            image_link='https://example.com/sample-image.jpg',
            count_read=100,
            votes=10,
        )

    def test_title_max_length(self):
        book = NewBook.objects.get(id=self.new_book.id)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_author_max_length(self):
        book = NewBook.objects.get(id=self.new_book.id)
        max_length = book._meta.get_field('author').max_length
        self.assertEquals(max_length, 100)

    def test_genre_max_length(self):
        book = NewBook.objects.get(id=self.new_book.id)
        max_length = book._meta.get_field('genre').max_length
        self.assertEquals(max_length, 255)

    def test_object_name(self):
        book = NewBook.objects.get(id=self.new_book.id)
        expected_object_name = book.title
        self.assertEquals(str(book), expected_object_name)

class UserVoteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

        cls.new_book = NewBook.objects.create(
            title='Some Book',
            author='Some Author',
            description='A description for the book.',
            genre='Fiction',
            rating=4.5,
            image_link='https://example.com/sample-image.jpg',
            count_read=100,
            votes=10,
        )