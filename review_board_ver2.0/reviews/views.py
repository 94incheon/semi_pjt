from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    # reviews = Review.objects.all() # 게시글 작성일기준
    reviews = Review.objects.all().order_by('-updated_at') # 게시글 수정일 순으로 위부터 정렬
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)

def create(request):
    return render(request, 'reviews/create.html')

def new(request):
    title = request.GET.get('title')
    content = request.GET.get('content')    
    review = Review.objects.create(title=title, content=content)
    review.save()
    return redirect('/reviews')

def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review': review
    }
    return render(request, 'reviews/detail.html', context)

def update(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review': review
    }
    return render(request, 'reviews/update.html', context)

def apply_update(request, pk):
    review = Review.objects.get(pk=pk)
    title = request.GET.get('title')
    content = request.GET.get('content')
    review.title = title
    review.content = content
    review.save()
    return redirect('/reviews')

def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('/reviews')