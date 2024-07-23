from django.contrib import admin
from userauths.models import User
from .models import ContactMessage
from .models import EntradaJournal


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)
    
    
    
admin.site.register(EntradaJournal)

admin.site.register(User, UserAdmin)