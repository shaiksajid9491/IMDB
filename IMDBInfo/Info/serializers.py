from rest_framework.serializers import ModelSerializer

from .models import MovieInfo


class MovieSerializers(ModelSerializer):
    class Meta:
        model=MovieInfo
        fields='__all__'