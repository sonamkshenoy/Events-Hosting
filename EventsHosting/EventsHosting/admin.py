from django.contrib import admin
from .models import Event, Category, Booking

admin.site.register(Category)
admin.site.register(Event)

class CategoryListFilter(admin.SimpleListFilter):
    title='category'

    parameter_name = 'categoryName'
    default_value = None

    def lookups(self, request, model_admin):
        queryset = Booking.objects.all()
        return [('Fun','Fun'),('Art & Craft','Art & Craft'),('Education','Education')]

    def queryset(self, request, queryset):
        print(self.value())
        if self.value():
            return queryset.filter(category__category=self.value())
        return queryset


@admin.register(Booking)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'category',)
    list_filter = (CategoryListFilter, )
