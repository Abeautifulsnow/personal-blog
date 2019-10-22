from django.contrib import admin

from .models import RelatedLinks, SiteInfo, Expectation
# Register your models here.


@admin.register(RelatedLinks)
class RelatedLinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_name', 'link_url', 'link_desc')
    list_display_links = ('link_name',)
    list_editable = ('link_url',)
    list_per_page = 30


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_desc')


@admin.register(Expectation)
class ExpectationAdmin(admin.ModelAdmin):
    list_display = ('id', 'expect_desc')
