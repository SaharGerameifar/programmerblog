from django.contrib import admin
from .models import Article, Category, IPAddress, ArticleHit
from account.models import User


# Register your models here.
def make_published(modeladmin, request, queryset):
    row_updated = queryset.update(status='p')
    if row_updated == 1:
        message_bit = "منتشر شد"
    else:
        message_bit = "منتشر شدند"
    modeladmin.message_user(request, "{} مقاله {}".format(row_updated, message_bit))
make_published.short_description = 'انتشار مقالات انتخاب شده'


def make_draft(modeladmin, request, queryset):
    row_updated = queryset.update(status='d')
    if row_updated == 1:
        message_bit = "پیش نویس شد"
    else:
        message_bit = "پیش نویس شدند"
    modeladmin.message_user(request, "{} مقاله {}".format(row_updated, message_bit))
make_draft.short_description = 'پیش نویس شدن مقالات انتخاب شده'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'slug', 'position', 'status')
    list_filter = (['status'])
    search_fields = (['title'])
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['queryset'] = User.objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


    list_display = ('title', 'author', 'thumbnail_tag', 'slug', 'jpublish', 'status', 'is_special', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']
    actions = [make_published, make_draft]


admin.site.register(Article, ArticleAdmin)
admin.site.register(IPAddress)
admin.site.register(ArticleHit)
