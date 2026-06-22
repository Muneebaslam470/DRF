from .models import Person
from .serializers import PersonModelSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class MultipleObjAPIView(ListCreateAPIView): 
    serializer_class = PersonModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Person.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
class SingleObjAPIView(RetrieveUpdateDestroyAPIView):
   serializer_class = PersonModelSerializer
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]
     
   def get_queryset(self):
      return Person.objects.filter(user=self.request.user)  