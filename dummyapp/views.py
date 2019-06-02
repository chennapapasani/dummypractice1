from django.shortcuts import render
from .models import FeedbackData
from django.http.response import HttpResponse
from .forms import FeedBackForm
import datetime

date1 = datetime.datetime.now()


def home(request):
    return render(request, 'base.html')


def base_home(request):
    return render(request, 'homepage_base.html')


def base_contacts(request):
    return render(request, 'contactspage.html')


def base_courses(request):
    return render(request, 'coursespage.html')


def base_ourteam(request):
    return render(request, 'ourteam.html')


def base_feedback(request):
    if request.method == 'POST':
        fform = FeedBackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')
            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fform = FeedBackForm()
            return render(request, 'feedback.html', {'fform': fform})
        else:
            return HttpResponse('invalid user data')
    else:
        fform = FeedBackForm()
        return render(request, 'feedback.html', {'fform': fform})


def base_gallery(request):
    return render(request, 'gallery.html')
