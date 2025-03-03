from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors', views.directors_list_api_view),
    path('api/v1/movie', views.movie_list_api_view),
    path('api/v1/review', views.review_list_api_view),
    path('api/v1/directors/<int:id>/', views.directors_detail_api_view),
    path('api/v1/movie/<int:id>/', views.movie_detail_api_view),
    path('api/v1/review/<int:id>/', views.review_detail_api_view),
    path('api/v1/movies/reviews/', views.movies_with_reviews_api_view)
]
