from rest_framework.generics import (
                            ListCreateAPIView,    
                            RetrieveUpdateDestroyAPIView,)
from ducks.models import Duck
from .serializers import DuckSerializer    
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated            

class DuckListView(ListCreateAPIView):
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer
    
    
class DuckDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)