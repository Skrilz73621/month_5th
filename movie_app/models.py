from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title =  models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(default=90)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director')
    
    def __str__(self):
        return f"{self.title} - {self.director}"

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
    
    def __str__(self):
        return f'{self.text}'
    
