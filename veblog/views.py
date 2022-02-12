from django.shortcuts import render
from slider.models import Slider
from article.models import Category, Article
from datetime import datetime, timedelta
from django.db.models import Count, Q, Max
from django.contrib.contenttypes.models import ContentType
from account.models import User
from settings.models import SiteSettings


def home(request):
    last_month = datetime.today() - timedelta(days=30)
    content_type_id = ContentType.objects.get(app_label='article', model='article')
    popular_articles = Article.objects.published().annotate(
        count=Count('hits', filter=Q(articlehit__created__gt=last_month))).order_by('-count', '-publish')[:6]

    hot_articles = Article.objects.published().annotate(
        count=Count('comments', filter=Q(comments__posted__gt=last_month) and Q(
            comments__content_type_id=content_type_id))).order_by('-count', '-publish')[:6]

    most_visited_articles = Article.objects.published().annotate(
        count=Count('hits')).order_by('-count', '-publish')[:6]

    latest_articles = Article.objects.published().order_by( '-publish')[:6]


    sliders = Slider.objects.all()

    # top_rate_articles = Article.objects.published().annotate(
    #     max=Max('rates',
    #                 filter=Q(rates__created__gt=last_month) and
    #                        Q(rates__content_type_id=content_type_id) and
    #                        Q(rates__average__gte=0)
    #
    #                 )).order_by('-max', '-publish')[:5]

    context = {
        'popular_articles': popular_articles,
        'hot_articles': hot_articles,
        'most_visited_articles': most_visited_articles,
        'latest_articles': latest_articles,
        # 'top_rate_articles': top_rate_articles
        'sliders': sliders,

    }
    return render(request, 'home.html', context)


def navbar(request):
    categories = Category.objects.filter(status=True)
    site_settings = SiteSettings.objects.first()
    context = {
        'categories': categories,
        'settings': site_settings,
    }
    return render(request, 'shared/navbar.html', context)


def header(request, *args, **kwargs):
    site_settings = SiteSettings.objects.first()
    context = {
        'settings': site_settings,
    }
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    site_settings = SiteSettings.objects.first()
    context = {
        'settings': site_settings,
    }
    return render(request, 'shared/Footer.html', context)


def meta_header(request, *args, **kwargs):
    site_settings = SiteSettings.objects.first()
    context = {
        'settings': site_settings,
    }
    return render(request, 'shared/meta_header.html', context)


def about_us(request, *args, **kwargs):
    authors = User.objects.filter(Q(is_author=True) & Q(is_active=True))
    context = {
        'authors': authors,
    }
    return render(request, 'about.html', context)