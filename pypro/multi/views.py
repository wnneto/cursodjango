from django.shortcuts import render


def video(request, slug):
    return render(request, 'multi/video.html')
