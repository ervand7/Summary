from rest_framework.viewsets import ModelViewSet
from .models import Project, Measurement
from .serializers import ProjectSerializer, MeasurementSerializer


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    queryset = Measurement.objects.select_related('project')
    serializer_class = MeasurementSerializer
