from django.urls import path
from pypro.loto.views import games


app_name = 'loto'
urlpatterns = [
    path('games', games, name='games')
]
