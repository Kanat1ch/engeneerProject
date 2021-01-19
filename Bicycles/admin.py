from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import Bsles
from .models import Marks
from .models import Type
from .models import Wheels


class InlineBsles(admin.TabularInline):
    model = Bsles


class BslesAdmin(ImportExportModelAdmin):
    list_filter = ('type',)
    list_display = ('stamp', 'type', 'wheels', 'weight', 'price')
    list_display_links = ('stamp',)
    search_fields = ('stamp', 'price')


class MarksAdmin(ImportExportModelAdmin):
    inlines = [InlineBsles, ]
    list_filter = ('mark',)
    list_display = ('mark', 'model')
    list_display_links = ('mark', 'model')
    search_fields = ('mark', 'model')


class TypeAdmin(ImportExportModelAdmin):
    inlines = [InlineBsles, ]
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


class WheelsAdmin(ImportExportModelAdmin):
    inlines = [InlineBsles, ]
    list_filter = ('mark',)
    list_display = ('mark', 'model', 'diameter')
    list_display_links = ('mark', 'model')
    search_fields = ('mark', 'model')


class FrameAdmin(ImportExportModelAdmin):
    inlines = [InlineBsles, ]
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Bsles, BslesAdmin)
admin.site.register(Marks, MarksAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Wheels, WheelsAdmin)
