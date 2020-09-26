from django.contrib import admin
from .models import Contact,Review,Quote

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name','Subject')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('Name','Review','status')


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('title',)
    

admin.site.register(Contact,ContactAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Quote,QuoteAdmin)
