from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Contact


def get_categories():
    """Barcha sahifalar uchun kategoriyalar"""
    return Category.objects.all()


def index(request):
    """Bosh sahifa"""
    featured = Article.objects.all()[:3]
    latest = Article.objects.all()[3:9]
    popular = Article.objects.order_by('-views')[:5]
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'featured_articles': featured,
        'latest_articles': latest,
        'popular_articles': popular,
        'categories': get_categories(),
    })


def article_detail(request, slug):
    """Maqola sahifasi"""
    article = get_object_or_404(Article, slug=slug)
    article.views += 1
    article.save()

    related = Article.objects.filter(category=article.category).exclude(id=article.id)[:4]

    return render(request, 'article.html', {
        'article': article,
        'related_articles': related,
        'categories': get_categories(),
    })


def category_view(request, slug):
    """Kategoriya sahifasi"""
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category)

    return render(request, 'category.html', {
        'category': category,
        'articles': articles,
        'categories': get_categories(),
    })


def about(request):
    """Biz haqimizda"""
    return render(request, 'about.html', {
        'categories': get_categories(),
    })


def contact(request):
    """Bog'lanish sahifasi"""
    success = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Ma'lumotlar bazasiga saqlash
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        success = True

    return render(request, 'contact.html', {
        'categories': get_categories(),
        'success': success,
    })