from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile) 
class ProfileAdmin(admin.ModelAdmin):
    # Поля, які будуть відображатися в списку об'єктів (list view) в адмінці
    list_display = ('user', 'location', 'birth_date')

    # Фільтри для бокової панелі, щоб зручно фільтрувати дані
    list_filter = ('location', 'birth_date')

    # Пошук по вказаних полях
    search_fields = ('user__username', 'location')

    # Поля, які будуть відображатися при перегляді/редагуванні об'єкта
    fieldsets = (
        (None, {
            'fields': ('user', 'bio', 'location', 'birth_date')
        }),
    )