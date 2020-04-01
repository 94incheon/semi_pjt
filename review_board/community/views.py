from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    reviews = list(Review.objects.all())[::-1] # 최신글이 맨위로 올라오게 했음.
    context = {
        'reviews': reviews
    }
    return render(request, 'review_list.html', context)


def new_review(request):
    return render(request, 'new_review.html')


def create_review(request):
    review = Review()
    review.title = request.GET.get('title')
    review.content = request.GET.get('content')
    review.rank = request.GET.get('rank')
    review.save()
    return redirect('/community/')


def review_detail(request, review_pk):
    review = Review.objects.get(id=review_pk)
    context = {
        'review': review
    }
    return render(request, 'review_detail.html', context)


def review_delete(request, review_pk):
    review = Review.objects.get(id=review_pk)
    review.delete()
    return redirect('/community/')


def review_update(request, review_pk):
    review = Review.objects.get(id=review_pk)
    review.title = request.GET.get('title')
    review.content = request.GET.get('content')
    review.save()
    return redirect('/community/')
