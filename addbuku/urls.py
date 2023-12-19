from django.urls import path
from addbuku.views import add_buku, get_newbook_json, get_filtered, add_newbook_ajax, increment_votes, approve_book, show_json_by_id, show_json, create_newbook_flutter, vote_flutter

app_name = 'addbuku'
urlpatterns = [
    path('',add_buku,name='add_buku'),
    path('search/', get_filtered, name='get_filtered'),
    path('get-newbook-json/', get_newbook_json, name='get_newbook_json'),
    path('add-newbook-ajax/', add_newbook_ajax, name='add_newbook_ajax'),
    path('increment-votes/<int:id>/', increment_votes, name='increment_votes'),
    path('approve-book/<int:id>/', approve_book, name='approve_book'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('create-flutter/', create_newbook_flutter, name='create_newbook_flutter'),
    path('vote-flutter/', vote_flutter, name='vote_flutter')
]