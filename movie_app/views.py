from rest_framework.decorators import api_view
from rest_framework.response import Response 
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from rest_framework import status
from django.db.models import Count, Avg

@api_view(http_method_names=['GET'])
def directors_list_api_view(request):
    directors = Director.objects.annotate(movies_count=Count('director'))
    # step 2: Reformat (Serialize) queryset to list of dictionaries
    data = DirectorSerializer(instance=directors, many=True).data
    # step 3: Response data and status 
    return Response(data=data, status=200)


@api_view(http_method_names=['GET'])
def movies_with_reviews_api_view(request):
    # Аннотация для среднего рейтинга по отзывам
    movies = Movie.objects.annotate(rating=Avg('reviews__stars'))
    data = MovieSerializer(instance=movies, many=True).data
    return Response(data=data, status=200)


@api_view(http_method_names=['GET'])
def movie_list_api_view(request):
    movie = Movie.objects.all()
    data = MovieSerializer(instance=movie, many=True).data
    return Response(data=data, status=200)

@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    review = Review.objects.all()
    data = ReviewSerializer(instance=review, many=True).data
    return Response(data=data, status=200)


@api_view(http_method_names=['GET'])
def review_detail_api_view(request, id):
    try:    
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error':'has not been found'}, status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(instance=review).data
    return Response(data=data, status=200)


@api_view(http_method_names=['GET'])
def movie_detail_api_view(request, id):
    try:    
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error':'has not been found'}, status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(instance=movie).data
    return Response(data=data, status=200)


@api_view(http_method_names=['GET'])
def directors_detail_api_view(request, id):
    try:    
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error':'has not been found'}, status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(instance=director).data
    return Response(data=data, status=200)