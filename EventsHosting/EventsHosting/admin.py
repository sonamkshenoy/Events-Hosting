from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(TicketType)
admin.site.register(EventTickets)

class CategoryListFilter(admin.SimpleListFilter):
    title='category'

    parameter_name = 'categoryName'
    default_value = None

    def lookups(self, request, model_admin):
        queryset = Booking.objects.all()
        categories = Category.objects.all()
        # Add events to filter
        queryList = []
        for i in categories:
            queryList.append((i.category, i.category))
        return queryList

    def queryset(self, request, queryset):
        print(self.value())
        if self.value():
            return queryset.filter(event__category__category=self.value())
        return queryset


@admin.register(Booking)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('token', 'name', 'emailid', 'event')
    list_filter = (CategoryListFilter, )
