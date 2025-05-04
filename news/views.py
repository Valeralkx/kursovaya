from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm, CommentForm
from django.views.generic import DetailView, UpdateView, DeleteView,  CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def article_detail(request, pk):
    article = Artiles.objects.get(pk=pk)
    comments = article.comments.all().order_by('-created_at')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('news-detail', pk=article.id)
    else:
        form = CommentForm()

    return render(request, 'news/details_view.html', {
        'article': article,
        'comments': comments,
        'form': form,
    })


def news_home(request):
    category = request.GET.get('category')
    if category:
        news = Artiles.objects.filter(category=category).order_by('-date')
    else:
        news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Artiles
    template_name = 'news/create.html'

    form_class = ArtilesForm


class NewsDeleteView(DeleteView):
    model = Artiles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = ArtilesForm()

    data = {
        'form':form,
        'error': error
    }

    return render(request, 'news/create.html', data)


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = Artiles
    form_class = ArtilesForm
    template_name = 'news/create.html'
    success_url = '/news/'