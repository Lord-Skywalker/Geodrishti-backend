from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ErosionData
from .serializers import ErosionDataSerializer

@api_view(['GET'])
def get_erosion_stats(request):  # <--- Check this name carefully!
    data = ErosionData.objects.all().order_by('year')
    serializer = ErosionDataSerializer(data, many=True)
    return Response(serializer.data)