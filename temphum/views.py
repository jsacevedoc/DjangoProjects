from rest_framework import viewsets
from .models import Temphum
from .serializers import TemphumSerializer

from .serializers import CultivoSerializer
from .models import Cultivo

class TemphumViewSet(viewsets.ModelViewSet):
    queryset = Temphum.objects.all().order_by('-created')
    serializer_class = TemphumSerializer

class CultivoViewSet(viewsets.ModelViewSet):
    queryset = Cultivo.objects.all().order_by('-created')
    serializer_class = CultivoSerializer 


