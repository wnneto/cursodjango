from django.shortcuts import render


def games(request):
    return render(request, 'loto/games.html')

