from rest_framework import serializers
from movie_app.models import Movie, Review, Director

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Director
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True)  # Отображение текстов отзывов
    rating = serializers.FloatField(read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
        depth = 1
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        depth = 1
        
   
