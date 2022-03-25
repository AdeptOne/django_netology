from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Theme, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_quantity = 0
        for form in self.forms:
            if form.cleaned_data['is_main'] == True:
                main_tag_quantity += 1
        if main_tag_quantity > 1:
            raise ValidationError('Только один Тэг может быть основным')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline,]
    pass


@admin.register(Theme)
class ThemesAdmin(admin.ModelAdmin):
    pass
