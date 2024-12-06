from rest_framework import serializers
from .models import Comics
from rest)framework import viewsets
from .serializers import ComicsSerializer

#class ComicsSerializer(serializers.ModelSerializer):
 #      class Meta:
  #         model = Comics
   #        fields = '__all__'

class ComicViewSet(viewsets.ModelViewSet):
      queryset = Comics.objects.all()
      serializer_class = ComicsSerializer
