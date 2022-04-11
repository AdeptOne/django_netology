from datetime import datetime

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleScope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_main = sum([1 for form in self.forms if form.cleaned_data.get('is_main')])
        if count_main > 1:
            raise ValidationError(f'Только Один Тэг может быть основным')
        elif count_main < 1:
            raise ValidationError(f'Один Тэг должен быть основным')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = ArticleScope
    extra = 3
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image', ]
    list_filter = ['title', 'text', 'published_at', ]
    inlines = [RelationshipInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name', ]
