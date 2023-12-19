from django.http import JsonResponse
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .serializers import UserProfileSerializer
from rprofile.models import UserProfile
from rest_framework.permissions import IsAuthenticated

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserProfileListCreateView(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter the queryset to retrieve the user profile of the authenticated user
        return UserProfile.objects.filter(user=self.request.user)
    
def user_profiles(request):
    profiles = UserProfile.objects.all()
    serializer = UserProfileSerializer(profiles, many=True)
    return JsonResponse(serializer.data, safe=False)