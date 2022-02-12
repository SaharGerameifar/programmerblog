from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from account.mixins import AuthorAccessMixin
from article.models import Article, Category
from datetime import datetime, timedelta
from django.db.models import Count, Q, Max
from django.contrib.contenttypes.models import ContentType
from account.models import User
from django.core.paginator import Paginator


class ArticleList(ListView):
    queryset = Article.objects.published()
    paginate_by = 3


class ArticleDetail(DetailView):

    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(), slug=slug)

        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)

        return article


class CategoryList(ListView):
    paginate_by = 3
    template_name = 'article/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class ArticlePreview(AuthorAccessMixin, DetailView):
    template_name = 'article/article_detail.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)


def aside(request):
    last_month = datetime.today() - timedelta(days=30)
    content_type_id = ContentType.objects.get(app_label='article', model='article')
    popular_articles = Article.objects.published().annotate(
        count=Count('hits', filter=Q(articlehit__created__gt=last_month))).order_by('-count', '-publish')[:5]

    hot_articles = Article.objects.published().annotate(
        count=Count('comments', filter=Q(comments__posted__gt=last_month) and Q(
            comments__content_type_id=content_type_id))).order_by('-count', '-publish')[:5]

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
        # 'top_rate_articles': top_rate_articles
    }
    return render(request, 'shared/aside_partial.html', context)


class SearchList(ListView):
    paginate_by = 1
    template_name = 'article/search_list.html'

    def get_queryset(self):
        search = self.request.GET.get('search')
        return Article.objects.filter(Q(description__icontains=search) | Q(title__icontains=search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context


class AuthorList(ListView):
    paginate_by = 3
    template_name = 'article/author_list.html'

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
