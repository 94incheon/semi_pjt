from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Vote, Comment
from .forms import VoteForm, CommentForm


# Create your views here.
def index(request):
    votes = Vote.objects.order_by('-pk')
    context = {
        'votes': votes
    }
    return render(request, 'votes/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.user = request.user
            vote.save()
            return redirect('votes:index')
    else:
        form = VoteForm()
    context = {
        'form': form
    }
    return render(request, 'votes/form.html', context)


def detail(request, pk):
    vote = get_object_or_404(Vote, pk=pk)
    total_comment = vote.comments.count()
    agree = vote.comments.filter(pick='Agree').count()
    disagree = vote.comments.filter(pick='Disagree').count()
    if total_comment:
        blue = round((agree/total_comment)*100, 2)
        red = round((disagree/total_comment)*100, 2)
    else:
        blue = 0
        red = 0
    form = CommentForm()
    context = {
        'vote': vote,
        'form': form,
        'blue': blue,
        'red': red,
    }
    return render(request, 'votes/detail.html', context)

@login_required
def update(request, pk):
    vote = get_object_or_404(Vote, pk=pk)
    if request.user == vote.user:
        if request.method == 'POST':
            form = VoteForm(request.POST, instance=vote)
            if form.is_valid():
                vote = form.save(commit=False)
                vote.user = request.user
                vote.save()
                return redirect('votes:detail', vote.pk)
        else:
            form = VoteForm(instance=vote)
        context = {
            'form': form
        }
        return render(request, 'votes/form.html', context)
    else:
        # 1. 메시지프레임워크를 사용하여, 메인페이지로 이동.
        messages.warning(request, '본인 글만 수정 가능합니다.')
        return redirect('votes:detail', vote.pk)

@login_required
def delete(request, pk):
    vote = get_object_or_404(Vote, pk=pk)
    if request.user == vote.user:
        vote.delete()
    return redirect('votes:index')

def comments_create(request, pk):
    if request.user.is_authenticated:
        vote = get_object_or_404(Vote, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.vote = vote
            comment.user = request.user
            comment.save()
        return redirect('votes:detail', vote.pk)
    else:
        messages.warning(request, '댓글 작성을 위해서는 로그인이 필요합니다.')
        return redirect('accounts:login')

def random(request):
    import random
    votes = Vote.objects.all()
    random_vote = random.choice(votes)
    return redirect('votes:detail', random_vote.pk)

