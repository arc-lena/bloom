from django.contrib import admin
from .models import Partner, PartnerStatus, Promocode

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'points_required')

@admin.register(PartnerStatus)
class PartnerStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'partner', 'status', 'timestamp')

@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('promocode', 'partner')
